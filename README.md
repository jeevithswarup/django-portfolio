# 🚀 Django Portfolio Website

A modern, dynamic, and fully responsive **personal portfolio website** built using **Django** to showcase projects, skills, and professional profile with a powerful admin dashboard for content management.

> Designed for students and developers who want a production‑ready portfolio with real backend functionality.

---

## ✨ Features

* 🧩 Dynamic content management using **Django Admin (CMS-style)**
* 📂 Projects, skills, experience, and profile sections stored in database
* 🖼️ Media upload support (project images, profile photo)
* 🔐 Secure environment-based configuration
* ⚡ Fast and scalable backend using Django ORM
* 📱 Fully responsive UI (mobile & desktop friendly)
* ☁️ Production deployment ready (Render / Railway / VPS)
* 🗃️ PostgreSQL support

---

## 🧑‍💼 Easy to Use – No Coding Required (For Non‑Technical Users)

This portfolio website is designed so that **anyone can manage and update it without touching the source code**.

After initial setup by a developer, all regular updates can be done through a simple **admin dashboard**, similar to using Google Forms or a blog editor.

### What non‑technical users can do:

* ✏️ Update name, bio, and profile details
* 🧩 Add / edit / delete projects
* 🖼️ Upload new project images
* 🏆 Add skills, experience, education, and certifications
* 📞 Update contact information
* 👀 Instantly see changes live on the website

### How it works (simple explanation):

1. Open the admin page: `/admin`
2. Log in using username & password
3. Use easy forms to add or edit information
4. Click **Save**
5. Website updates automatically 🎉

No programming, no file editing, and no technical knowledge required.

This makes the project ideal for:

* Students
* Freelancers
* Job seekers
* Developers building client portfolios
* Small business owners

---

## 🛠️ Tech Stack

| Category        | Technologies                     |
| --------------- | -------------------------------- |
| Backend         | Django, Python                   |
| Frontend        | HTML5, CSS3, JavaScript          |
| Database        | SQLite (Dev) / PostgreSQL (Prod) |
| Media Storage   | Cloudinary / Local               |
| Deployment      | Render / Gunicorn / Whitenoise   |
| Version Control | Git & GitHub                     |

---

## 📸 Screenshots

<img width="1881" height="914" alt="image" src="https://github.com/user-attachments/assets/c2e6bc04-6448-4dee-94e5-45c650af9969" />

<img width="1722" height="947" alt="image" src="https://github.com/user-attachments/assets/726a2fb2-7443-43f7-8992-fb91cbab4bea" />
<img width="1900" height="921" alt="image" src="https://github.com/user-attachments/assets/d59c961d-6218-4ec5-88f4-cb294e2b2df6" />




---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/jeevithswarup/django-portfolio.git
cd django-portfolio
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
CLOUDINARY_URL=your_cloudinary_url
```

### 5️⃣ Apply migrations

```bash
python manage.py migrate
```

### 6️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run the server

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

Admin Panel: `http://127.0.0.1:8000/admin/`

---

## 🌐 Deployment

This project is ready for production deployment on:

* Render
* Railway
* VPS (Ubuntu + Gunicorn + Nginx)

### Production checklist

* Set `DEBUG = False`
* Configure `ALLOWED_HOSTS`
* Use PostgreSQL
* Configure static files
* Enable Whitenoise

---

## 📁 Project Structure

```
django-portfolio/
│── portfolio/
│── projects/
│── templates/
│── static/
│── media/
│── manage.py
│── requirements.txt
```

---

## 🧠 Learning Outcomes

* Practical Django project architecture
* ORM modeling & relationships
* Admin panel customization
* Secure configuration using environment variables
* Production deployment process
* Full‑stack development workflow

---

## 🧪 Future Improvements

* User authentication
* Blog module
* REST API integration
* SEO optimization
* Dark mode UI
* Docker support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Jeevith Swarup**
🎓 Computer Science Student
🌐 GitHub: [https://github.com/jeevithswarup](https://github.com/jeevithswarup)

---

## ⭐ Support

If you like this project, please consider giving it a **star ⭐** on GitHub — it helps a lot!

---

> Built with ❤️ using Django
