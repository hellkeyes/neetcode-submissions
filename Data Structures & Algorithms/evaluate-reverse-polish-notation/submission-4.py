class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []
        i = 0

        for i in range(len(tokens)):
            if tokens[i] in "+-&/*":
                r = mystack.pop()
                l = mystack.pop()

                if tokens[i] == "+":
                    res = l + r
                elif tokens[i] == "-":
                    res = l - r
                elif tokens[i] == "*":
                    res = l * r
                elif tokens[i] == "/":
                    res = int(l / r)

                mystack.append(res)
            else: 
                mystack.append(int(tokens[i]))

        return mystack[0]
            