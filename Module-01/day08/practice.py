# day08/practice.py

# 1. Recursive sum and countdown

def total(nums):
    if not nums:
        return 0
    return nums[0] + total(nums[1:])


def count_down(n):
    if n <= 0:
        return
    print(n)
    count_down(n - 1)


# Test
numbers = [10, 20, 30, 40]
print('Total:', total(numbers))

print('Countdown:')
count_down(5)