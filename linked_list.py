class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_daa(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class UnorderedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

temp = Node(93)
print(temp.get_data())

mylist = UnorderedList()
mylist.add(10)
mylist.add(15)
mylist.add(19)
mylist.add(12)
mylist.add(6)

class OrderedList(object):
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def size(self):
        current = self.head
        counter = 0
        while current != None:
            counter += 1
            current = current.get_next()
        return counter
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            elif current.get_data() < item:
                break
            else:
                current = current.get_next()
        return found
    def add(self, item):
        current = self.head
        previous = None
        while current != None:
            if current.get_data() < item:
                previous = current
                current = current.get_next()
            else:
                break
        new_node = Node(item)
        if previous == None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(current)
            previous.set_next(temp)

print(mylist.search(6))
