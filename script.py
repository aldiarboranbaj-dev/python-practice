name = input("Enter your name: ")
math = float(input("Enter your math: "))
phys = float(input("Enter your physics: "))
python = float(input("Enter your python: "))
avg = (math+phys+python)/3

scholarship = 35000 if avg >= 90 else 0

gpa = avg/25

print("==============================")
print("STUDENT REPORT CARD")
print("==============================")
print("Student :", name)
print("Math :", math)
print("Physics :", phys)
print("Python :", python)
print("------------------------------")
print("Average :", round(avg, 2))
print("GPA :", round(gpa, 2))
print("Scholarship :", scholarship, "KZT")
print("==============================")