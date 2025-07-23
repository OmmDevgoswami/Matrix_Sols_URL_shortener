# 🔗 URL Shortener (Django-based)

A simple and efficient URL shortener built using Django. This project allows users to input long URLs and receive shortened versions that can be used for redirection.

---

## Features

- Shorten long URLs into unique short codes
- Redirect to original URLs when short URL is accessed
- Track created URLs
- Admin dashboard for full control 
- Responsive frontend with Bootstrap

---
## To Run the File

```bash
cd url-shortener
python manage.py runserver
```

- Paste your long-url
- Copy the new short-url generated

- To Access admin-dashbaord (USER: "admineUser" Password: "pass4321")

Code Structure:
```
url-shortener/
│
├── shortener/             
│   ├── migrations/
│   ├── templates/
│   │   └── shortener/    
│   ├── static/
│   │   └── shortener/    
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── urlshortener/     
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3
└──  manage.py
```
