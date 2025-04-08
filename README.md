# 📝 Task Management Application

A full-stack, multi-service task management system with user authentication and task CRUD operations. Built using:

- **Frontend**: Vue.js (Vite)
- **Auth Backend**: Node.js (Express) + SQLite
- **Task Backend**: Django + DRF + SQLite
- **Authentication**: JWT-based login & registration
- **Extras**: Export tasks to Excel

## 📁 Project Structure

```

task-manager/
├── auth-backend/ # Node.js Auth API
├── taskbackend/ # Django Task API
├── frontend/ # Vue.js Frontend
└── README.md

```

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/bhavart-joshi/task-manager.git
cd task-manager
```

### 2. Setup: Auth Backend (Node.js)

```bash
cd auth-backend
npm install
```

#### 🔧 Create a `.env` file

```env
PORT=5000
JWT_SECRET=jwt_secret
```

#### ▶️ Run the server

```bash
node server.js
```

Runs at: [http://localhost:5000](http://localhost:5000)

### 3. Setup: Task Backend (Django)

```bash
cd ../task-backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### 🔧 Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### ▶️ Run the server

```bash
python manage.py runserver
```

Runs at: [http://localhost:8000](http://localhost:8000)

### 4. Setup: Frontend (Vue.js)

```bash
cd ../frontend
npm install
```

#### ▶️ Start Vite Dev Server

```bash
npm run dev
```

Runs at: [http://localhost:5173](http://localhost:5173)

> Make sure all three servers (auth, task, frontend) are running.

## 🔐 Auth API (Node.js)

**Base URL**: `http://localhost:5000/api/auth`

| Endpoint    | Method | Description                  |
| ----------- | ------ | ---------------------------- |
| `/register` | POST   | Register new user            |
| `/login`    | POST   | Login with username/password |

### 📥 Sample: Register

```json
POST /api/auth/register
Content-Type: application/json

{
  "username": "username",
  "password": "password123"
}
```

### 📥 Sample: Login

```json
POST /api/auth/login
Content-Type: application/json

{
  "username": "username",
  "password": "password123"
}
```

**Response:**

```json
{
  "token": "jwt.token"
}
```

Use this token for authenticated requests to Django API.

## ✅ Task API (Django)

**Base URL**: `http://localhost:8000/api/tasks/`

| Endpoint         | Method | Description     |
| ---------------- | ------ | --------------- |
| `/tasks/`        | GET    | List all tasks  |
| `/tasks/`        | POST   | Create a task   |
| `/tasks/<id>/`   | PUT    | Update a task   |
| `/tasks/<id>/`   | DELETE | Delete a task   |
| `/tasks/export/` | GET    | Export to Excel |

Include JWT token from auth backend in headers:

```
Authorization: Bearer jwt.token
```

### 📥 Sample: Create Task

```json
POST /api/tasks/
Authorization: Bearer jwt.token
Content-Type: application/json

{
  "title": "Finish project",
  "description": "Complete the full-stack task manager",
  "effort_days": 3,
  "due_date": "2025-04-15"
}
```

## 🧪 Example Workflow

1. **Register/Login** using the frontend
2. **Fetch JWT** and store in local storage or memory
3. **Access Django Task API** using the token
4. **Create, Edit, Delete Tasks**
5. **Export** to Excel via `/api/tasks/export/` or frontend

## 🧰 Tech Stack

| Layer    | Stack                      |
| -------- | -------------------------- |
| Frontend | Vue.js + Vite              |
| Auth API | Node.js + Express + SQLite |
| Task API | Django + DRF + SQLite      |

## 👤 Author

Bhavarth Joshi - [@bhavarth-joshi](https://github.com/bhavarth-joshi)
