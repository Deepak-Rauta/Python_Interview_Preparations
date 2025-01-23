# def roated_left(arr, d):
#     n = len(arr)
#     #d = d % n #is wrapped around within the valid index renge This result will always be a value between 0 and n-1
#     # for circular and cyclic opearation we generally use this
#     roated_array = arr[d:] + arr[:d]
#     return roated_array
# arr = [1,2,3,4,5,6,7,8,9]
# d = 2
# roated_array = roated_left(arr, d)
# print('original array', arr)
# print('Roated array', roated_array)






# class Solution:
#     #Function to rotate an array by d elements in counter-clockwise direction. 
#     def rotateArr(self,A,D,N):
#         self.N = N
#         D = D % N
#         roated_arr = A[D:] + A[:D]
#         return roated_arr
        
# #Example usages
# solution_instance = Solution()
# A = [1,2,3,4,5]
# D = 2
# N = len(A)
# roated_array = solution_instance.rotateArr(A,D,N)
# print(f'The original array is:{A}')
# print(f'The roated array is:{roated_array}')
















