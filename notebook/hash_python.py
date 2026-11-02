import ast, hashlib, sys
with open(sys.argv[1], encoding="utf-8") as f:
    code = f.read()
normalized = ast.unparse(ast.parse(code))  + "\n"
hashcode = hashlib.md5(normalized.encode("utf-8")).hexdigest()
print(hashcode[:6])