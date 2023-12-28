'''
Created on Dec 19, 2023

@author: PBL
'''


print("I am new")

a = 120

b = 20

c = 10

if a > b and a > c :
    print(f'{a} is greater')
elif b > c :
    print(f'{b} is greater')
else :
    print(f'{c} is greater')
    
    
list1=[1,2,3,4,5,6,7,8,9,10]
e_count=0
o_count=0
for i in list1 :
    if i % 2 == 0 :
        e_count=e_count+1
    else : 
        o_count=o_count+1
print(f'even number count :{e_count}')
print(f'odd number count :{o_count}')


str='*'

for i in range(0,5) :
    for j in range(i) :
        print(str,end=" ")
    print()
    
 
strname= 'punyakeerthi'
for ch in strname :
    print(ch)
    
print('l' in ['x','y','z'])

print ('mykey' in {'mykey','value'})

mylist=[10,20,30,40,50]
 
from random import shuffle
mylist2=[1,2,3,4,5,6,7,8]
print(mylist2)
shuffle(mylist2)
print(mylist2)

from random import randint
mylistdata=[i for i in range(0,10)]
print(f'mylist data : {mylistdata}')
print(randint(0,100))


result=input("what is your wife name ?")
print(f"Hello, {result}")







