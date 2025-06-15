# Your code here
class Person():
    def __init__(self, name):
        self.name = name 
    def greet(self):
        print (f'Hello, My name is {self.name}.')
        
        
class Teacher(Person):
    def __init__(self, name_t):
        super(). __init__(name_t)
        self.name = name_t
    def teach(self):
        print (f'Im Teacher teaching class')    
        
# Example:
p = Person("Alice")
t = Teacher("Bob")
p.greet()
t.greet()
t.teach()

# Expected Output:
# Hello, my name is Alice.
# Hello, my name is Bob.
# I'm teaching a class.
