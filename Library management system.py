from datetime import datetime

books = {}
issued_book = {}

def add_book():
    while True:
        name = input("enter book name:")
        if name == "over":
            break
        else:
            books[name] = "hai ye book"
    print("book added successfully")
    print(f"available books are:{books}")
    
def show_book():
    if len(books)==0:
        print("khali hai library bhai,yaha ka maalik gareeb hai")
    else:
        print("books in library:")
        for b in books:
            print(b)
            
def issue_book():
   
    global date, issued_for_days, fee_per_day
    name = input("enter book name to issue:")
    
    if name in books:
        issued_book[name] = "ye book issue ho chuki hai"
        del books[name]
        print("books issued successfully")
        print(f"issued books are:{issued_book}") 
    else:
        print("book not available in library")
        return

    student_name = input("enter student name:")
    date = input("enter date of issue (YYYY-MM-DD):")
    issued_for_days = int(input("enter issued for how many days:"))
    fee_per_day = int(input("enter fee per day:"))

    n = {
        "student_name": student_name,
        "date": date,
        "issued_for_days": issued_for_days,
        "fee_per_day": fee_per_day
    }
    print(n)

def return_book():
    
    global date, issued_for_days, fee_per_day
    
    returns_date = input("enter return date (YYYY-MM-DD):")
    
    issue_date = datetime.strptime(date, "%Y-%m-%d")
    returns_date = datetime.strptime(returns_date, "%Y-%m-%d")
    
    late_days = (returns_date - issue_date).days - issued_for_days
    fine = 0
    
    if late_days > 0:
        for i in range(1, late_days + 1):
            week = (i-1)//7 + 1
            fine += 10 * week
        total = fee_per_day * issued_for_days + fine
        print("book returned successfully")
        print(f"fee to be paid with fine is:{total}")
    else:
        print("book returned successfully")
        print(f"no fine to be paid only fee paid:{fee_per_day*issued_for_days}")  


def library():
    
    while True:
        
        print("\n1. Add book")
        print("2. Show books")
        print("3. Issue books")
        print("4. Return books")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank you for using library")
            break
        else:
            print("Invalid choice")
            

library()