# from .LinkedList import LinkedList
from DataStructure.LinkedList import LinkedList

linked_list = LinkedList()

linked_list.push(2)
linked_list.push(5)
linked_list.push(3)

linked_list.append(6)

# Insert 7 at the beginning. So linked list becomes 7->6->None
linked_list.push(7)

# Insert 1 at the beginning. So linked list becomes 1->7->6->None
linked_list.push(1)

# Insert 4 at the end. So linked list becomes 1->7->6->4->None
linked_list.append(4)

# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
linked_list.insertafter(linked_list.head.next, 8)


linked_list.printlist()
