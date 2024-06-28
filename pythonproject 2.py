# creating variable to store the 
s = input("Enter a string: ")
# splitting the data into separate lines
# using the split() function
words = s.split()
#print(words)
# adding the length of words
word_count = len(words)
#printing the total number of words
print("the number of words in the string: ", word_count)