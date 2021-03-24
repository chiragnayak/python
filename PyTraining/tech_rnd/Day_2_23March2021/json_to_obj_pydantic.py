from pydantic import BaseModel
from typing import List, Optional

print('-' * 75)

json_text = '''{
  "first_name": "John",
  "last_name": "Smith",
  "age": 25,
  "scores": [
    {
      "course": {
        "name": "Algebra",
        "teacher": "Mr. Schmidt"
      },
      "ind_score": 100
    },
    {
      "course": {
        "name": "Statistics",
        "teacher": "Mrs. Lee"
      },
      "ind_score": 90
    }
  ]
}'''

# Course
class Course(BaseModel):
    name: str
    teacher: str

# Scores
class Score(BaseModel):
    course: Course
    ind_score: int

# Student
class Student(BaseModel):
    first_name: str
    last_name: str
    age: int
    scores: List[Score]

    def __str__(self):
        return f"Details of {self.first_name} {self.last_name}"

obj = Student.parse_raw(json_text)
print('First Name -', obj.first_name)
print('Last Name -', obj.last_name)

print('-' * 75)

print(obj.dict())

print('-' * 75)
