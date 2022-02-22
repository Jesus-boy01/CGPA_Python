numUnits = [5.0, 4.0, 3.0, 2.0, 1.0, 0.0]
numOfCourses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
qualityPoints = []
summation = 0
totalUnits = 0
gpa = 0
cQualityPoints = 0
cSummation = 0
cTotalUnits = 0
cGpa = 0

getStudentsSemester = eval(input("Enter the number of semesters completed: "))
for semesterCompleted in range(0, getStudentsSemester):
    getNumberOfCourse = eval(input("How many courses are you offering for this semester: "))
    if getNumberOfCourse in numOfCourses:
        for num in range(0, getNumberOfCourse):
            grade = int(input("Enter your grade: "))
            unitOfCourse = int(input("Enter the unit of this course: "))

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

    if getStudentsSemester == 1:
        for i in qualityPoints:
            summation = summation + i

        gpa = summation / totalUnits

        print(f"Your semester's gpa is {gpa}")

    print("\n")

if getStudentsSemester > 1:
    cTotalUnits += totalUnits
    for i in qualityPoints:
        cSummation += i
    cGpa = cSummation / cTotalUnits
    print(f"Your CGPA is {cGpa}")
