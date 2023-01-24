## Problem
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

## Code Complexity

The time complexity of this the code is O(S), where S is the sum of the characters of all strings in the input list.
The outer loop iterates through the characters of the prefix, and since the prefix can have at most n characters (n is the length of the shortest string in the input list), the outer loop has a time complexity of O(n).
The inner zip() function iterates through all characters of all strings in the input list, so it has a time complexity of O(S), where S is the sum of the characters of all strings in the input list.
Therefore, the overall time complexity of the code is O(n + S).
As for space complexity, it is O(1) as the function only uses a prefix variable to store the result and it doesn't use any additional data structure