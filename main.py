#main of grade calculator

def main():
    print('###########################################')
    print('            GRADE CALCULATOR')
    print('                by Aidan')
    print('###########################################')


    gradeTypes = []
    userInput = 'x'
    userInput2 = 'x'

    print("Enter 'done' when you have no further entries.\n")
    print("STEP ONE: ENTER GRADE TYPES")
    while userInput != 'done':
        userInput = input("Enter the grade type (homework, quiz, etc): ")

        if userInput != 'done':
            userInput2 = input("Enter the percentage that grade makes up of final grade: ")
            gradeTypes.append([userInput, userInput2])
    print()

    print("STEP TWO: ENTER INDIVIDUAL GRADES")
    grades = []
    for type in gradeTypes:
        userInput = 'x'
        tempGrades = []
        while userInput != 'done':
            userInput = input("Enter your grades for '" + type[0].upper() + "': ")
            if userInput != 'done':
                tempGrades.append(userInput)
        grades.append(tempGrades)
    print(grades)

    typeGrades = []
    c = 0
    for type in grades:
        typeGrades.append(average(grades[c]))
        c = c + 1

    print(typeGrades)

    totalPercentage = 0
    totalAccumPoints = 0
    c = 0
    print("\n\nGRADE STATISTICS")
    for type in gradeTypes:
        print("AVERAGE '" + type[0].upper() + "' GRADE: " + str(int(typeGrades[c])))
        print("PERCENT OF GRADE: " + type[1])
        print()
        totalPercentage = int(totalPercentage) + int(type[1])
        totalAccumPoints = totalAccumPoints + (typeGrades[c] * (int(type[1])/100))
        c = c + 1

    print("\nFINAL GRADE: " + str(int(totalAccumPoints/totalPercentage * 100)))


def average(L):
    sum = 0
    c = 0
    for i in L:
        sum = sum + int(i)
        c = c + 1
    return sum/c


main()