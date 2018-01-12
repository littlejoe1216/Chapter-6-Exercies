#Exercise 3:
#Encapsulate this code in a function named count, and generalize it so that it accepts the string 
#and the letter as arguments.

def count():
    word = 'racecar'

    index = len(word) - 1

    rvsword = ''

    while index >= 0:
        prin = word[index]
        index = index - 1
        rvsword = rvsword + prin

    print(rvsword)

count()
