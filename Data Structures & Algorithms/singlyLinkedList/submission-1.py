class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:  # we get a pointer curr and i counter 
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        else:
            return -1

    def insertHead(self, val: int) -> None:  
        new_node = Node(val)
        if self.head: # if there already exist a linked list
            new_node.next = self.head
        else:   # if there is no linked list and we are going to create one
            self.tail = new_node
        self.head = new_node
        
    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail:   #if linked list exist 
            self.tail.next = new_node
        else:     #there is no linked list and we create it
            self.head = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        curr = self.head   # traverse the list to find the target node
        prev = None        # we keep track of the previous node ! 
        i = 0

        if not self.head or not self.tail:  #if there aint any list
            return False

        if index == 0:      #if the element is at index 0 (with edge cases)
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return True
            self.head = curr.next
            return True
        
        while curr: 
            if curr.next is None and i == index:    #if it is last index (self.tail)
                self.tail = prev
                prev.next = None
                return True
            elif i == index:         # any index in between
                prev.next = curr.next
                return True
            else:   # continuing the loop
                i += 1
                prev = curr
                curr = curr.next

        else:
            return False

    def getValues(self) -> List[int]:   
        link_list_arr = []
        curr = self.head
        while curr:
            link_list_arr.append(curr.val)
            curr = curr.next
        return link_list_arr

class Node:            # this class is for creating the node
    def __init__(self, val):
        self.val = val  
        self.next = None


# this is not the most optimized solution. But it is what i tried on my own. 
