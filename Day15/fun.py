def analyze(num):
  total = sum(num)
  avg = total/len(num)
  high = max(num)
  low = min(num)
  return total, avg, high, low 

num = [10, 20, 30, 40, 50]
total, avg, high, low = analyze(num)
print("Total:", total)
print("Average:", avg)
print("High:", high)
print("Low:", low)

nums = [2, 7, 11, 15]
target = 9




def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

result = twoSum([2, 7, 11, 15], 9)
print(result)

def process_numbers(numbers):
    even = filter(lambda x: x%2==0, numbers)
    mul = map(lambda x: x*3, even)
    result = sorted (mul, reverse = True)
    print(list(result))

numbers = [5, 12, 8, 20, 15, 24, 7, 30]
process_numbers(numbers)

