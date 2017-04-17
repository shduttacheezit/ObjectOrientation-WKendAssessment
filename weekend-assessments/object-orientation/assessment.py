"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Object orientation is advantageous in that you can re-use your code 
and keep it closer together. The three benefits of it are: 

Encapsulation - The data is kept closer to its functionality. 

Abstraction - You do not need to know the specifics of the methods, 
and can abstract the code into classes so it can be reused. 

Polymorphism - This means you can reuse the components of code while creating 
different types, without having to make conditionals.
   

2. What is a class?

"Everything" is a class but some examples are lists, tuples, files, and strings. 
A class is a type of thing - something that has attributes, objects, and methods. 
It has more structure and less flexibility than dictionaries, and more "smarts". 
Classes still allow you to store data like a dictionary, 
but allow you to use one generic code for multiple instances 
when there is closely related data, or code. 

3. What is an instance attribute?

An instance attribute is a variable assigned to an instance (object!) of a class.
You can find usually find the attribute set directly on the object rather than
the entire class. 

4. What is a method?

It is like a function, but methods are defined specifically for and within a class. 
A method must always begin with 'self' as a default argument. 
It can refer to other attributes and can call on other methods. 

5. What is an instance in object orientation?

An instance in object orientation is basically equivalent to an 'object'. 
It is an individual occurence of a class, for example a specific string. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is different than an instance attribute, 
as a class attribute is found on the class itself. 
If you change the class attribute on the class, 
it will change it for only that specific object. 
I would use a class attribute when I think I will not be changing the attribute for each class. 
I would use an instance attribute when I would most likely change the attribute for each object. 

"""


# Parts 2 through 5:
# Create your classes and class methods

## PART 2 

class Student(Object): 
    def __init__(self, first, last, address): 
        self.first = firstname
        self.last = lastname
        self.address = address
    def __repr__(self):
        return "{'first_name': %s, \n 'last_name': %s, \n'address': %s}" % (self.first, self.last, self.address)

class Question(Object):
    def __init__(self, question, correct_answer):
        self.question = question 
        self.correct_answer = answer 
    def __repr__(self):
        return "{'question': %s, \n 'correct_answer': %s}" % (self.question, self.correct_answer)

class Exam(Object): 

    def __init__(self, name, questions): 
        self.name = name
        self.questions = []

    def __repr__(self): 
        return "'name': %s, \n 'questions': [%s]}" & (self.name, self.questions)











