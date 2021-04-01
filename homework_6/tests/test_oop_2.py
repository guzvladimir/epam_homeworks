from datetime import timedelta

import pytest

from task01.oop_2 import (  # isort: skip
    DeadlineError,
    Homework,
    HomeworkResult,
    Student,
    Teacher,
)


@pytest.fixture()
def good_student():
    return Student("Lev", "Sokolov")


@pytest.fixture()
def lazy_student():
    return Student("Roman", "Petrov")


@pytest.fixture()
def opp_teacher():
    return Teacher("Daniil", "Shadrin")


@pytest.fixture()
def advanced_python_teacher():
    return Teacher("Aleksandr", "Smetanin")


def test_student_attribute(lazy_student, good_student):

    assert lazy_student.first_name == "Roman"
    assert lazy_student.last_name == "Petrov"
    assert good_student.first_name == "Lev"
    assert good_student.last_name == "Sokolov"


def test_teacher_attribute(opp_teacher, advanced_python_teacher):

    assert opp_teacher.first_name == "Daniil"
    assert opp_teacher.last_name == "Shadrin"
    assert advanced_python_teacher.first_name == "Aleksander"
    assert advanced_python_teacher.last_name == "Smetanin"


def test_teacher_create_homework(opp_teacher):

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    assert oop_hw.text == "Learn OOP"
    assert oop_hw.deadline == timedelta(days=1)
    assert docs_hw.text == "Read docs"
    assert docs_hw.deadline == timedelta(days=5)


def test_homework_return_homeworkresult(good_student, opp_teacher):
    oop_hw = opp_teacher.create_homework("Learn OOP", 2)
    result = good_student.do_homework(oop_hw, "I have done this hw")

    assert isinstance(result, HomeworkResult)
    assert result.solution == "I have done this hw"
    assert result.homework.text == "Learn OOP"


def test_check_homework_with_length(good_student, opp_teacher):

    oop_hw = opp_teacher.create_homework("Learn OOP", 2)
    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(oop_hw, "done")

    assert opp_teacher.check_homework(result_1) == True
    assert opp_teacher.check_homework(result_2) == False


def test_raise_deadlineerror(lazy_student, advanced_python_teacher):
    docs_hw = advanced_python_teacher.create_homework("Read docs", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        lazy_student.do_homework(docs_hw, "I have done this hw too late")


def test_homework_is_not_a_homework_class_object():
    with pytest.raises(TypeError, match="You gave a not Homework object."):

        assert isinstance(
            HomeworkResult("it is not a Homework class object", "Solution").homework,
            Homework,
        )


def test_check_homework_in_homework_done(good_student, opp_teacher):
    oop_hw = opp_teacher.create_homework("Learn OOP", 2)
    result = good_student.do_homework(oop_hw, "I have done this hw")
    opp_teacher.check_homework(result)

    assert "Learn OOP" in opp_teacher.homework_done
    assert "I have done this hw" in opp_teacher.homework_done[result.homework.text]


def test_teacher_check_homework_not_in_homework_done(lazy_student, opp_teacher):
    docs_hw = opp_teacher.create_homework("Read docs", 5)
    result = lazy_student.do_homework(docs_hw, "done")
    opp_teacher.check_homework(result)

    assert "Read docs" not in opp_teacher.homework_done
    assert "done" not in opp_teacher.homework_done[result.homework.text]


def test_reset_homework_argument(good_student, opp_teacher):

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    result = good_student.do_homework(oop_hw, "I have done this hw")
    opp_teacher.check_homework(result)

    assert "I have done this hw" in opp_teacher.homework_done[oop_hw.text]
    assert "Learn OOP" in opp_teacher.homework_done
    opp_teacher.reset_results(oop_hw)
    assert "I have done this hw" not in opp_teacher.homework_done[oop_hw.text]
    assert "Learn OOP" in opp_teacher.homework_done


def test_reset_homework_full(good_student, opp_teacher):
    docs_hw = opp_teacher.create_homework("Read docs", 5)
    result = good_student.do_homework(docs_hw, "I have done this hw too")
    opp_teacher.check_homework(result)

    assert "I have done this hw too" in opp_teacher.homework_done[docs_hw.text]
    assert "Read docs" in opp_teacher.homework_done
    opp_teacher.reset_results()
    assert "Read docs" not in opp_teacher.homework_done
    assert "I have done this hw too" not in opp_teacher.homework_done[docs_hw.text]
