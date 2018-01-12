#Exercise 5: 
#Take the following Python code that stores a string:`
#str = 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after the colon character and then use the 
#float function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475'
num = str.find(" ")
print(num)

date = str[num+1:]

new_date = float(date)

print (date), type(date)
print (new_date), type(new_date)
