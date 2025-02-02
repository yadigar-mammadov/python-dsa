[🔙 Go back to main list](../../../README.md)

## Problem 

Given an array consists of strings, the <abbr title="The words consisted of the rearrangement the same letters using each original one exactly once.">anagrams</abbr> should be group together. 
You can return the answer in any order.

### [Go to solution](../group_anagrams.py)

## Example
### Input: strs = ["car", "arc", "eat", "bold", "tea"]
### Output: [["car", "arc"], ["eat", "tea"], ["bold"]]


## Explanation

Each array holds the words that consist of the same original letters. 

Both **car** and **arc** have the same letters of **a**, **r** and **c**. 
The same logic applies to other groups. The last word **bold** has no anagram. 

Any other order of the words and arrays accepted as long as they are grouped into the same array.

## Notes
- Assume that strings array contains at least one string.
- All letters are lowercase.

## Solutions
### Group by sorting

In the example input, if we sort each word, we will get list as ["acr", "acr", "aet", "bdlo", "aet"]. As you can observe, all anagrams form the same sorted form as they are formed of the same letters with the same amount.
  
We can use additional dictionary **{str: list}** or **{tuple: list}** to group anagrams into the convenient arrays and return the values at the end. 

We use sorted version of each string as key (because sorted versions of the anagrams will be the same) and original values as a value to append to relevant list.

**Time complexity**: Let N be the number of strings, and M be the average length of each string. Sorting each string takes (M * logM). We apply sorting to all elements and get the total complexity of O(N * M * log M)

**Space complexity**: The hash map (dictionary) stores each string exactly once in the result lists, and each sorted string (or tuple) as a key.Storing the sorted version of each string requires up to 𝑂(𝑀) space, so for N strings, the keys collectively take the maximum of 
𝑂(𝑁 * 𝑀). The lists in the dictionary stores the original N strings consisting of average M characters. So the total space complexity is O(N * M)



### Group using array

In this method, we create an array of length 26 (each value represents the letter in english alphabet) and measure the number of occurrence of each different letters. For example, both the strings **aba** and **aab** have 2 a and 1 b. So, they are considered anagrams. The logic is the same with the first method. We just use tuple as a key (convertion to tuple is necessary since dictionary key must be hashable which means immutable).

**Time complexity**: It takes the same time complexity since counting frequencies of each string to loop each string takes average length of M and conversion to tuple is constant time operation O(1), because the lenght of the list is fixed (26). For N strings, final complexity becomes O(N * M).

**Space complexity**: The total space is O(N×M), as you must account for all the characters stored in the original strings.

### Group using dict

The same logic applies with the second method. Instead of using array, dictionary is used to achieve the same result. At the end, conversion to frozenset is needed to make dictionary hashable. 

Time and space complexity are calculated with the same logic of the second method.