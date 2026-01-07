def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


def get_student_result(
    name="Default Student",
    department="CSE",
    semester=5,
    marks=(85, 90, 88)
):
    avg = calculate_average(marks)
    grade = calculate_grade(avg)

    return {
        "name": name,
        "department": department,
        "semester": semester,
        "average": round(avg, 2),
        "grade": grade
    }


def main():
    result = get_student_result()
    print("Student Result")
    print("----------------")
    for key, value in result.items():
        print(f"{key.capitalize()}: {value}")


if __name__ == "__main__":
    main()
