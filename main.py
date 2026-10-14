import sys
students=[]

def add_student():
    name = input("\nEnter Student name: ")
    age = int(input("Enter Student age: "))
    mark = float(input("Enter Student marks: "))
 
    student=(name, age, mark)

    students.append(student)
    print(F"\n{name.capitalize()} added successfully!\n")

def view_student():
    if not students:
        print("No student found.")
    else:
        print("\n----- Student List -----\n")
        print("Slno. Name       Age    Mark")
        print("-"*28)
        t=1
        for i in students:
            print(f"[{t}]   {i[0].capitalize():<10} {i[1]:<6} {i[2]:<4}")
            t += 1
    print()

def search_student():
    name = input("\nEnter Name to search: ").strip()
    print("\n----- Search result -----\n")
    found =[s for s in students if s[0].lower() == name.lower()]
    if found:
        print("Slno. Name       Age    Mark")
        print("-"*28)
        t=1
        for i in found:
            print(f"[{t}]   {i[0].capitalize():<10} {i[1]:<6} {i[2]:<4}")
            t += 1
    else:
        print(f"- No record found for {name.capitalize()}.")

def delete_student():
    name = input("Enter Name to delete: ").strip()
    global students
    exist=[]
    for i in students:
        if i[0] == name:
            exist.append(i)

    if not exist:
        print("Student not found. The specified student does not exist in the system.")
    else:
        print("\nID    Name       Age    Mark")
        print("----------------------------")
        t=1
        for i in exist:
            print(f"[{t}]   {i[0]:<10} {i[1]:<6} {i[2]:<4}")
            t += 1

        find_dlt_index = int(input("\nEnter ID to delete: "))
        students.remove(exist[find_dlt_index-1])
                
        print(f"Student Name: {exist[find_dlt_index-1][0].capitalize()} Age: {exist[find_dlt_index-1][1]} Deleted ")

def unique_name():
    if not students:
        print("No student records available. Please add a student first.")
    else:
        names = set([s[0] for s in students])
        print(f"\nUnique Student names: ")
        for i in names:
            print(i.capitalize(), end=" | ")
        print()

def student_summery():
    if not students:
            print("No student records available. Please add a student first.")
    else:
        summery ={
            "Students": len(students),
            "Avarage Mark" : sum([s[2] for s in students])/len(students) if students else 0
        }
        print("\n----------Summery----------\n")
        for key, value in summery.items():
            print(f"{key}: {value}")
        print()

def save_in_file():
    try:
        with open("students.txt", "w") as f:
            for s in students:
                f.write(f"{s[0]},{s[1]},{s[2]}\n")
        print("Data save in student.txt\n")
    except Exception as e:
        print("Error saving file ", e)

        
def load_file():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, age, mark= line.strip().split(",")
                students.append((name, int(age), float(mark)))
        print("Data loaded from file.\n")
    except:
        print("students.txt Not found")
        sys.exit()

def main():
    load_file()
    print("==== Student Managment System ====")
    while True:
        print('''
--------------------------\n
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Show Unique Names
6. Summary
7. Save & Exit\n''')

        choice = input("Enter your choice: ")
        if choice =="1":
            add_student()
        elif choice =="2":
            view_student()
        elif choice =="3":
            search_student()
        elif choice =="4":
            delete_student()
        elif choice =="5":
            unique_name()
        elif choice =="6":
            student_summery()
        elif choice =="7":
            save_in_file()
            break

if __name__=="__main__":
    main()