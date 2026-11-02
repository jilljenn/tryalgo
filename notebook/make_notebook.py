#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a Typst notebook from tagged Python snippets."""
from __future__ import annotations

import argparse
import ast
import subprocess
import json
import os
from pathlib import Path
import re

ICPC_TITLE = re.compile(r'^\s*#\s*icpc-title\s+(.+?)\s*$')
START = re.compile(r'^\s*#\s*snip\{\s*(.*?)\s*$')
END = re.compile(r'^\s*#\s*snip\}\s*$')
PYLINT = re.compile(r'^\s*#\s*pylint\b', re.IGNORECASE)
ICPC_IGNORE = re.compile(r'^\s*#\s*icpc-ignore\s*$')
DEF = re.compile(r'^\s*(?:async\s+)?def\s+([A-Za-z_]\w*)\s*\(')
CLASS = re.compile(r'^\s*class\s+([A-Za-z_]\w*)\b')

TEMPLATE = r'''// Python snippets grouped by source file, excluding pylint directives.
#set page(
  paper: "a4", flipped: true, columns: 2,
  margin: (top: 13mm, bottom: 17mm, left: 13mm, right: 13mm),
  footer: context {
    let numero = here().page()
    let balises = query(<repere-fichier>)
    let noms = ()
    for repere in balises {
      if repere.location().page() == numero {
        let nom = repere.value.nom
        if not (nom in noms) { noms.push(nom) }
      }
    }
    block(
      width: 100%, stroke: (top: 0.5pt + rgb("#CCD5E0")),
      inset: (top: 5pt),
      grid(columns: (1fr, auto), gutter: 12pt,
        [#text(size: 7.3pt, fill: rgb("#52627A"))[#if noms.len() == 0 { [—] } else { noms.map(n => raw(n)).join([ · ]) }]],
        [#text(size: 7.3pt, weight: "bold", fill: rgb("#28486A"))[#counter(page).display("1 / 1", both: true)]]
      ),
    )
  },
)
#set columns(gutter: 8mm)
#set text(font: "DejaVu Sans", size: 8.6pt, fill: rgb("#243448"))
#set par(leading: 0.45em, spacing: 0.6em)
#set raw(tab-size: 4)
#show raw.where(block: true): set text(font: "DejaVu Sans Mono", size: 7.2pt)
#let extrait(empreinte, code) = block(
  width: 100%, fill: rgb("#F5F7FA"),
  stroke: 0.4pt + rgb("#E3E9F0"),
  inset: (x: 7pt, y: 7pt), radius: 3pt,
  above: 4pt, below: 9pt,
)[
  // place is an overlay: it consumes no vertical space.
  // The hash aligns with the first line of the code.
  #place(top + right)[#text(size: 5.7pt, fill: rgb("#718198"))[#raw(empreinte)]]
  #code
]

#let fichier(nom) = block(sticky: true, above: 8pt, below: 6pt)[
  #metadata((nom: nom)) <repere-fichier>
  #text(size: 12pt, weight: "bold", fill: rgb("#17456B"))[#raw(nom)]
]

#let illustration(chemin, hauteur) = block(above: 1pt, below: 7pt)[
  #image(chemin, height: hauteur)
]

__BODY__
'''


