class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mystack = []
        n = len(temperatures)
        mylist = [0] * n
        j = 1

        mystack.append(0)

        while j < len(temperatures):

            while mystack and temperatures[mystack[-1]] < temperatures[j]:
                x =  mystack.pop()
                mylist[x] = j - x

            mystack.append(j)
            j += 1


        return mylist





                 

                


        