"""141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list."""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
    
    def nthNode(self,n):
        count = 0
        curr = self.head
        while curr:
            if count == n:
                return curr
            count+=1
            curr = curr.next
        return None

    def addNodes(self,dataList,last_ptr):
        for data in dataList:
            new_node = ListNode(data)
            if self.head is None:
                self.head = new_node
                continue
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        new_node.next = self.nthNode(last_ptr)
    
    def hasCycle(self,head,pos):
        self.addNodes(head,pos)         #not needed for leetcode
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


print(LinkedList().hasCycle(head = [3,2,0,-4], pos = 1))            #True
print(LinkedList().hasCycle(head = [1,2], pos = 0))                 #True
print(LinkedList().hasCycle(head = [1], pos = -1))                  #False