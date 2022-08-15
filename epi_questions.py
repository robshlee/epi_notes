# Chapter 6: Strings



# Chapter 7: Linked Lists
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# 7.1 Merged Two Sorted Lists
def merged_lists(L1, L2):
    dummy = curr = Node(0)

    while L1 and L2:
        if L1.val < L2.val:
            curr.next = L1
            L1 = L1.next
        else:
            curr.next = L2
            L2 = L2.next

        curr = curr.next

    if L1:
         curr.next = L1
     
    if L2:
        curr.next = L2

    return dummy.next

# test case
# L1 = Node(2)
# L1.next = Node(5)
# L1.next.next = Node(7)
# L2 = Node(3)
# L2.next = Node(11)
# x = merged_lists(L1, L2)


# 7.2 Reverse a Single Sublist
def reverse_sublist(L, s, f):
    # step 1: get pointers to start of sub list
    # step 2: reverse sub list 
    # step 3: set head and tail of sub list correctly
    dummy = Node(0, L)
    left_sublist = dummy
    curr = L

    for i in range(s - 1):
        left_sublist = curr
        curr = curr.next

    prev = None

    for i in range(f - s + 1):
        nxt = curr.next
        curr.next = prev
        
        prev = curr
        curr = nxt

    left_sublist.next.next = curr
    left_sublist.next = prev

    return dummy.next

# test case
# 11 -> 3 -> 5 -> 7 -> 2 
# L = Node(11)
# L.next = Node(3)
# L.next.next = Node(5)
# L.next.next.next = Node(7)
# L.next.next.next.next = Node(2)
# reverse_sublist(L, 2, 4)


# 7.3: Test for Cyclicity
def cycle_test(head):
    seen = {}
    ind = 0

    while head:
        if head in seen:
            return seen[head]
        else:
            seen[head] = ind
            ind += 1

    return None

# test case
# 1 -> 2 -> 3 -> 4
#       <--------            
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = head.next
# cycle_test(head)


# 7.4 Test for Overlapping Lists- Lists are Cycle-free
def test_for_overlap(l1, l2):
    seen = []

    while l1:
        seen.append(l1)
        l1 = l1.next

    while l2:
        if l2 in seen:
            return True
        else:
            l2 = l2.next

    return False

# test case
# l1 = Node(1)
# l1.next = Node(2)
# l1.next.next = Node(3)
# l1.next.next.next = Node(4)
# l2 = Node(5)
# l2.next = l1.next
# test_for_overlap(l1, l2)


# 7.5 Test for Overlapping Lists- Lists may have cycles
def test_for_overlap(l1, l2):
    # loop through first list and mark each node seen
    seen = []
    slow = fast = Node(0, l1)

    while slow and slow != fast:
        slow = slow.next
        fast = fast.next.next
        seen.append(slow)

    while slow:
        if slow in seen:
            break
        else:
            seen.append(slow)
            slow = slow.next

    
    # loop through second list to check if any nodes have been visited
    while l2:
        if l2 in seen:
            return l2
        else:
            l2 = l2.next

    return None
    
    
# test case
# l1 = Node(1)
# l1.next = Node(2)
# l1.next.next = Node(3)
# l1.next.next.next = Node(4)
# l1.next.next.next.next = l1.next.next
# l2 = Node(5)
# l2.next = l1.next
# test_for_overlap(l1, l2)


# 7.6: Delete a Node From a Singly Linked List
def delete_node(head, delete_node):
    delete_node.val = delete_node.next.val
    delete_node.next = delete_node.next.next

    return head

# test case
# l1 = Node(1)
# l1.next = Node(2)
# l1.next.next = Node(3)
# l1.next.next.next = Node(4)
# delete_node(l1, l1.next)


# 7.7: Remove the kth Last Element from a List
def remove_kth_last_element(head, k):
    dummy = Node(0, head)
    l = r = head

    for i in range(k):
        r = r.next

    while r:
        l = l.next
        r = r.next

    l.val = l.next.val
    l.next = l.next.next

    return dummy.next

# test case
# 1 -> 2 -> 3 -> 4
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# remove_kth_last_element(head, 2)


# 7.8: Remove Duplicates From a Sorted List
def remove_dupes(head):
    dummy = Node(0, head)

    while head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next

    return dummy.next

# test case
# head = Node(1)
# head.next = Node(1)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# remove_dupes(head, 2)


# 7.9: Implement a Cycle Right Shift for Singly Linked List
def cyclic_shift(head, k):
    dummy = curr = counter = Node(0, head)
    n = 0

    while counter:
        n += 1
        counter = counter.next
    
    shifts = k % n

    if shifts == 0:
        return head

    # assign last node to first node
    while curr.next:
        curr = curr.next
    curr.next = dummy.next

    # assign dummy to start of new ordered list
    for i in range(shifts + 1):
        curr = curr.next
    dummy.next = curr.next

    # assign last node of new ordered list to none
    curr.next = None

    return dummy.next

# test case
# 1 -> 2 -> 3 -> 4
# 3 -> 4 -> 1 -> 2
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# cyclic_shift(head, 6)


# 7.10: Implement Even-Odd Merge
def even_odd_merge(head):
    dummy = Node(0, head)
    even = dummy.next
    odd = odd_head = dummy.next.next

    while even.next and odd.next:
        even.next = even.next.next
        odd.next = odd.next.next

        even = even.next
        odd = odd.next

    even.next = odd_head

    return dummy.next

# test case
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# even_odd_merge(head)


# 7.11: Test Whether a Singly Linked List is Palindromic
def test_palindrom(head):
    stack = []
    n = 0
    counter = head

    # get length of linked list
    while counter:
        n += 1
        counter = counter.next

    # get midpoint based on odd or even number length
    if n % 2 == 0:
        isOdd = 0
        mid = n / 2
    else:
        isOdd = 1
        mid = (n // 2) + 1

    # add to stack until midpoint
    c = 0
    curr = head

    while c < mid:
        stack.append(curr.val)
        curr = curr.next
        c += 1

    # if odd list length, remove the middle odd number from stack
    if isOdd:
        stack.pop()

    # check remaining node values against stack
    while curr:
        if curr.val == stack[-1]:
            stack.pop()
            curr = curr.next
        else:
            return print('no')

    return print('yes')

# test case
# 1 -> 2 -> 3 -> 2 -> 1
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(2)
# head.next.next.next.next = Node(1)
# test_palindrom(head)


# 7.12: Implement List Pivoting