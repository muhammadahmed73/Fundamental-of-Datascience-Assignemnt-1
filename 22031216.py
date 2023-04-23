# Question No.1: Reading Data and Storing it in an array
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("D:\Hertfordshire\Fundamental of DS/data6.csv", delimiter=',')

# Question No 2: Creating another array
# Define a function to calculate the mode(s) of a list of values
def mode_calc(values):
    # Create a dictionary to store the frequency of each value
    frequency = {}
    for num in values:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find the mode(s)
    mode = []
    max_frequency = max(frequency.values())
    for num, freq in frequency.items():
        if freq == max_frequency:
            mode.append(num)
    return mode

# Define a function to calculate the standard deviation of a list of values
def std_calc(values):
    # Calculate the mean of the values
    mean = sum(values) / len(values)

    # Calculate the variance of the values
    variance = sum((x - mean)**2 for x in values) / len(values)

    # Calculate the standard deviation of the values
    std = variance ** 0.5
    return std

# Define a function to calculate the median of a list of values
def median_calc(values):
    # Sort the values in ascending order
    sorted_values = sorted(values)

    # Calculate the median of the sorted values
    mid = len(sorted_values) // 2
    median = (sorted_values[mid] + sorted_values[~mid]) / 2 if len(sorted_values) % 2 == 0 else sorted_values[mid]
    return median


# creates another array, representing the distribution of newborn weights in a given dataset;
array = data
array_size = len(array)
mean = sum(array)/array_size
#median = (array[array_size//2 - 1] + array[array_size//2]) / 2 if len %2 == 0 else array[array_size//2]
median = median_calc(array)
mode = mode_calc(array)
std = std_calc(array)
min_array = min(array)
max_array = max(array)

out = f"Mean:{mean} \n Mode:{mode} \n Median:{median} \n STD:{std} \n Min Value:{min_array} \n Max Value:{max_array}"
print(out)



# Question No. 3: Plotting the Distribution
bins=10
plt.hist(array, bins=bins, color='skyblue', edgecolor='black')
plt.xlabel("Weights")
plt.ylabel("Frequency")
plt.title("Distribution of Newborn Weights")
plt.show()



# Question 4: Calculating Average Weight of Babies (W)
#Average weight of babies
mean = sum(array)/len(array)

print(f"According to distribution the average weight of babies is:{mean}")


# Question No. 5: Calculating Value of X
# Sort the array in ascending order
array = sorted(array)

# Calculate the index for the 10th percentile of the sorted array
index_10 = int(0.1 * len(array))

# Get the weight value at the 10th percentile of the data (X)
X = array[index_10]

# Print the value of X
print(f"Value of X: {X}")


# Question No. 6: Plotting X and W on graph
# using the array data, set the histogram to be normalized (density=True)
# set the opacity of the histogram to 0.5 and add a label 'Newborn Weights' to the histogram
# set the color of the histogram to skyblue and its edge color to black
plt.hist(array, bins=10, density=True, alpha=0.5, label='Newborn Weights', color='skyblue', edgecolor='black')

# Add a vertical line on the plot indicating the mean of the array (W~)
# set the color of the line to green, its style to dashed, its width to 2, and add a label 'Average Weight (W~)'
plt.axvline(x=mean, color='green', linestyle='--', linewidth=2, label='Average Weight (W~)')

# Add a vertical line on the plot indicating the value of X (10th percentile of the data)
# set the color of the line to red, its style to dashed, its width to 2, and add a label 'X(10th Percentile)'
plt.axvline(x=X, color='red', linestyle='--', linewidth=2, label='X(10th Percentile)')

# Set the label for the x-axis to 'Newborn Weight' and the label for the y-axis to 'Frequency'
# Set the title of the plot to 'Distribution of Newborn Weights'
plt.xlabel('Newborn Weight')
plt.ylabel('Frequency')
plt.title("Distribution of Newborn Weights")
plt.legend()

# Show the plot
plt.show()
