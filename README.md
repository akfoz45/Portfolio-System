# 👨‍💻 Django Personal Portfolio CMS

A fully dynamic, responsive personal portfolio website built with **Django 5** and **Bootstrap 5**. This project acts as a mini-CMS (Content Management System), allowing the owner to manage profile details, projects, and skills directly through the frontend after logging in.

![Project Screenshot](image_4b93db.png) 
## 🚀 Features

* **Dynamic Content Management:** Update your "About Me", "Profile Picture", and "Subtitle" without touching the code.
* **Project CRUD:** Add, Edit, and Delete projects directly from the dashboard.
* **Secure Admin Access:** Editing features are only visible and accessible to logged-in administrators (`@login_required`).
* **Contact Form:** Functional contact form (currently logging to console for development).
* **Responsive Design:** Fully responsive layout using Bootstrap 5 and custom CSS for mobile compatibility.
* **Database:** Uses SQLite for easy development and deployment.

## 🛠️ Tech Stack

* **Backend:** Python, Django 5.x
* **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
* **Database:** SQLite (Default)
* **Styling:** Custom CSS + Bootstrap Grid

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/akfoz45/Portfolio-System.git
    cd Portfolio-System
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (to manage the site):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the server:**
    ```bash
    python manage.py runserver
    ```

7.  **Visit the site:**
    Open `http://127.0.0.1:8000/` in your browser.

## 📖 Usage

1.  **Guest View:** Visitors can see your profile, projects list, and details.
2.  **Admin View:**
    * Go to `/admin` or click a "Login" link (if added) to log in with your superuser credentials.
    * Once logged in, you will see **Edit (✏️)** and **Delete (🗑️)** buttons on project cards.
    * You can edit your profile information directly from the home page header.

## 📂 Project Structure

```text
├── config/             # Main Django configuration
├── portfolio/          # The portfolio app
│   ├── migrations/     # Database migrations
│   ├── static/         # CSS, JS, and Image files
│   ├── templates/      # HTML templates
│   ├── forms.py        # Django Forms
│   ├── models.py       # Database Models (Project, Profile)
│   ├── views.py        # Business logic & Views
│   └── ...
├── media/              # User uploaded content (Images)
├── db.sqlite3          # Database file
└── manage.py           # Django command-line utility
```