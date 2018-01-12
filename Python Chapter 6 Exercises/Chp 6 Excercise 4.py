#Exercise 4:
#There is a string method called count that is similar to the function in the previous exercise. 
#Read the documentation of this method at https://docs.python.org/3.5/library/stdtypes.html#string-methods 
#and write an invocation that counts the number of times the letter a occurs in "banana".

word = "banana"
let = input("Enter a letter in the word banana.")

def counter():
  count = 0
  for letter in word:
    if letter == let: 
      count = count + 1
  return count
  
print (counter())
print ("is the number of times this letter is in the word banana.")

