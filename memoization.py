class Solution:
    def fib_memo(self, n, memo={}):
        # check if the result is already present or not
        if n in memo:
            return memo[n]
        
        # the basic rules
        if n <= 1:
            return n
        # performing recurssion operation
        memo[n] = self.fib_memo(n - 1, memo) + self.fib_memo(n - 2, memo)
        return memo[n]
    
number = 3
obj = Solution()
print(obj.fib_memo(number))


# def fib_memo(self, n, memo={}):

"""In Python, default arguments are evaluated only once when the function is defined, not every time you call the function.

The Problem: The dictionary memo is shared across all calls to this function. If you call obj.fib_memo(50) and then later call obj.fib_memo(5) in the same program run, the second call will use the leftover cache from the first call.

Why it matters: While it doesn't break the math for Fibonacci (since fib(5) is always 5), this is considered a bad practice in interviews. If the problem were different (e.g., finding paths in a grid that changes), reusing the old cache would give you the wrong answer."""


class Solution:
    def fib_memo(self, n, memo=None):
        # initialize the dictionay strictly if it's the first call
        if memo is None:
            memo = {}

        # 1. Check cache
        if n in memo:
            return memo[n]
        
        # 2. Base cases
        if n <= 1:
            return n
        # 3. Recurse & store
        memo[n] = self.fib_memo(n - 1, memo) + self.fib_memo(n - 2, memo)

        return memo[n]
    
number = 50
obj = Solution()
print(obj.fib_memo(number))
            