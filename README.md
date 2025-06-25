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

## 📡 API Endpoints

Here are the main REST API endpoints available in this project:

### 🔐 Authentication

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| POST   | /auth/register/  | Register new user   |
| POST   | /auth/login/     | Login user (JWT)    |
| GET    | /auth/profile/   | Get user profile    |

### 🛍️ Products

| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| GET    | /products/         | List all products   |
| GET    | /products/<id>/    | Product details     |

### 🛒 Cart

| Method | Endpoint           | Description            |
|--------|--------------------|------------------------|
| POST   | /cart/add/         | Add product to cart    |
| GET    | /cart/             | View cart items        |
| DELETE | /cart/remove/<id>/ | Remove product from cart |

### 📦 Orders

| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| POST   | /orders/create/    | Create new order    |
| GET    | /orders/           | List user orders    |

---

### 📚 API Documentation & Admin Panel

| Name           | URL                 | Description                       |
|----------------|----------------------|-----------------------------------|
| 🔧 Swagger UI   | `/swagger/`          | Interactive API documentation     |
| 📘 ReDoc        | `/redoc/`            | Clean, readable API docs          |
| 🔐 Admin Panel  | `/admin/`            | Django admin dashboard            |

