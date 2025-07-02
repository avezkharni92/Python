'''692. Top K Frequent Words
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.
Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, 
with the number of occurrence being 4, 3, 2 and 1 respectively.
'''

words = ["i","love","leetcode","i","love","coding"]

def k_most_frequent_words(words, k):
    new_dict = {}
    for i in words:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] +=1
    print(new_dict)
    #sorted_words = sorted(new_dict.keys(), key=lambda word: (-new_dict[word], word))
# here we use lambda as dummy function, -new_dict[word] tells that sorting should be done in descending(-ve), 
# then word is given to if 2 keys have same value then use word in alphabetical order
    sorted_words = sorted(new_dict.keys(), key=lambda hello: (-new_dict[hello], hello))
    return sorted_words[:k]

print(k_most_frequent_words(words, 2))