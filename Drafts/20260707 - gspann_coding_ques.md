"""
Question: Longest Substring Without Repeating Characters
Given a string s, return the length of the longest substring without repeating characters.
Example:
s = "abcabcbb"
# output: 3  # "abc"
"""

"""

ALGO:

1: Iteration over characters of the input string
2: Keep a dict char_dict = { "<char>": <count == 1 (in my case)> }
3: As I do the iteration: I would store characters read so far in a var out_str till I find a character that is alread present in char_dict




"""