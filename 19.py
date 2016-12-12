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

    def get(self, index):
        node = self

        for x in range(0, index):
            node = node.getNext()

        return node

    def printAllReverse(self):
        node = self
        str = ""
        msg = ""

        while node:
            str += node.value
            node = node.getNext()

        for x in range(0, len(str)):
            msg += str[len(str) - x -1] + ","

        print(msg)

    def delete(self, index):
        node = self.get(index)

        previousNode = self.get(index - 1)
        previousNode.next = self.get(index + 1)

        return node.value



mijnList = Node("a", Node("b", Node("c", Node("d"))))
mijnList.printAll()
opgeruimd = mijnList.delete(2)
print(opgeruimd == "c")
mijnList.printAll()
