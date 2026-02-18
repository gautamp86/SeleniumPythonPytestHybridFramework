# Selenium Python Pytest Hybrid Framework

This project demonstrates a **Selenium + Python + Pytest Hybrid Automation Framework** designed using **Page Object Model (POM)** and aligned with **OOPS principles** for scalability and maintainability.

---

## 🚀 Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- OpenPyXL (Excel DDT)
- Logging
- Git & GitHub

---

## 🏗️ Framework Architecture
                    +----------------------+
                    |      config.ini       |
                    | (Environment Config)  |
                    +-----------+----------+
                                |
                                v
                    +----------------------+
                    |     conftest.py      |
                    | (Pytest Fixtures)    |
                    +-----------+----------+
                                |
                                v
                    +----------------------+
                    |    DriverFactory     |
                    | (Polymorphism)       |
                    +-----------+----------+
                                |
                                v
         +------------------------------------------+
         |               Test Cases                 |
         |   (Business Validation & Assertions)     |
         +------------------+-----------------------+
                            |
                            v
         +------------------------------------------+
         |              Page Objects                |
         | LoginPage / AddRowPage / LanguageTable   |
         | (Encapsulation + Abstraction)            |
         +------------------+-----------------------+
                            |
                            v
         +------------------------------------------+
         |               BasePage                   |
         |  Click | Type | Wait | Common Actions   |
         |            (Inheritance)                |
         +------------------+-----------------------+
                            |
                            v
                    +----------------------+
                    |     Selenium WebDriver|
                    +----------------------+

project/
│
├── pageObjects/
│ ├── BasePage.py
│ ├── LoginPage.py
│ ├── AddRowPage.py
│ ├── LanguageTablePage.py
│
├── utilities/
│ ├── DriverFactory.py
│ ├── BaseClass.py
│ ├── readProperties.py
│ ├── customLogger.py
│ ├── ExcelUtils.py
│
├── testCases/
│ ├── test_login.py
│ ├── test_login_ddt.py
│ ├── test_AddRow.py
│ ├── test_language_filter.py
│
├── TestData/
│ └── DataLogin.xlsx
│
├── Screenshots/
├── conftest.py
├── config.ini
└── README.md

---

## 🧠 Framework Design (OOPS Principles)

### ✔ Inheritance
- `BasePage` provides reusable methods like click(), type().
- Page objects inherit from BasePage.

### ✔ Encapsulation
- Locators are kept private inside page classes.

### ✔ Abstraction
- Tests call business methods like:
  - `login()`
  - `click_add_button()`
- Selenium implementation is hidden from tests.

### ✔ Polymorphism
- Browser handling implemented using `DriverFactory`.

---

## ⭐ Key Features

- Page Object Model design
- Data Driven Testing (Excel)
- Cross-browser support (Chrome / Firefox / Edge)
- Centralized Driver Management
- Config-based environment setup
- Logging support
- Screenshot capture on failure
- Explicit waits (No hard sleeps)
- Pytest markers (sanity / regression)

---

## ⚙️ Configuration
Framework configuration is maintained in:
config.ini
Example:
[common info]
baseURL = https://practicetestautomation.com/practice-test-login/
browser = chrome
username = student
password = Password123
▶️ How to Run Tests
Run all tests
pytest
Run single test file
pytest testCases/test_login.py
Run single test case
pytest testCases/test_login.py::Test_001_Login::test_login
Run by marker
pytest -m sanity
🔁 Data Driven Testing (DDT)
Test data is maintained in:

TestData/DataLogin.xlsx
Excel data is read dynamically using ExcelUtils.

🧪 Cross Browser Execution
Browser selection is handled through:
DriverFactory.py
Supported browsers:
Chrome
Firefox
Edge

📸 Screenshots
Screenshots are automatically captured for failed tests and saved in:

Screenshots/
📝 Logging
Logs are generated using custom logger utility:

utilities/customLogger.py
🤝 Git Workflow
git add .
git commit -m "message"
git push origin main

👨‍💻 Author
Gautam Pophali
Automation QA Engineer
Python | Selenium | Pytest | API Testing

⭐ Future Improvements
Parallel execution (pytest-xdist)
Jenkins CI integration
Allure reporting
API + UI hybrid execution
Docker/Grid execution
