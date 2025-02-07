# Jump Game II - Minimum Number of Jumps

Problem Overview
This repository contains solutions for the "Jump Game II" problem, where the task is to find the minimum number of jumps required to reach the last index of an array.

## Problem Statement

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0]. Each element nums[i] represents the maximum length of a forward jump from index i.

The goal is to return the minimum number of jumps required to reach nums[n-1].


## Example
Example 1:

vbnet
Copy
Edit
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

makefile
Copy
Edit
Input: nums = [2,3,0,1,4]
Output: 2



# Approach
We use a greedy algorithm to solve this problem efficiently. The goal is to always try to jump to the farthest index we can reach from the current position and keep track of the minimum number of jumps. We iterate through the array, and at each step, we update the farthest point we can reach. When we reach the end of the current jump, we increment the jump counter.

## Time Complexity
The solution runs in O(n) time, where n is the length of the array nums.
