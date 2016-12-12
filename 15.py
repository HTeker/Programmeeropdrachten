class Node:
    def __init__(self, v, n = None):
        self.value = v
        self.next = n

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

    def printAll(self):
        node = self
        msg = ""

        while node:
            msg += node.value + ","
            node = node.getNext()

        print(msg)

mijnList = Node("a", Node("b", Node("c")))
mijnList.printAll()