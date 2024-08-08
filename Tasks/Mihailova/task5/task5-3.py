#3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.
def long_words(words):
     return [word for word in words if len(word) > 5]
strings = ["one", "five", "twelve"]
long_word = long_words(strings)
print(long_word) 