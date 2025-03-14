# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()  # Dummy node to simplify merging
        tail = dummy  # Tail pointer to track the merged list
    
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move the tail forward
    
        # Attach the remaining nodes
        tail.next = list1 if list1 else list2
    
        return dummy.next  # Return the head of the merged list
