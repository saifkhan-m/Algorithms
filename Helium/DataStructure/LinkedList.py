
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertafter(self, prev_node, data):
        if(prev_node is None):
            print('Not a valid node in the list')

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        new_node = Node(data)

        if(self.head is None):
            self.head = new_node
            return

        temp = self.head

        while(temp.next):
            temp = temp.next

        temp.next = new_node

    def printlist(self):
        if(self.head is None):
            print('Empty linked list')

        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

        print()


linked_list = LinkedList()
#
# linked_list.push(2)
# linked_list.push(5)
# linked_list.push(3)
#
# linked_list.append(6)
#
# # Insert 7 at the beginning. So linked list becomes 7->6->None
# linked_list.push(7)
#
# # Insert 1 at the beginning. So linked list becomes 1->7->6->None
# linked_list.push(1)
#
# # Insert 4 at the end. So linked list becomes 1->7->6->4->None
# linked_list.append(4)
#
# # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
# linked_list.insertafter(linked_list.head.next, 8)
#
#
# linked_list.printlist()
