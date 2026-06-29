class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
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
        if self.head:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node
        
    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        curr = self.head
        prev = None
        i = 0

        if not self.head or not self.tail:
            return False

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return True
            self.head = curr.next
            return True
        
        while curr:
            if curr.next is None and i == index:
                self.tail = prev
                prev.next = None
                return True
            elif i == index:
                prev.next = curr.next
                return True
            else:
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

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
