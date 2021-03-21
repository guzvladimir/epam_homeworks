import pytest
from task01.oop_1 import Homework, Student, Teacher


def test_student_init():
    student = Student("Roman", "Petrov")

    assert student.first_name == "Petrov"


def test_teacher_init():
    teacher = Teacher("Daniil", "Shadrin")

    assert teacher.last_name == "Daniil"


def test_homework_init():
    homework = Homework("Learn functions", 0)

    assert homework.text == "Learn functions"


@pytest.mark.parametrize(
    ["homework_text", "deadline", "expected_result"],
    [("Learn Python", 0, False), ("Create 2 simple classes", 5, True)],
)
def test_homework_activity(homework_text: str, deadline: int, expected_result: bool):
    homework = Homework(homework_text, deadline)
    assert homework.is_active() == expected_result


def test_student_do_homework(capsys):
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    expired_homework = teacher.create_homework("Learning is the eye of the mind", 0)

    oop_hw = student.do_homework(expired_homework)
    out, err = capsys.readouterr()

    assert oop_hw is None
    assert out == "You are late\n"
