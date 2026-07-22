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


# 2. Binary search

def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test
balances = [500, 1200, 2500, 3200, 4500, 6000]
print('Binary search index:', binary_search(balances, 3200))