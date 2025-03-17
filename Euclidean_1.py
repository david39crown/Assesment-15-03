#Question no:1
'''Question 1: Calculate Euclidean distance
Write a Python program to calculate Euclidean Distance.
Example 1:
Input:
Given First point values P(x1, y1) : 6 , 7
Given second point values Q(x2, y2) : 5, 4
Output:
The Euclidean Distance between the above given two points 'PQ' = 3.1622776601683795'''

#answer

import math


def euclidean_dist(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

x1, y1 = 6, 7
x2, y2 = 5, 4

distance = euclidean_dist(x1, y1, x2, y2)
print(f"The Euclidean Distance between the above given two points 'PQ' = {distance}")
