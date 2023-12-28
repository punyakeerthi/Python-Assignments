'''
Created on Dec 20, 2023

@author: PBL
''' 
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0 and a<b :
        return min(a,b)
    else : 
        return max(a,b)
    
print(lesser_of_two_evens(4, 4))

def animal_crackers(text):
    sts=text.split() 
    if sts[0][0]==sts[1][0]:
        return True
    else :
        return False
    
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


def makes_twenty(n1,n2):
    if n1==20 or n2==20 :
        return True
    elif n1+n2==20:
        return True
    else :
        return False
    
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
    
print(old_macdonald('macdonald'))  


def master_yoda(text):
    return ' '.join(text.split()[::-1])

print(master_yoda('I am home'))