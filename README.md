# 🚀 Personal Task Manager API

A production-ready backend API built with FastAPI that supports user authentication and task management with secure, user-specific access control.

---

## 🌐 Live Demo

👉 https://task-manager-b7px.onrender.com/docs

---

## 🔐 Features

### Authentication

* User Registration
* User Login
* JWT-based Authentication
* Secure password hashing using bcrypt

### Task Management

* Create Task
* Get User-specific Tasks
* Update Task
* Delete Task

### Advanced Features

* Filtering tasks by status (pending / done)
* Pagination support (limit & offset)
* Ownership validation (users can only access their own tasks)

---

## 🧱 Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL (Supabase)
* **ORM:** SQLAlchemy
* **Authentication:** JWT (python-jose)
* **Security:** Passlib (bcrypt)
* **Containerization:** Docker
* **Deployment:** Render

---

## ⚙️ API Endpoints

### Auth

* `POST /register` → Register user
* `POST /login` → Login & get JWT

### Tasks

* `POST /tasks` → Create task
* `GET /tasks` → Get tasks (with filtering & pagination)
* `PUT /tasks/{id}` → Update task
* `DELETE /tasks/{id}` → Delete task

---


## 🐳 Run with Docker

### Build Image

```bash
docker build -t task-manager-api .
```

### Run Container

```bash
docker run -p 8000:8000 --env-file .env task-manager-api
```

---

## 🧪 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🧠 Key Learnings

* Implemented JWT-based authentication and authorization
* Designed secure user-specific data access
* Built scalable APIs with filtering and pagination
* Containerized and deployed backend applications

---

## 📌 Notes

* Deployed on Render free tier (may have cold start delays)
* Browser may show warning due to new domain (safe to proceed)

---


