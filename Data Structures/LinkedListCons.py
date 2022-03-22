class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def popfirst(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        if self.length == 0:
            self.tail == None
        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def setvalue(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insertval(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

new = LinkedList(0)
for i in range(1,3):
    new.append(i)
new.insertval(2, 4)
new.printlist()