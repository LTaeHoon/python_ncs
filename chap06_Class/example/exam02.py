'''
Created on 2016. 12. 2.

@author: acorn
'''

class Person:
    name =None
    gender = None
    age =0
    
    def __init__(self,name,gender,age):
        self.name = name
        self.gender= gender
        self.age = age
    
    def display(self):
        if(self.gender =='male'):
            self.gender = '남자'
        else :
            self.gender ='여자'
        print('이름 : %s, 성별 : %s\n나이: %d'%(self.name,self.gender,self.age))


name = input('이름 :')        
age = int(input('나이 :'))        
gender = input('성별(male/female) :')        
    
per = Person(name,gender,age) 
per.display() 