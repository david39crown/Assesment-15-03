#Question no:3
'''Finding indices of Closest Temperatures
Imagine you work for a weather station, and you have a list of temperatures recorded
throughout the day. Your job is to find which two temperatures in the list are the most similar
(closest in value). Once you find the two closest temperatures, you need to tell their positions
(indices) in the list.
'''




def closest_temperatures(temps):
    min_diff = float('inf')
    indices = [-1, -1]

    
    for i in range(len(temps)):
        for j in range(i + 1, len(temps)):
            diff = abs(temps[i] - temps[j])
            if diff < min_diff:
                min_diff = diff
                indices = [i, j]

    return indices

# Example inputs
temps1 = [1, 7, 9, 2, 10]
temps2 = [5, 8, 12, 15, 7]


print(closest_temperatures(temps1))  
print(closest_temperatures(temps2))  
