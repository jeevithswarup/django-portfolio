🚀 Dynamic Portfolio Management System

🔥 A production-grade, database-driven portfolio management system built using Django and PostgreSQL.
This project is designed as a reusable content management platform, not a static personal website ⚡

✨ The system enables complete control of portfolio content through an administrative interface, allowing non-technical users to manage projects, documents, media, and academic data without modifying source code.

⚠️ Traditional portfolio websites are static and require developer intervention for every content update.
🚀 This project solves that limitation by providing a fully dynamic backend architecture where all portfolio data is stored in a relational database and managed via Django Admin.

✨ The application follows production deployment best practices and cloud-based media handling, making it suitable for real-world usage.

⚡ Core Capabilities
✅ Dynamic content rendering using database-backed models
✅ Centralized admin panel for content management
✅ Cloud-based storage for images and PDF documents ☁️
✅ PostgreSQL database integration for production 🐘
✅ Environment-based configuration for deployment ⚙️
✅ Static file optimization for production environments 🚀


🏗️ System Architecture
🧠 Backend
Django 5.2.4 (MTV architecture)

Django ORM for database abstraction

PostgreSQL as primary production database

☁️ Media Handling
Cloudinary used for media storage

Images and PDF files served via cloud URLs

No dependency on local filesystem storage

🚀 Deployment
Hosted on Render
Gunicorn as WSGI server
Automatic migrations and static file collection on deploy
