# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
# If there exists a solution, it is guaranteed to be unique.

 

# Example 1:

# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.


class Solution:
    def Gas_Station(self, gas, cost):
         # If total gas is less than total cost, return -1 (not possible to travel)
        total_gas, total_cost = sum(gas), sum(cost)
        if total_gas < total_cost:
            return -1
        start = 0 # Possible starting index
        tank = 0  # Current fuel in tank
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # If tank becomes negative, reset the start index to i+1
            if tank < 0:
                start = i + 1
                tank = 0 # Reset tank
        return start
Gas = [1, 2, 3, 4, 5]
Cost = [3, 4, 5, 1, 2]
solution_instance = Solution()
print(solution_instance.Gas_Station(Gas, Cost))