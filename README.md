# 🚀 FastAPI User-Task Backend

## 📌 Overview

This project is a backend API built using FastAPI and SQLAlchemy.
It supports user management and task management with proper relational mapping.

---

## 🛠 Tech Stack

* Python (FastAPI)
* SQLAlchemy (ORM)
* PostgreSQL
* Pydantic (Validation)

---

## ⚙️ Features

* ✅ Create User
* ✅ Create Task under User
* ✅ One-to-Many Relationship (User → Tasks)
* ✅ Nested API Response (User with Tasks)
* ✅ Input Validation using Pydantic
* ✅ Eager Loading (joinedload)

---

## 📂 Project Structure

```
app/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── crud/
├── routers/
```

---

## 🔥 API Endpoints

### Create User

POST /users

### Create Task for User

POST /users/{user_id}/tasks

### Get Users with Tasks

GET /users_with_tasks

### Get Tasks by User

GET /users/{user_id}/tasks

---

## 🧠 Key Learnings

* Built REST APIs using FastAPI
* Implemented relational database design
* Used ORM for database operations
* Designed scalable backend structure

---

## 🚀 Future Improvements

* Add Authentication (JWT)
* Add Pagination
* Add Docker support

---
