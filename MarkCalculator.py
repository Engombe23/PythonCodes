# Assessed Task 1
firstMark = int(input("Input the first mark: "))
firstMarkWeight = int(input("Input the weight of the first mark: "))

secondMark = int(input("Input the second mark: "))
secondMarkWeight = int(input("Input the weight of the second mark: "))

thirdMark = int(input("Input the third mark: "))
thirdMarkWeight = int(input("Input the weight of the third mark: "))

print("The overall mark for the marks and weight input is: ")
print("Mark1 = " + str(float(firstMark)) + " Weight 1 = " + str(float(firstMarkWeight)) + "% weighted mark = " + str(float(firstMark)) + " x " + str(float(firstMarkWeight)) + "% = " + str(float(firstMark * (firstMarkWeight / 100))) + " %")
print("Mark2 = " + str(float(secondMark)) + " Weight 2 = " + str(float(secondMarkWeight)) + "% weighted mark = " + str(float(secondMark)) + " x " + str(float(secondMarkWeight)) + "% = " + str(float(secondMark * (secondMarkWeight / 100))) + " %")
print("Mark3 = " + str(float(thirdMark)) + " Weight 1 = " + str(float(thirdMarkWeight)) + "% weighted mark = " + str(float(thirdMark)) + " x " + str(float(thirdMarkWeight)) + "% = " + str(float(thirdMark * (thirdMarkWeight / 100))) + " %")

total = float(firstMark * (firstMarkWeight / 100)) + float(secondMark * (secondMarkWeight / 100)) + float(thirdMark * (thirdMarkWeight / 100))

print("Overall mark is " + str(firstMark * (firstMarkWeight/100)) + " % +" + str(secondMark * (secondMarkWeight/100)) + " % + " + str(thirdMark * (thirdMarkWeight/100)) + " % = " + str(total) + "%")