class Student:
    """Объкты класса Student, описываются именем, фамилией, возрастом и набором навыков.
    Атрибут зачисления на курс (is_learning) = True при создании объекта.
    В атрибуте self.skills по умолчанию находится значение "English". """

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.skills = ['English']
        self.is_learning = True

    def learning(self):
        """Метод обучения: в атрибут self.skills добавляются значения SQL, Linux и Python)"""

        subjects = ['SQL', 'Linux', 'Python']
        for sub in subjects:
            self.skills.append(sub)

    def accept(self):
        """Метод прием на работу: если студент обладает всеми необходимыми навыками
        возвращает "успешное сообщение", иначе - "неуспешное"."""

        skills_need = ['English', 'SQL', 'Linux', 'Python']
        if self.skills == skills_need:
            return f"{self.name}, you're accepted! Good job!"
        else:
            return f"{self.name}, sorry, you're denied! Try next time."

students = []

Alice = Student('Alice', 'Arrow', 21)
Bob = Student('Bob', 'Brown', 23)
Cean = Student('Cean', 'Crown', 19)
students.extend([Alice, Bob, Cean])

for student in students:
    student.learning()
Cean.skills.remove('Python')

for student in students:
    print(student.accept())

