class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_count = {}
        self.count_node = {}
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node[node.count]

    def inc(self, key: str) -> None:
        count = self.key_count.get(key, 0)
        new_count = count + 1
        self.key_count[key] = new_count

        current_node = self.count_node.get(count)
        new_node = self.count_node.get(new_count)

        if not new_node:
            new_node = Node(new_count)
            self.count_node[new_count] = new_node
            if not current_node:
                self._add_node_after(new_node, self.head)
            else:
                self._add_node_after(new_node, current_node)
        new_node.keys.add(key)

        if current_node:
            current_node.keys.discard(key)
            if not current_node.keys:
                self._remove_node(current_node)

    def dec(self, key: str) -> None:
        count = self.key_count[key]
        current_node = self.count_node[count]
        current_node.keys.discard(key)

        if count == 1:
            del self.key_count[key]
        else:
            new_count = count - 1
            self.key_count[key] = new_count
            new_node = self.count_node.get(new_count)
            if not new_node:
                new_node = Node(new_count)
                self.count_node[new_count] = new_node
                self._add_node_after(new_node, current_node.prev)
            new_node.keys.add(key)

        if not current_node.keys:
            self._remove_node(current_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
