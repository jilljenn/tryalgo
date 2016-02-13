#!/usr/bin/env python3

import yaml

# tuples:
#   - nice
#   - chapter
#   - name
#   - links
L = []

def code(url):
    for c in ":/.":
        url = url.replace(c, " ")
    for w in url.split():
        if w not in ["http", "www", "acm", "https", "code", "google", "com", "uva", "informatik", "cs"]:
            return w
    return "?"

for item in yaml.load(open("problems.yaml").read()):
    if 'broken' in item:
        continue
    if 'order' in item:
        order = item['order'] - 1
    else:
        order = 3
    chapter = item['chapter']
    name = item['name']
    links = item['links']
    L.append((order, chapter, name, links))

L.sort(key = lambda t: (t[1].lower(),t[2].lower()))

cat = [':fish:', ':dolphin:', ':tropical_fish:', ':whale2:']

print("section | order | problem | link\n--- | --- | --- | ---")
for order, chapter, name, links in L:
    print("%s | %s | %s | " % (chapter, cat[order], name), end='')
    for a in links:
        print(' [[%s]](%s)' % (code(a), a),  end='')
    print()
print()