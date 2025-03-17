#Question no:2
'''Strange Sort: Alternating Smallest and Largest
In an amusement park ticket queue, visitors are sorted in a strange manner. The smallest
number (representing the youngest visitor) stands first, followed by the oldest visitor. The next
youngest visitor stands next, followed by the next oldest visitor, and so on. Write a Python
program to sort a list of numbers in such a “strange sort,” where the first element is the
smallest, the second is the largest, the third is the next smallest, and so on.
'''


def strange_sort(arr):
    arr.sort()  
    result = []
    
    left, right = 0, len(arr) - 1
    while left <= right:
        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[left])  
            result.append(arr[right]) 
        left += 1
        right -= 1

    return result

# Example input
nums = [1, 3, 4, 5, 11]

# Sorting in strange order
print(strange_sort(nums)) 
