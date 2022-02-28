# Initialization of variables
numUnits = [5.0, 4.0, 3.0, 2.0, 1.0, 0.0]
numOfCourses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
totalNumOfSemesters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qualityPoints = []
summation = 0
totalUnits = 0
gpa = 0
cQualityPoints = 0
cSummation = 0
cTotalUnits = 0
cGpa = 0

# program to get the number of semesters completed by the user and check to see that the input is valid

getStudentsSemester = eval(input("Enter the number of semesters completed: "))
if getStudentsSemester not in totalNumOfSemesters:
    raise Exception("Sorry, Invalid value or value greater than the maximum number of semesters that can be chosen")

# program to obtain the number of courses offered by the user and to check to see that the input is valid

for semesterCompleted in range(0, getStudentsSemester):
    getNumberOfCourse = eval(input("How many courses are you offering for this semester: "))
    if getNumberOfCourse not in numOfCourses:
        raise Exception("Sorry, Invalid value or value greater than the maximum number of courses that can be chosen")

# program to calculate the total quality points and total units

    if getNumberOfCourse in numOfCourses:
        for num in range(0, getNumberOfCourse):
            grade = int(input("Enter your score: "))
            unitOfCourse = int(input("Enter the unit of this course: "))

            if unitOfCourse == 0:
                raise Exception("Sorry a course cannot be 0 units")

            if 70 <= grade <= 100:
                qualityPoints.append(numUnits[0] * unitOfCourse)
            elif 60 <= grade < 70:
                qualityPoints.append(numUnits[1] * unitOfCourse)
            elif 50 <= grade < 60:
                qualityPoints.append(numUnits[2] * unitOfCourse)
            elif 45 <= grade < 50:
                qualityPoints.append(numUnits[3] * unitOfCourse)
            elif 40 <= grade < 45:
                qualityPoints.append(numUnits[4] * unitOfCourse)
            elif 0 <= grade < 40:
                qualityPoints.append(numUnits[5] * unitOfCourse)
            else:
                print("Invalid Grade Entered")
                break

            totalUnits = totalUnits + unitOfCourse

# program to calculate one semester gpa

    if getStudentsSemester == 1:
        for i in qualityPoints:
            summation = summation + i

        gpa = summation / totalUnits
        print(f"Your semester's gpa is {gpa}")

    print("\n")

# program to calculate the cgpa based on the number of semesters obtained from the user

if getStudentsSemester > 1:
    cTotalUnits += totalUnits
    for i in qualityPoints:
        cSummation += i
    cGpa = cSummation / cTotalUnits

# program to catch division by 0 error
    try:
        print(f"Your semester's gpa is {gpa}")
    except ZeroDivisionError:
        print("Sorry, you can't divide by 0")

    print(f"Your CGPA is {cGpa}")
