# Prompt the user to enter a sentence and then print the sentence in uppercase letters.
#print (input("Please enter a sentece: ").upper())

# Prompt the user to enter a paragraph and then count the number of words in the paragraph.
paragraph = input("Please enter a paragraph: ")
print (f"{paragraph} has {len(paragraph.split())} words.")

# Prompt the user for a string, and check if all the characters in the string are digits. Output true or false
paragraph = input("Please enter a string: ")
print (paragraph.isdigit())

# Prompt the user for a string, and replace all occurrences of the letter "a" with the letter "o".
paragraph = input("Please enter a string: ")
print (paragraph.replace("a", "o"))

# Prompt the user to enter their full name and then print their initials. Assume that the user will enter their full name with a space between each name.
words = input("Please enter your full name: ").capitalize().split()
i = 0
initials = ""
while i<len(words):
    initials = initials + words[i][0]
    i+=1
print (f"Your initials are {initials.upper()}")



# Prompt the user for a string, then print its length.
