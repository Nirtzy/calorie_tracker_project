# Calorie Tracker Project

A Django-based web application for searching food nutrition data, building meals, and calculating total calories and macronutrients. Includes a visual portion size guide and dynamic food search features.

## Features
- Search for food items and view nutrition facts in a table
- Build your meal by selecting foods and quantities
- Calculate total calories, protein, fat, carbs, and fiber for your meal
- Visual portion size guide (bowl, plate, tablespoon, handful)
- User authentication (login/register/logout)
- Responsive Bootstrap UI

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/calorie_tracker_project.git
cd calorie_tracker_project
```

### 2. Install dependencies
```bash
python -m venv venv
source venv/bin/activate
pip install django
```

### 3. Database migration
```bash
python manage.py migrate
```

### 4. Create superuser (optional)
```bash
python manage.py createsuperuser
```

### 5. Run the development server
```bash
python manage.py runserver
```

### 6. Access the app
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Static Files
- Place your portion size images (bowl.jpg, plate.jpg, tablespoon.jpg, handful.jpg) in `foods/static/foods/`.

## Project Structure
- `foods/` - Main app with models, views, templates, and static files
- `config/` - Django project settings and URLs
- `db.sqlite3` - SQLite database
- `data/` - Food nutrition datasets

## Customization
- Update food images in `foods/static/foods/`
- Add more food items via Django admin or by updating the database

## License
MIT

---

**Developed by Nirtzy**

