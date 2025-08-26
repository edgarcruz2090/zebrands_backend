# Zebrands Backend Test

Backend test for ZeBrands. API for managing a product catalog including roles for admins and anonymous users with notifications and usage tracking.

## Overview

- **Product Management**: Complete CRUD operations for products with SKU, name, price, and brand
- **User Management**: Admin users can manage other users, brands, and products
- **Anonymous Access**: Public endpoints for listing and retrieving product information
- **Tracking System**: Automatic tracking of product views by anonymous users
- **Email Notifications**: Admin users receive email notifications when products are updated
- **JWT Authentication**: Secure API access with JWT tokens
- **API Documentation**: Auto-generated Swagger/OpenAPI documentation

## Project Structure

```
zebrands/
├── apps/
│   ├── authentication/     # JWT authentication
│   ├── products/          # Product and brand management
│   └── users/             # User management
├── zebrands_catalog/      # Main project settings
├── fixtures/              # Sample data
└── manage.py
```

## Prerequisites

- Docker and Docker Compose
- Python 3.12.3


## Run project
1. Copy the `.env.example` to `.env`
```
cp .env.example .env
```
Update variable values
~~~
SES_AWS_ACCESS_KEY=1231313 #Your AWS Access Key
SES_AWS_SECRET_KEY=123123 #Your AWS Secrete Key
SES_AWS_REGION=us-east-1
SES_AWS_SOURCE=email@example.com #Your email verified in AWS SES
~~~
**Note: Do not forget to move your user from the SES sandbox to test with several emails as recipients without the need to verify them**

2. You can use `Make` to build the image and create the first super user:

```bash
# Build the Docker image
make docker-build

# Start the container in background
make docker-start

# Create a superuser
make docker-superuser

# Access container bash (if needed)
make docker-bash
```

### 3. Access the Application

- **Health Check**: http://localhost:8001/
- **Admin Panel**: http://localhost:8001/admin
- **API Documentation**: http://localhost:8001/docs

## Available Make Commands

### Docker Commands
```bash
make docker-build      # Build Docker image
make docker-build-nc   # Build without cache
make docker-start      # Start container in background
make docker-stop       # Stop container
make docker-rebuild    # Rebuild and start
make docker-bash       # Access container bash
make docker-shell      # Django shell in container
make docker-superuser  # Create superuser
make docker-loaddata   # Load sample data
```

### Local Development Commands
```bash
make install           # Install dependencies
make migrate           # Create migrations
make migrate-apply     # Apply migrations
make migrate-reset     # Reset database
make superuser         # Create superuser
make load-fixtures     # Load sample data
make run               # Run development server
make test              # Run tests
make format            # Format code with Black
make clean             # Clean cache files
```

## API Endpoints

### Public Endpoints (No Authentication Required)
- `GET /api/v1/products/` - List all products
- `GET /api/v1/products/{id}/` - Retrieve product details
- `GET /api/v1/brands/` - List all brands
- `GET /api/v1/brands/{id}/` - Retrieve brand details

### Protected Endpoints (JWT Authentication Required)
- `POST /api/v1/products/` - Create product
- `PUT /api/v1/products/{id}/` - Update product
- `DELETE /api/v1/products/{id}/` - Delete product
- `POST /api/v1/brands/` - Create brand
- `PUT /api/v1/brands/{id}/` - Update brand
- `DELETE /api/v1/brands/{id}/` - Delete brand
- `POST /api/v1/users/` - Create user
- `PUT /api/v1/users/{id}/` - Update user
- `DELETE /api/v1/users/{id}/` - Delete user

### Authentication Endpoints
- `POST /api/auth/login/` - Get JWT token
- `POST /api/auth/refresh/` - Refresh JWT token

## Authentication

All protected endpoints require JWT authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

To get a token:
1. Use the `/api/auth/login/` endpoint
2. Include the token in subsequent requests with `Bearer` prefix


## Postman collections
You can use the [Postman collection](Postman) for test