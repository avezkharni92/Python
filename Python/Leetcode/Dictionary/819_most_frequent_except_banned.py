'''Given a string paragraph and a string array of the banned words banned, 
return the most frequent word that is not banned. It is guaranteed there is at 
least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.
Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
'''
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
def mostCommonWord(paragraph, banned):
    words = re.findall(r'\b\w+\b', paragraph.lower())
    new_dict = {}
    for i in words:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1
    sorted_words = sorted(new_dict.keys(), key=lambda hello: (-new_dict[hello], hello))
    for banned_word in banned:
        if banned_word in sorted_words:
            sorted_words.remove(banned_word)
    return sorted_words[0]

print(mostCommonWord(paragraph, "hit"))
