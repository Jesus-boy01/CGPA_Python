# Initialization of variables
numUnits = [5.0, 4.0, 3.0, 2.0, 1.0, 0.0]
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

for semesterCompleted in range(0, getStudentsSemester):
    getNextScore = input("Do you want to input a score(Y or N): ").upper()

# program to obtain scores of the user based on if the user chooses to input more courses

    while getNextScore == "Y":
        score = eval(input("Enter your score: "))
        unitOfCourse = int(input("Enter the unit of this course: "))
        if unitOfCourse == 0:
            raise Exception("Sorry a course cannot be 0 units")

        getNextScore = input("Do you want to input another score(Y or N): ").upper()

        if 70 <= score <= 100:
            qualityPoints.append(numUnits[0] * unitOfCourse)
        elif 60 <= score < 70:
            qualityPoints.append(numUnits[1] * unitOfCourse)
        elif 50 <= score < 60:
            qualityPoints.append(numUnits[2] * unitOfCourse)
        elif 45 <= score < 50:
            qualityPoints.append(numUnits[3] * unitOfCourse)
        elif 40 <= score < 45:
            qualityPoints.append(numUnits[4] * unitOfCourse)
        elif 0 <= score < 40:
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

    print(f"Your CGPA is {cGpa}")
