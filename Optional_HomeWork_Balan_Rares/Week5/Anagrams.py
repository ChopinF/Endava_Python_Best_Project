word1 = "listen"
word2 = "silent"
dict1 = {}
dict2 = {}
for letter in word1:
    if letter in dict1:
        dict1[letter]+=1
    else:
        dict1[letter] = 1
print(dict1)
for letter in word2:
    if letter in dict2:
        dict2[letter]+=1
    else:
        dict2[letter] = 1
print(dict2)
if dict1 == dict2:
    print("Words are anagrams")
else:
    print("Words are not anagrams")
dict1.pop('i')
print(dict1)
print(dict2)