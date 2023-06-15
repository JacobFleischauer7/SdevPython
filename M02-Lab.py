#Jacob Fleischauer
#M02-Lab.py
#This application will accept the name and GPA of a student and specify if this student has made honor roll
# or the deans list.
print("Enter the student's last name, or ZZZZ to quit.")
L = input()
if L == "ZZZZ":
    exit()
print("Enter the student's first name")
N = input()
print("Enter the student's GPA")
GradePA = float(input())
if GradePA >= 3.5:
    print(N+" "+L+" has made the Dean's list.")
if GradePA >= 3.25:
    print(N+" "+L+" has made Honor Roll.")
print(str(L)+" "+str(N)+" "+str(GradePA))
#if GradePA ZZ