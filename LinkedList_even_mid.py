# Definition for singly-linked list.

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def findMid(self, head):
        # Initialize the pointers
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next  # Move one step
            fast = fast.next.next  # Move two step

        return slow
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

# Create Solution object
obj = Solution()

# Find middle node
mid = obj.findMid(head)

# Print middle value
print("Middle Node Value:", mid.value)

