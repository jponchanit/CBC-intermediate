# Your code here
class Person():
    def __init__(self, name):
        self.name = name 
        
class Teacher(Person):
    def __init__(self, name, name_t):
        super().def __init__(self, name):
            self.name = name
            self.name_t = name_t
    def teacher(self):
        
        
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
