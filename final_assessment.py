import random
"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""


class CFGStudent:

    def __init__(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = self.generate_id()

    @staticmethod
    def generate_id():
        'your code goes here'
        'create a random new id, which is any number between 1,000 and 10,000'
        'return id as a string'
        "Example '8754' "
        # we will use uuid as creates a random uuid and maintain privacy
        x = random.randrange(1000,10000)
        return str(x)



    def get_id(self):
        return self.student_id


    def get_fullname(self):
        return self.name + " " + self.surname


class NanoStudent(CFGStudent):

    def __init__(self, specialization, name, surname, age, email):
        super().__init__(name, surname, age, email)
        self.specialization = specialization
        self.course_grades = {}
    @staticmethod
    def generate_id():
        child_id= CFGStudent.generate_id
        return "NANO"+ str(child_id)

    def add_new_grade(self, task, grade):
        self.course_grades[task] = grade
        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"

    def get_course_grades(self):
        for i, j in self.course_grades.items():
            print(f"{i}: {j} ")


############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', 'Mia', 'Papandopulu', 20, 'mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""

def even_fibonacci_sum(limit):
    num1 = 0
    num2 = 1
    fib_even_num_sequence = num1
    if limit <= 0:
        return "invalid limid, we need a bigger number and not negative"
    elif limit==1:
        return 0
    x=0
    while x < limit:
        # check if num is even I will add it to the fib sequence
        if (num1 % 2) == 0:
            #fib= num1+num2
            fib_even_num_sequence +=num1
        fib= num1+num2
        num1=num2
        num2=fib
        x += 1
    return fib_even_num_sequence




##### TESTS ####

print(even_fibonacci_sum(10))  # should be 44
print(even_fibonacci_sum(15))  # should be 188
print(even_fibonacci_sum(1))   # should be 0





"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""

def is_valid_subsequence(array, sequence):
    for x in sequence:
        for y in array:
            #index_x = x.index(x)
            index_x = x(index_x)
            #index_y = y.index(y)
            index_y = y(index_y)
            if index_y == index_x:
                return True

    return False


#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

#print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

#print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
    TASK 4

To improve the code I would suggest to create another class to keep employee class have responsabilities sepratate from the department. 
The use a subclass is useful in this case as well and they are missing.
We get the id in a way that is not safe.
"""





