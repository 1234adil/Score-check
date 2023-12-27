import streamlit as st


def calculate_grade(score):
    if score >= 90 and score <= 100:
        return "Grade: A"
    elif score >= 80 and score < 90:
        return "Grade: B"
    elif score >= 70 and score < 80:
        return "Grade: C"
    elif score >= 60 and score < 70:
        return "Grade: D"
    else:
        return "Grade: E: \nSorry, you didn't pass the semester"


def main():
    st.title("Student Exam Grade Checker")

    score = st.number_input("Enter your exam score:", min_value=0, max_value=100, step=1)

    if st.button("Check Grade"):
        if score is not None:
            grade = calculate_grade(score)
            st.write(grade)


if __name__ == "__main__":
    main()
