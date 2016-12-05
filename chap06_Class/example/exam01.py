'''
Created on 2016. 12. 2.

@author: acorn
'''
class Rectangle:
    #멤버 변수
    width=0
    height=0
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        result = self.width * self.height
        print('사각형의 넓이 :',result)
    def circum(self):
        print('사각형의 둘레 : %d'%((self.width+self.height)*2))

w = int(input('사각형의 가로 입력:'))
h = int(input('사각형의 세로 입력:'))

rec = Rectangle(w,h) 
rec.area()
rec.circum()
