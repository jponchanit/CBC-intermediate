# Your code here
class Person():
    def __init__(self, name):
        self.name = name 
        
class Teacher(Person):
    def teach(self) :
        print(f"")
        
# Example:
# p = Person("Alice")
# t = Teacher("Bob")
# p.greet()
# t.greet()
# t.teach()

# Expected Output:
# Hello, my name is Alice.
# Hello, my name is Bob.
# I'm teaching a class.
