class Node:
    size = 0

    def __init__(self, v, n = None):
        self.value = v
        self.next = n

        self.setSize()

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

    def setSize(self):
        node = self

        while node:
            node = node.getNext()
            self.size += 1

    def printAll(self):
        node = self
        msg = ""

        while node:
            msg += node.value + ","
            node = node.getNext()

        print(msg)

mijnList = Node("a", Node("b", Node("c")))
print(mijnList.size == 3)