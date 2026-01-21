print("===== Student Insight Generator =====")

students = []

# STEP 1: number of students
n = int(input("Enter number of students: "))

# STEP 2: get name & mark
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    mark = int(input(f"Enter mark of {name}: "))

    students.append({
        "name": name,
        "mark": mark
    })

# STEP 3: calculations
passed = 0
failed = 0
marks = []

for s in students:
    marks.append(s["mark"])
    if s["mark"] >= 50:
        passed += 1
    else:
        failed += 1

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

# STEP 4: performance insight
if average >= 75:
    performance = "Excellent"
elif average >= 60:
    performance = "Good"
elif average >= 50:
    performance = "Average"
else:
    performance = "Poor"

# STEP 5: find topper
topper = students[0]
for s in students:
    if s["mark"] > topper["mark"]:
        topper = s

# STEP 6: output student details with grade
print("\n===== STUDENT DETAILS =====")
for s in students:
    if s["mark"] >= 75:
        grade = "A"
    elif s["mark"] >= 60:
        grade = "B"
    elif s["mark"] >= 50:
        grade = "C"
    else:
        grade = "F"

    print(s["name"], "->", s["mark"], "| Grade:", grade)

# STEP 7: final insights
print("\n===== INSIGHTS =====")
print("Total students     :", len(students))
print("Passed students    :", passed)
print("Failed students    :", failed)
print("Highest mark       :", highest)
print("Lowest mark        :", lowest)
print("Average mark       :", round(average, 2))
print("Class performance  :", performance)
print("Topper             :", topper["name"], "with", topper["mark"])
