def AnagramFinder(str1,str2):
   str1 = str1.replace(" ", "").lower()
   str2 = str2.replace(" ", "").lower()
# This line remove the space from each input string using the replace method and convert them into the lower case    
   return sorted(str1)==sorted(str2)
# sorted function returns a sorted list of character
word1 = 'listen'
word2 = 'silent'
if AnagramFinder(word1, word2):
   print(f'{word1} and {word2} are anagrams')
else:
   print(f'{word1} and {word2} are not anagrams')   