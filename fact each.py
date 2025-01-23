class Solution:
    def cal_fact(self, n):
        if n == 0 or n== 1:
            return 1
        else:
            return n * self.cal_fact (n-1)
        
    def cal_fact2(self,numbers):
        factorials = []
        for num in numbers :
            factorials.append(self.cal_fact(num))  
        return factorials  

#Example usages:
number_to_calculate = [5,4,3,2,1]

solution_instance = Solution()
result = solution_instance.cal_fact2(number_to_calculate)
print(f'The original number is: {number_to_calculate}')
print(f'The factorial of number is: {result}')
    