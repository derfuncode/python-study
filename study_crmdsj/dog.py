class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        print(self.name.title()+" rolled over!")


my_dog = Dog('willie',6)
print("my dog's name is "+my_dog.name.title()+".")
print("my dog is "+str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

