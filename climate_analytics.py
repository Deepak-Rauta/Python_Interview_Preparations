"We have a list of numbers representing daily temperatures. I want you to write a loop that calculates the average temperature. However, if you encounter a 'null' value or a temperature above 100°C (which is an equipment error), skip that specific value. If you encounter a temperature of exactly -99°C, that's a 'shutdown' signal—stop the loop entirely and return the average calculated up to that point."

class Solution:
    def calculate_average_temp(self, temps):
        total_sum = 0
        valid_count = 0

        for temp in temps:
            # shutdown signal
            if temp == -99:
                break

            # skip invalid data (null or error)
            if temp is None or temp > 100:
                continue

            # process valid data
            total_sum += temp
            valid_count += 1
        
        # Calculate avrage (handle empty case)
        if valid_count == 0:
            return 0

        return total_sum / valid_count

daily_temp = [20, 25, None, 105, 30, -99, 15] 
obj = Solution()
print(obj.calculate_average_temp(daily_temp))