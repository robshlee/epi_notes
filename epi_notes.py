# Chapter 7: Linked Lists

# node example
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# search list
def search_list(L, key):
    while L and L.val != key:
        L = L.next
    # if key was not present in the list, L will have become None and will return None
    return L

# test case
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# search_list(head, 4)

# insert new node after node
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

# delete node past this one. Assume node is not a tail
def delete_after(node):
    node.next = node.next.next

