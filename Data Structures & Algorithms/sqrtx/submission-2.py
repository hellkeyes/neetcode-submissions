class Solution:
    def mySqrt(self, x: int) -> int:
        guess = x // 2  
        prev = guess  

        if x == 1 or x == 0:
            return x

        if x == (guess*guess):
            return guess
        
        final_ans  = self.newton_formula(guess, x, prev)
        return final_ans
        
    def newton_formula(self, guess: float, x: int, prev: int) -> int: 
        next_guess = (guess + (x / guess)) / 2
        ans = min(prev, int(next_guess))

        if ans == prev:
            return ans
        else:
            prev = ans
            return self.newton_formula(next_guess, x, prev)    



                                         