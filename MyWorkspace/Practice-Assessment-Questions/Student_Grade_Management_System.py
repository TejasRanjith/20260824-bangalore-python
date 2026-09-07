import subprocess

students = [
    {"id": 1, "name": "Aarav Sharma", "course": "Python Core", "marks": 88.5, "grade": "A"},
    {"id": 2, "name": "Diya Patel",   "course": "Data Science", "marks": 74.0, "grade": "B"}
]

def enroll_stud():
    name = input("Enter Candidate's Name (only letters pls): ").title().strip()
    if len(name)==0:
        print("Name cannot be empty... pls try again")
        return -1
    course = input("Enter Course enrolled for (only letters pls): ").title().strip()
    if len(course)==0:
        print("Course cannot be empty... pls try again")
        return -1
    try:
        marks = int(input("Enter the Marks achieved :"))
        if 0.0 >= marks >= 100.0: 
            return -1
    except ValueError:
        print("Please enter marks as int....")
        
def grade(marks):
    if marks >= 85:
        return 'A'
    elif marks in range(70,85):
        return 'B'
    
    elif marks in range(50,70):
        return 'C'
    else:
        return 'F'



def menu():
    print("*"*15,"Student Grade Management System".upper(),"*"*15,"\n   ")
    print("""    [1] Enroll Student  \n    [2] Cohort Directory  \n    [3] Query Records  \n    [4] Revise Evaluation  \n    [5] Purge Record  \n    [6] Save to JSON  \n    [7] Load from JSON  \n    [8] Terminate\n   """)
    try:
        choice = int(input("Enter the choice: "))
        return choice
    except ValueError:
        return -1
    

def main():
    while True:
        choice = menu()
        match choice:
            case 0:
                subprocess.call('cls',shell=True)
            case 1:
                print(grade(int(input("Enter grade --> "))))
            case 8:
                print("\n","*"*60,'\n',sep='')
                break
            case -1:
                pass
            case _:
                print("\nInvalid Choice, please try again.\n")


if __name__ == '__main__':
    main()
    
    