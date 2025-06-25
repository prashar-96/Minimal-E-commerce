# 🛒 Minimal-E-commerce

A minimal e-commerce backend built with Django and Django REST Framework.

## 🚀 Features

- JWT Authentication (Register/Login)
- Product Listing & Detail APIs
- Cart Management
- Order Creation & Tracking

## 🛠️ Project Structure

- `users/` - User auth and profile
- `products/` - Product APIs
- `cart/` - Shopping cart logic
- `orders/` - Order creation

## 🧰 Tech Stack

- Python 3
- Django
- DRF (Django REST Framework)
- SQLite3
- JWT (SimpleJWT)

## ▶️ How to Run Locally

```bash
git clone https://github.com/prashar-96/Minimal-E-commerce.git
cd Minimal-E-commerce
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
