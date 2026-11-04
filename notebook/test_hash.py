from heapq import heappush, heappop


def huffman(freq):
    forest = [] ;    trees = []      # asd
    for item in freq:
        heappush(forest, (freq[item], len(trees)))
        trees.append(item)  
    while len(forest) > 1:
        (f_l, left) = heappop(forest)        
        (f_r, right) = heappop(forest)
        heappush(forest, (f_l + f_r, len(trees)))
        trees.append([trees[left], trees[right]])
    code = {}                                
    extract(code, trees[forest[0][1]], [])
    return code



def extract(code, tree, prefix):
    if isinstance(tree, list):        # aha
        left, right = tree
        prefix.append('0')
        extract(code, left, prefix)   
        prefix.pop()
        prefix.append('1')
        extract(code, right, prefix)  
        prefix.pop()
    else:
        code[tree] = ''.join(prefix)
