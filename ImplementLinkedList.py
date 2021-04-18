# A class that would have the node implementation
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # a function to insert element in a linked list
    def insert(self, data):
        # check if linkedlist is empty
        for val in data:
            if self.head is None:
                self.insert_at_beginning(val)
            # have a sorted linked list
            else:
                itr = self.head
                while itr.next:
                    itr = itr.next
                if itr.data < val:
                    node = Node(val)
                    itr.next = node
                else:
                    itr.next = Node(itr.data)
                    itr.data = val

    def insert_at_beginning(self, val):
        self.head = Node(val)

    def insert_at(self, index, val):
        if self.head is None:
            raise Exception("Linked List is empty")
        itr = self.head
        count = 0
        while itr.next:
            if count == index - 1:
                itr.next = Node(itr.data, itr.next)
                itr.data = val
                break
            count += 1
            itr = itr.next

    def insert_at_end(self, val):
        if self.head is None:
            self.insert_at_beginning(val)
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(val)
        itr.next = node

    def delete(self, val):
        if self.head is None:
            raise Exception("Linked List is empty")
        itr = self.head
        while itr.next:
            if itr.data == val:
                itr.data = itr.next.data
                itr.next = itr.next.next if itr.next.next else None
            else:
                itr = itr.next
        if itr.data == val:
            self.remove_last_node()

    def remove_last_node(self):
        itr = self.head
        second_last = itr
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def find_element(self, ele):
        if self.head is None:
            raise Exception("Linked List is empty")
        itr = self.head
        while itr.next:
            if itr.data == ele:
                return True
            itr = itr.next
        return False

    def find_index(self, val):
        if self.head is None:
            raise Exception("Linked List is empty")
        index = 0
        itr = self.head
        while itr.next:
            if itr.data == val:
                return index
            index += 1
            itr = itr.next
        return index

    def print(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)


test = LinkedList()
test.insert([1, 6, 4, 7])
print(test.find_element(8))
test.print()
print(test.find_index(7))
test.insert_at(2, 10)
test.print()
test.insert_at_end(19)
test.print()
test.delete(7)
test.print()
test.print()
test.print()
test.print()
test.print()
test.print()
