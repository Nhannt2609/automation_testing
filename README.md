# 🧪 Automation Testing Project

This project contains **automated UI tests** for a web-based Transport Job system, developed using **Selenium WebDriver** and the **Python unittest** framework.

It is designed to follow the **Page Object Model (POM)** to improve **maintainability**, **scalability**, and **readability**.

---

## 🚀 Project Objectives

- ✅ Automate core UI functionalities for regression testing.
- ✅ Practice industry-standard testing patterns (POM, separation of concerns).
- ✅ Improve confidence in application behavior during frequent deployments.
- ✅ Enhance Python skills and testing mindset through real-world scenarios.

---

## 🔧 Tech Stack

- **Python 3.x**
- **Selenium**
- **unittest**
- **Faker** (for random test data)
- **python-dotenv** (for loading environment variables)

---

## 🗂️ Project Structure

```
automation_test/
├── config/
│   └── setting.py          # Load env
├── pages/
│   |── job_page.py          # Page Object Model (POM)
|   └── ...
├── tests/
│   |── test_job_cases.py    # Test cases
|   └── ...
├── .env                     # Environment variables (ignored by git)
├── utils/
├── .gitignore
└── README.md
```

---

## 📌 Notes

- Tests follow the Page Object Model design pattern.
- Sensitive data is stored in `.env` (make sure it's in `.gitignore`).

---

## 📚 Learning & Benefits

✍️ Practice writing clean test code using POM
💡 Understand separation of logic between UI interaction and test assertions
🔁 Learn test automation pipelines for CI/CD integration
✅ Build a foundation for professional QA automation roles

---

## 📎 Future Improvements

- Integration with pytest for better flexibility
- Add test reports using Allure or HTMLTestRunner
- Setup CI pipeline using GitHub Actions or Jenkins