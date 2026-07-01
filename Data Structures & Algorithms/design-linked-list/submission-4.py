class MyLinkedList:

    def __init__(self):
        self.tail = None
        self.head = None
        

    def get(self, index: int) -> int:
        i = 0
        curr = self.head

        if self.head is None:  # if not list return - 1
            return -1
        
        while curr:  
            if i == index:  # if it is valid within the index 
                return curr.val
            i += 1
            curr = curr.next
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.tail = new_node 
        else:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node       

    def addAtTail(self, val: int) -> None:
        new_node = Node(val) 

        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node  

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        curr = self.head
        
        if self.head is None:
            if index == 0:  # if no list
                self.addAtHead(val)
                return 
            elif index > 0:
                return

        if index == 0:    # if it is head
                self.addAtHead(val)
                return

        while curr:

            if i == index:  # if in between
                new_node = Node(val) 
                left_pointer = curr.prev
                # ----------------------------
                left_pointer.next = new_node 
                new_node.prev = left_pointer
                curr.prev = new_node
                new_node.next = curr
                return

            i += 1
            curr = curr.next
        
        if curr == None and index == i:
            new_node = Node(val) 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return
            

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head

        if self.head is None:  # if no list
            return 

        if index == 0:    # if index is first and it is only node
            if self.head.next == None:
                self.head = None
                self.tail = None
                return
            else:
                self.head = self.head.next
                self.head.prev = None
                return


        while curr: 
            if curr.next == None and index == i: # if last value
                self.tail = curr.prev
                self.tail.next = None
                return

            if i == index:  # if in between
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return

            i += 1
            curr = curr.next

    
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)