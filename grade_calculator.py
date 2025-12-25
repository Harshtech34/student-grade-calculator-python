# ================================
# Student Grade Calculator
# ================================

def calculate_grade(marks):
    """
    Determines grade and message based on marks
    """
    if 90 <= marks <= 100:
        return "A", "Excellent performance! Keep aiming high 🌟"
    elif 80 <= marks < 90:
        return "B", "Very Good! You're doing great 👍"
    elif 70 <= marks < 80:
        return "C", "Good job! A little more effort will help 😊"
    elif 60 <= marks < 70:
        return "D", "You passed. Focus more next time 💪"
    else:
        return "F", "Don't give up! Practice makes perfect 🌱"


def get_valid_marks():
    """
    Takes marks input and validates it (0-100 only)
    """
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")


def display_result(name, marks):
    """
    Displays the final result
    """
    grade, message = calculate_grade(marks)
    percentage = marks  # Out of 100

    print("\n📊 RESULT SUMMARY")
    print("-" * 30)
    print("Student Name :", name.upper())
    print("Marks        :", marks, "/100")
    print("Percentage   :", percentage, "%")
    print("Grade        :", grade)
    print("Message      :", message)
    print("-" * 30)


def main():
    print("🎓 STUDENT GRADE CALCULATOR 🎓")

    while True:
        name = input("\nEnter student name: ").strip()
        marks = get_valid_marks()

        display_result(name, marks)

        choice = input("\nDo you want to calculate for another student? (y/n): ").lower()
        if choice != 'y':
            print("\nThank you for using Student Grade Calculator 🙏")
            break   
# Program execution starts here
main()
