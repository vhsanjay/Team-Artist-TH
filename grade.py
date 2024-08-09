def calculate_grade():
    math_score = float(input("Enter math score: "))
    science_score = float(input("Enter science score: "))
    english_score = float(input("Enter english score: "))
    history_score = float(input("Enter history score: "))
    geography_score = float(input("Enter geography score: "))
    total_score = math_score + science_score + english_score + history_score + geography_score
    average_score = total_score / 5
    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    elif average_score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade
grade = calculate_grade()
print("Grade:", grade)
