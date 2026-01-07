from studentp import calculate_average, calculate_grade, get_student_result


def test_average():
    assert calculate_average([80, 90, 100]) == 90


def test_grade_A():
    assert calculate_grade(85) == "A"


def test_grade_S():
    assert calculate_grade(95) == "S"


def test_default_student():
    result = get_student_result()
    assert result["grade"] == "A"
