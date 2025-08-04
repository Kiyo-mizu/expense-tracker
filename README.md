# Expense Tracker

A Django web application for tracking personal expenses.

## Features

- Add, edit, and delete expenses
- Categorize expenses
- View expense history
- Simple and intuitive interface

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment to Render

### Prerequisites

1. A Render account
2. Your code pushed to a Git repository (GitHub, GitLab, etc.)

### Deployment Steps

1. **Connect your repository to Render:**
   - Go to your Render dashboard
   - Click "New +" and select "Web Service"
   - Connect your Git repository

2. **Configure the service:**
   - **Name:** expense-tracker (or your preferred name)
   - **Environment:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn expense_tracker.wsgi:application`

3. **Set Environment Variables:**
   - `SECRET_KEY`: Generate a secure Django secret key
   - `DEBUG`: Set to `False` for production
   - `ALLOWED_HOSTS`: Set to your Render app URL (e.g., `your-app-name.onrender.com`)
   - `DATABASE_URL`: Render will automatically provide this if you add a PostgreSQL database

4. **Add a PostgreSQL Database (Recommended):**
   - In your Render dashboard, create a new PostgreSQL database
   - Connect it to your web service
   - Render will automatically set the `DATABASE_URL` environment variable

5. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

### Environment Variables

Create a `.env` file locally (not committed to Git) with:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
DATABASE_URL=sqlite:///db.sqlite3
```

### Important Notes

- The application uses SQLite for local development and PostgreSQL for production
- Static files are served using WhiteNoise
- The application is configured for production security settings
- Make sure to run `python manage.py migrate` after deployment if using a new database

## Project Structure

```
expense-tracker/
├── expense_tracker/          # Django project settings
├── tracker/                  # Main app
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── urls.py              # URL routing
│   └── templates/           # HTML templates
├── requirements.txt          # Python dependencies
├── render.yaml              # Render deployment config
├── build.sh                 # Build script
└── Procfile                 # Process file for Render
``` 