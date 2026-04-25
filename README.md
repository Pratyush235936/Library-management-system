# 📚 Library Management System (Python CLI Project)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project](https://img.shields.io/badge/Level-Beginner-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📝 Project Overview

The **Library Management System** is a simple command-line application built using Python.  
It helps manage library operations such as adding books, issuing books to students, returning books, and calculating fines for late returns.

This project is ideal for beginners to understand how real-world systems like libraries can be implemented using programming logic.

---

## 🎯 Objectives

- Learn Python basics through a real-world project  
- Understand how to use dictionaries for data storage  
- Implement date-based calculations using `datetime`  
- Build a menu-driven system  

---

## 🚀 Features

- ➕ Add books to the library  
- 📖 Display available books  
- 📕 Issue books to students  
- 🔁 Return books  
- ⏳ Automatic fine calculation for late returns  
- 📅 Date-based tracking system  
- 🖥️ Interactive CLI menu  

---

## 🛠️ Technologies Used

- **Language:** Python 3  
- **Module:** datetime  
- **Concepts:**
  - Dictionaries  
  - Functions  
  - Loops & Conditions  
  - Date calculations  

---

## 📂 Project Structure


library-management-system/
│── main.py # Main program
│── README.md # Documentation


---

## ⚙️ How the System Works

### 📚 Book Storage
Books are stored in a dictionary:

books = {}


- Key → Book Name  
- Value → "available"  

---

### 📕 Issue Process

- User selects a book  
- If available:
  - Book is moved to issued list  
- User enters:
  - Student name  
  - Issue date  
  - Number of days  
  - Fee per day  

---

### 🔁 Return Process

- User enters return date  
- System calculates delay:

late_days = (return_date - issue_date) - allowed_days


---

### 💰 Fine Calculation Logic

- No fine → if returned on time  
- Late return → fine increases weekly:

| Week | Fine per Day |
|------|-------------|
| 1    | ₹10         |
| 2    | ₹20         |
| 3    | ₹30         |

Total cost:

total = (fee_per_day × issued_days) + fine


---

## ▶️ How to Run

### 1️⃣ Clone Repository

git clone https://github.com/Pratyush235936/library-management-system.git


### 2️⃣ Navigate to Folder

cd library-management-system


### 3️⃣ Run Program

python main.py


---

## 🖥️ Menu Preview

Add book
Show books
Issue books
Return books
Exit

---

## ⚠️ Limitations

- ❌ Uses global variables (not scalable)  
- ❌ Supports only one issued record at a time  
- ❌ Data is not saved permanently  
- ❌ No user authentication system  

---

## 📌 Future Improvements

- 👥 Support multiple users  
- 💾 Save data using files/database  
- 🧱 Convert to Object-Oriented Programming (OOP)  
- 🖼️ Add GUI (Tkinter)  
- 📊 Improve fine calculation system  

---

## 🧠 Learning Outcomes

- Python fundamentals  
- Data handling using dictionaries  
- Date calculations  
- Building menu-driven applications  

---

## 👨‍💻 Author

**Pratyush Yadav**  
🔗 GitHub: https://github.com/Pratyush235936  

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project useful:

⭐ Star this repository  
🍴 Fork it  
📢 Share it  

---

## 💬 Feedback

Suggestions and improvements are always welcome!
