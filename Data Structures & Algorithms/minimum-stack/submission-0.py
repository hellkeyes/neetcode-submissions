class MinStack:

    def __init__(self):
        self.mystack = []   # for the main stack
        self.smallest = []  # to track the smallest in O(n)

    def push(self, value: int) -> None:
        self.mystack.append(value)  # this will append in the main stack
        if not self.smallest:    #whole loop to find the smallest at current level
            self.smallest.append(value)
        else:           
            current_min = min(value, self.smallest[-1])
            self.smallest.append(current_min)

    def pop(self) -> None:
        self.mystack.pop()  
        self.smallest.pop()  #remember to pop the element from smallest as well

    def top(self) -> int:
        return self.mystack[-1]    

    def getMin(self) -> int:
        return self.smallest[-1]
        