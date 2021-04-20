
def duplicate(l):

    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    print(l1)
    
def unique(l):
    l1=[]
    for i in l:
        if l.count(i)==1:
            l1.append(i)
    print(l1)
   


class MyMath():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
        