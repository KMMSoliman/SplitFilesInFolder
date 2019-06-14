class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def MyFun(self):
        return self
        #print("My name is: " + self.name)
    x = 5

p1 = MyClass("Mido", 50)
tt = p1.MyFun()
print(tt)
#print (p1.name)