"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are 
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without - 
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes 
you want.
"""

import datetime

class DeadlineError(Exception):
    pass

class Homework:
    
    def __init__(self, hw_text, deadline):
        self.hw_text = hw_text
        self.deadline = deadline

    def is_active(self):
        return datetime.datetime.now() < self.deadline

class HomeworkResult:
    
    def __init__(self, author, homework, solution):
        self.author = author
        self.homework = homework
        self.solution = solution

    def __str__(self):
        return f"{self.solution}"
    
    def __len__(self):
        return len(self.solution)

class Student:
    
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError("You are late")

class Teacher:
    
    homework_done = {}
    
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    @classmethod
    def create_homework(cls, text, days):
        deadline = datetime.datetime.now() + datetime.timedelta(days = days)
        homework = Homework(text, deadline)
        if homework not in cls.homework_done:
                cls.homework_done[homework] = []
        return homework

    @classmethod
    def check_homework(cls, homework_result):
        if len(homework_result.solution) > 5:
            if homework_result.homework not in cls.homework_done:
                cls.homework_done[homework_result.homework] = []
            if homework_result not in cls.homework_done[homework_result.homework]:
                cls.homework_done[homework_result.homework].append(homework_result)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework=None):
        if homework is not None:
            cls.homework_done[homework] = []
        else:
            cls.homework_done = {}
