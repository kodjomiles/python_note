class myclass:
    num = 5
firstTrail = myclass()
print(firstTrail.num)

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
   
person1 =person("Kodjo",28)
print(person1.name,"I am",person1.age)        
        
class mYp:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
        
    def myfuncOUTPUT(self):
        print(self.fname,self.lname,"is my name and i am",self.age)
p1 = mYp("Kodjo","Miles",28)
p1.myfuncOUTPUT()                   