def typst_string(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def raw_fence(code: str) -> str:
    longest = max((len(m.group()) for m in re.finditer(r'`+', code)), default=0)
    fence = '`' * max(3, longest + 1)
    return f'{fence}python\n{code.rstrip()}\n{fence}'


def cleaned_code(code: str) -> str:
    """Canonical Python code for hashing: parse, remove docstrings, unparse.

    ast.unparse preserves Python syntax, drops comments, and normalizes
    whitespace. Hash the exact output without adding a trailing newline.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError as exc:
        raise ValueError(f"invalid Python snippet for MD5 computation : {exc}") from exc

    class RemoveDocstrings(ast.NodeTransformer):
        def _strip(self, node: ast.AST) -> ast.AST:
            body = node.body
            if (body and isinstance(body[0], ast.Expr)
                    and isinstance(body[0].value, ast.Constant)
                    and isinstance(body[0].value.value, str)):
                # An otherwise empty body must still contain a statement.
                node.body = body[1:] or [ast.copy_location(ast.Pass(), body[0])]
            return node

        def visit_Module(self, node: ast.Module) -> ast.AST:
            self.generic_visit(node)
            return self._strip(node)

        def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
            self.generic_visit(node)
            return self._strip(node)

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> ast.AST:
            self.generic_visit(node)
            return self._strip(node)

        def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:
            self.generic_visit(node)
            return self._strip(node)

    tree = RemoveDocstrings().visit(tree)
    ast.fix_missing_locations(tree)
    return ast.unparse(tree)


def md5sum(code: str) -> str:
    """Hash cleaned code with the md5sum command, exactly as requested."""
    cleaned = cleaned_code(code)
    try:
        process = subprocess.run(['md5sum'], input=cleaned.encode('utf-8'),
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 check=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError(f"md5sum failed : {exc}") from exc
    return process.stdout.decode('ascii').split()[0]


def infer_name(block: str, tag: str) -> str:
    for line in block.splitlines():
        m = DEF.match(line) or CLASS.match(line)
        if m:
            return m.group(1)
    return tag or 'snippet'


def snippets(path: Path) -> list[tuple[str, str]]:
    """Extract included snippets without delimiters or pylint directives."""
    result = []
    tag = None
    content = []
    opened_at = 0
    previous_nonempty = ""
    skipped = False
    for lineno, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        start = START.match(line)
        if start:
            if tag is not None:
                raise ValueError(f'{path}:{lineno}: # snip{{ nested (opened at line {opened_at})')
            tag, content, opened_at = start.group(1).strip(), [], lineno
            skipped = bool(ICPC_IGNORE.match(previous_nonempty))
        elif END.match(line):
            if tag is None:
                raise ValueError(f'{path}:{lineno}: # snip}} without opening tag')
            code = '\n'.join(content).strip('\n')
            if code.strip() and not skipped:
                result.append((infer_name(code, tag), code))
            tag, content, skipped = None, [], False
        elif tag is not None and not PYLINT.match(line):
            content.append(line)
        if line.strip():
            previous_nonempty = line
    if tag is not None:
        raise ValueError(f'{path}:{opened_at}: # snip{{ without closing tag')
    return result


IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp', '.svg', '.pdf')


def image_for(path: Path, image_dir: Path) -> Path | None:
    """Return the first matching image (case-insensitive extension)."""
    choices = {p.name.lower(): p for p in image_dir.iterdir() if p.is_file()}
    for extension in IMAGE_EXTENSIONS:
        result = choices.get(f'{path.stem}{extension}'.lower())
        if result is not None:
            return result
    return None




def source_title(path: Path) -> str:
    """Use the first nonempty icpc-title directive, or format the filename."""
    for line in path.read_text(encoding='utf-8-sig').splitlines():
        match = ICPC_TITLE.match(line)
        if match:
            return match.group(1).strip()
    return path.stem.replace('_', ' ').title()


def typst_for(path: Path, image_dir: Path) -> Path | None:
    """Find a Typst companion file with the same basename."""
    for candidate in image_dir.iterdir():
        if candidate.is_file() and candidate.suffix.lower() == '.typ' and candidate.stem.lower() == path.stem.lower():
            return candidate
    return None

def image_reference(image_path: Path, typst_path: Path) -> str:
    """Make images accessible relative to the generated .typ file."""
    return Path(os.path.relpath(image_path.resolve(), typst_path.parent.resolve())).as_posix()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source_dir', type=Path, help='directory containing *.py files')
    parser.add_argument('--images', type=Path, default=None, help='directory containing optional matching images or .typ files')
    parser.add_argument('--image-height', default='1cm', help='image height, e.g. 1cm or 15mm (default: 1cm)')
    parser.add_argument('--cleaned-dir', type=Path, default=None,
                        help='export the exact normalized snippet bytes used for hashing')
    parser.add_argument('--title-file', type=Path, default=Path('title.typ'), help='Typst file included at the start (default: title.typ)')
    parser.add_argument('-o', '--output', type=Path, default=Path('notebook.typ'))
    args = parser.parse_args()
    if not args.source_dir.is_dir():
        parser.error(f'source directory not found : {args.source_dir}')
    if args.images is not None and not args.images.is_dir():
        parser.error(f'image directory not found : {args.images}')
    if not re.fullmatch(r'(?:\d+(?:\.\d+)?|\.\d+)(?:mm|cm|pt|in)', args.image_height):
        parser.error('invalid height, e.g. : 1cm, 12mm, 20pt')
    if not args.title_file.is_file():
        parser.error(f'title file not found : {args.title_file}')

    title_ref = image_reference(args.title_file, args.output)
    bodies = [f'#include {typst_string(title_ref)}']
    count = 0
    if args.cleaned_dir is not None:
        args.cleaned_dir.mkdir(parents=True, exist_ok=True)
    files = list(args.source_dir.glob('*.py'))
    sections = []
    for path in files:
        try:
            items = snippets(path)
        except (ValueError, UnicodeError) as exc:
            parser.error(str(exc))
        if items:
            sections.append((source_title(path), path, items))

    # Sort by the actual heading rendered in Typst, not by source filename.
    sections.sort(key=lambda section: (section[0].casefold(), section[1].name.casefold()))
    rendered_titles = []
    for title, path, items in sections:
        rendered_titles.append(title)
        bodies.append(f'#fichier({typst_string(title)})')
        if args.images is not None:
            image = image_for(path, args.images)
            if image is not None:
                reference = image_reference(image, args.output)
                bodies.append(f'#illustration({typst_string(reference)}, {args.image_height})')
            else:
                companion = typst_for(path, args.images)
                if companion is not None:
                    reference = image_reference(companion, args.output)
                    bodies.append(f'#include {typst_string(reference)}')
        for snippet_idx, (name, code) in enumerate(items, 1):
            try:
                digest = md5sum(code)
            except ValueError as exc:
                parser.error(f'{path} ({name}) : {exc}')
            if args.cleaned_dir is not None:
                # Preserve exactly the UTF-8 bytes passed to md5sum.
                clean_path = args.cleaned_dir / f'{path.stem}_{snippet_idx:02d}.py'
                clean_path.write_bytes(cleaned_code(code).encode('utf-8'))
            bodies.append(f'#extrait({typst_string(digest[:6])}, [\n{raw_fence(code)}\n])')
            count += 1
    if not count:
        parser.error('no included # snip{ ... # snip} blocks found')
    # Catch accidental regressions in the ordering of generated headings.
    assert rendered_titles == sorted(rendered_titles, key=str.casefold), 'Section headings are not sorted'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(TEMPLATE.replace('__BODY__', '\n\n'.join(bodies)), encoding='utf-8')
    print(f'{args.output} : {count} snippets from {len(sections)} sections ({len(files)} Python files examined, sorted by heading)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
