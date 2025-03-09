class Solution:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        # Divide: Find the middle
        mid = len(arr) // 2
        left_half = self.merge_sort(arr[mid:])
        right_half = self.merge_sort(arr[:mid])

        # conqure: merge the sorted halves
        return self.merge(left_half, right_half)
    
    def merge(self, left, right):
        sorted_arr = []
        i = j = 0
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        # Append remaining elements
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

arr = [6, 3, 8, 5, 2, 7, 4, 1]
solution_instance = Solution()
print(solution_instance.merge_sort(arr))