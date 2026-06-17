# Definition for Singly - linked list

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def hasCycle(self, head):
        # Initialize the pointers
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
    
head = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

head.next = second
second.next = third
third.next = fourth

# Create cycle
fourth.next = second

obj = Solution()
print(obj.hasCycle(head))















 