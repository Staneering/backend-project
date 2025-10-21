
````markdown
# 🧙‍♂️ Backend Wizards — Stage 0 Task: Dynamic Profile API

This project is a simple RESTful API built with **Django**, designed to return my profile information along with a **dynamic cat fact** fetched from an external API.  

It’s part of the **Backend Wizards Stage 0 Task**, which validates understanding of REST APIs, JSON serialization, environment setup, and external API integration.

---

## 🚀 Features

- Returns personal profile information (`name`, `email`, `GitHub`, `bio`)
- Fetches a random cat fact dynamically from [catfact.ninja](https://catfact.ninja/fact)
- Includes status codes and error handling
- Uses environment variables for secure configuration
- Ready for deployment on [Railway.app](https://railway.app)

---

## 🧩 API Endpoint

### **GET** `/api/me`

#### ✅ Successful Response
```json
{
  "status": "success",
  "profile": {
    "name": "Ogochukwu Stanley Ikegbo",
    "email": "stacymacbrains@gmail.com",
    "github": "https://github.com/stacymacbrains",
    "bio": "Backend developer passionate about APIs and Django."
  },
  "cat_fact": "Cats can rotate their ears 180 degrees."
}
````

#### ⚠️ Error Response (e.g. timeout)

```json
{
  "status": "error",
  "profile": {
    "name": "Ogochukwu Stanley Ikegbo",
    "email": "stacymacbrains@gmail.com",
    "github": "https://github.com/stacymacbrains",
    "bio": "Backend developer passionate about APIs and Django."
  },
  "cat_fact": "The request to fetch cat fact timed out."
}
```

---

## ⚙️ Tech Stack

* **Python 3.x**
* **Django 5.x**
* **Gunicorn** (for production)
* **Requests** (for external API calls)
* **python-dotenv** (for environment variables)

---

## 🧠 How It Works

1. A GET request is made to `/api/me`.
2. Django returns static profile info.
3. It sends a live HTTP request to the Cat Fact API (`https://catfact.ninja/fact`) with a 5-second timeout.
4. If successful, it combines both into a JSON response.
5. If the request fails or times out, an error message and `status: "error"` are returned.

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Staneering/backend-wizards-stage0.git
cd backend-wizards-stage0
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # on Windows
# or
source venv/bin/activate # on macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your environment variables

Create a `.env` file in the project root:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
```

### 5. Run the development server

```bash
python manage.py runserver
```

Visit 👉 [http://127.0.0.1:8000/api/me](http://127.0.0.1:8000/api/me)

---

## ☁️ Deployment on Railway

1. Push your code to GitHub.
2. Connect your repository to [Railway.app](https://railway.app).
3. Set your environment variables (`SECRET_KEY`, `DEBUG=False`) in the Railway dashboard.
4. Add a **Procfile** to the root of your project:

   ```
   web: gunicorn mybackend.wsgi
   ```
5. Deploy 🎉

---

## 🧾 Example Project Structure

```
mybackend/
│
├── api/
│   ├── __init__.py
│   ├── urls.py
│   ├── views.py
│
├── mybackend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── Procfile
├── requirements.txt
└── .env
```

---

## 👨‍💻 Author

**Ogochukwu Stanley Ikegbo**
📧 [stacymacbrains@gmail.com](mailto:stacymacbrains@gmail.com)
🔗 [GitHub: stacymacbrains](https://github.com/stacymacbrains)

---

## 🐾 Credits

* [CatFact Ninja API](https://catfact.ninja/fact) for the random cat facts
* [Backend Wizards](https://backend-wizards.io/) for the task challenge

```


