class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def push(self, data):                       # inserting at the begining of linkedist
        new_data = Node(data)                   # TC - O(1)  AS - O(1)
        new_data.next = self.head
        self.head = new_data

    def insertAfter(self,prev_node,data):       # inserting after a node of linkedist
        if prev_node is None:                   # TC - O(1)  AS - O(1)
            print("prev node musn't be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,data):                      # inserting at the end of linkedist
        new_node = Node(data)                   # TC - O(n)  AS - O(1)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next  
        last.next = new_node

    def delete(self,key):                       # iterative method to delete a node
        current = self.head
        if current and current.data == key:     # if the first element is to be deleted
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:                     # if key is not found in linked list
            print(key, "not found in the linkedlist")
            return
        prev.next = current.next                
        print(key, "removed from the linkedlist")
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")

    def getCount(self):                         # TC - O(n)  AS - O(1)
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(count)
        return
    
    def getNth(self,index):
        current = self.head
        count = 0
        while current:
            if count == index:
                print("[",index,"] - ", current.data,sep="")
                return
            current =current.next
            count+=1
        print("index out of bound")
        return

    def findMiddle(self):
        if self.head is None:
            print("empty Linkedlist...")
            return
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        print(slow_ptr.data)
        return 


linked_list = LinkedList()

linked_list.findMiddle()                        #empty Linkedlist...

linked_list.push("third")
linked_list.push("second")
linked_list.push("first")
linked_list.display()                           #first -> second -> third -> Null

linked_list.insertAfter(linked_list.head,"new")
linked_list.display()                           #first -> new -> second -> third -> Null

linked_list.append("last")
linked_list.display()                           #first -> new -> second -> third -> last -> Null

linked_list.findMiddle()                        #second

linked_list.delete("new")                       #new removed from the linkedlist
linked_list.display()                           #first -> second -> third -> last -> Null

linked_list.findMiddle()                        #third

linked_list.delete("nwew")                      #nwew not found in the linkedlist
linked_list.display()                           #first -> second -> third -> last -> Null

linked_list.getCount()                          #4
linked_list.getNth(2)                           #[2] - third
linked_list.getNth(100)                         #index out of bound