# Taggar Associates Blog 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-3.2.6-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A professional and dynamic blog website built with **Django**. This platform is designed to share insights, articles, and updates for Taggar Associates, featuring a clean UI and robust backend.

## 🌟 Features

*   **Dynamic Blog System:** Create, read, update, and delete blog posts easily.
*   **Rich Media Support:** Embed videos seamlessly using `django-embed-video`.
*   **Responsive Design:** Built with **Bootstrap 4** via `django-crispy-forms` for a mobile-first experience.
*   **User Authentication:** Secure login and management for administrators.
*   **Sitemap & SEO:** Integrated `sitemaps` and `sites` framework for better search engine visibility.
*   **Contact Integration:** SMTP email backend configuration for handling inquiries.
*   **Image Processing:** Optimized image handling with `Pillow`.

## 🛠️ Tech Stack

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, Bootstrap 4
*   **Database:** SQLite (Dev) / Configurable (Prod)
*   **Utilities:** `django-cleanup`, `requests`, `pytz`

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

*   Python 3.8 or higher
*   Git

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/taggar-blog.git
    cd taggar-blog
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv env
    # Windows
    .\env\Scripts\activate
    # macOS/Linux
    source env/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r taggar/requirments.txt
    ```

4.  **Set up Environment Variables**
    Create a `.env` file or set the following environment variables in your system:
    *   `SECRET_KEY`: Your Django secret key
    *   `DEBUG`: `True` or `False`
    *   `DB_ENGINE`: `django.db.backends.sqlite3` (or other)
    *   `DB_NAME`: Database name
    *   `DB_USER`: Database user
    *   `DB_PASSWORD`: Database password
    *   `EMAIL_HOST_USER`: Your email address
    *   `EMAIL_HOST_PASSWORD`: Your email password

5.  **Run Migrations**
    ```bash
    cd taggar
    python manage.py migrate
    ```

6.  **Create a Superuser**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000` to view the site.

## 📸 Screenshots

*(Add screenshots of your application here)*

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
