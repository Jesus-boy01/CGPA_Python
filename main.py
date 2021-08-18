# GPA FOR FIRST SEMESTER
print("FIRST SEMESTER")
numUnits = [5.0, 4.0, 3.0, 2.0, 1.0, 0.0]
qualityPoints = []
summation = 0
totalUnits = 0
gpa = 0
cQualityPoints = 0
cSummation = 0
cTotalUnits = 0
cGpa = 0

for num in range(0, 5):
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

for i in qualityPoints:
    summation = summation + i

gpa = summation / totalUnits

print(f"Your semester's gpa is {gpa}")

print("\n")

# GPA FOR SECOND SEMESTER
print("SECOND SEMESTER")
numUnits2 = numUnits.copy()
qualityPoints2 = []
summation2 = 0
totalUnits2 = 0
gpa2 = 0

for num2 in range(0, 7):
    grade2 = int(input("Enter your grade: "))
    unitOfCourse2 = int(input("Enter the unit of this course: "))

    if 70 <= grade2 <= 100:
        qualityPoints2.append(numUnits2[0] * unitOfCourse2)
    elif 60 <= grade2 < 70:
        qualityPoints2.append(numUnits2[1] * unitOfCourse2)
    elif 50 <= grade2 < 60:
        qualityPoints2.append(numUnits2[2] * unitOfCourse2)
    elif 45 <= grade2 < 50:
        qualityPoints2.append(numUnits2[3] * unitOfCourse2)
    elif 40 <= grade2 < 45:
        qualityPoints2.append(numUnits2[4] * unitOfCourse2)
    elif 0 <= grade2 < 40:
        qualityPoints2.append(numUnits2[5] * unitOfCourse2)
    else:
        print("Invalid Grade Entered")

    totalUnits2 = totalUnits2 + unitOfCourse2

for i in qualityPoints2:
    summation2 = summation2 + i

gpa2 = summation2 / totalUnits2

print(f"Your semester's gpa is {gpa2}")

cTotalUnits = totalUnits + totalUnits2
cQualityPoints = qualityPoints + qualityPoints2

for i in cQualityPoints:
    cSummation = cSummation + i

cGpa = cSummation / cTotalUnits

print(f"\nYour CGPA is {cGpa}")
