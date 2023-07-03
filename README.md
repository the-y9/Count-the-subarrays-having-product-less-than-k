# Count-the-subarrays-having-product-less-than-k
## Slider window approach
The sliding window approach is a common algorithmic technique used for dealing with subarray or substring problems. It involves creating a window of fixed size and sliding it over the array or string to find the solution to the problem.

In this approach, we maintain two pointers: left and right, which represent the left and right endpoints of the window. We initialize them to the start of the array or string. We then slide the window to the right by incrementing right and updating the solution accordingly. If the solution is not yet found, we slide the window to the right again by incrementing left and updating the solution.

The sliding window approach is particularly useful for solving problems that involve finding a subarray or substring that satisfies a certain condition (e.g. maximum sum, minimum length, etc.). By maintaining a fixed-size window, we can avoid redundant computations and solve the problem in linear time complexity.

The algorithm used in the question, i.e., to find the number of possible contiguous subarrays having product less than a given number k, uses the sliding window approach.

## Here's how it works:

- We initialize count to 0, prod to 1, and left to 0.
- We iterate through the array using a sliding window approach, where right is the right endpoint of the window.
- At each iteration, we multiply prod by a[right].
- If prod is greater than or equal to k, we divide prod by a[left] and increment left until prod is less than k.
- We add the number of subarrays that end at right to count, which is equal to right - left + 1.
- We return the final value of count.
