'''
Created on Dec 19, 2023

@author: PBL
'''

#Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

splitst=st.split()
print(splitst)

for word in splitst :
    if word[0]=='s':
        print(word)


#Use range() to print all the even numbers from 0 to 10.

for i in range(0,10):
    if(i%2==0) :
        print(i)     
        
        
#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

mylistdata=[i for i in range(0,50) if i%3==0]
print(mylistdata)

#Go through the string below and if the length of a word is even print "even!"
print('Go through the string below and if the length of a word is even print "even!"')


st = 'Print every word in this sentence that has an even number of letters'

splitst=st.split()
print(splitst)

for word in splitst :
    if len(word)%2==0:
        print(word)
        
print('Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".')

for i in range(1,100):
    if(i%3==0 and i%5==0) :
        print("FizzBuzz")
    elif(i%5==0) :
        print("Buzz")
    elif(i%3==0) :
        print("Fizz")
print('Use a List Comprehension to create a list of the first letters of every word in the string below:')

list1=[word[0] for word in st.split()]
print(list1)