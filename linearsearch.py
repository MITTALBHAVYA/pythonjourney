def linear_search(arr,target):
  for i in range(len(arr)):
     if arr[i] == target:
       return i
  return -1

numbers = [4,2,7,1,5]
target_number=7
result = linear_search(numbers,target_number)
print(f"The target number {target_number} was found at index {result}.")