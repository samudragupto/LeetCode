from collections import Counter
from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.serial = None

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node()
        for path in paths:
            cur = root
            for folder in path:
                if folder not in cur.children:
                    cur.children[folder] = Node()
                cur = cur.children[folder]

        def compute_serial(node):
            if not node.children:
                node.serial = ''
                return ''
            subs = []
            for k in sorted(node.children):
                subs.append(k + '(' + compute_serial(node.children[k]) + ')')
            node.serial = ''.join(subs)
            return node.serial

        compute_serial(root)

        serial_count = Counter()
        def count_serial(node):
            if node.serial is not None and node.serial != '':
                serial_count[node.serial] += 1
            for child in node.children.values():
                count_serial(child)

        count_serial(root)

        def clean_tree(node):
            to_remove = []
            for k, child in list(node.children.items()):
                clean_tree(child)
                if child.serial != '' and serial_count[child.serial] > 1:
                    to_remove.append(k)
            for k in to_remove:
                del node.children[k]

        clean_tree(root)

        ans = []
        def collect(node, path):
            for k in node.children:
                ans.append(path + [k])
                collect(node.children[k], path + [k])

        collect(root, [])
        return ans
