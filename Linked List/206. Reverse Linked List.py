"""206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Input: head = [1,2]
Output: [2,1]
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def addNodes(self,dataList):
        for data in dataList:
            new_node = ListNode(data)
            if self.head is None:
                self.head = new_node
                continue
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        return self.head

    def nodeValues(self,head):
        res = []
        curr=head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    def reverseList(self,head):
        linked_list = self.addNodes(head)                 #Not needed on leetcode
        prev, curr = None, linked_list
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # return prev
        return self.nodeValues(prev)
    
print(LinkedList().reverseList(head = [1,2,3,4,5]))       #[5, 4, 3, 2, 1]
print(LinkedList().reverseList(head = [1,2]))             #[2, 1]