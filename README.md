# FastAPI Hexagonal Architecture Project

This project is a FastAPI application designed with Hexagonal Architecture (Ports and Adapters). It demonstrates the separation of concerns, making the application more maintainable, testable, and scalable.

## Table of Contents

- [FastAPI Hexagonal Architecture Project](#fastapi-hexagonal-architecture-project)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Migrations with Alembic](#database-migrations-with-alembic)
- [Endpoints](#endpoints)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/j-e-0/scaffold-hexagonal-pattern-py
    cd scaffold-hexagonal-pattern-py
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your environment variables (if needed).

## Usage

1. Start the application:

    ```bash
    uvicorn app.main:app --reload
    ```

2. The API will be running at `http://localhost:8000`.

## Project Structure

```
project/
├── alembic/
│   ├── versions/
│   │   └── some_unique_id_initial_migration.py
│   ├── env.py
│   ├── script.py.mako
│   └── __init__.py
├── alembic.ini
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── user_router.py
│   │   │   ├── user_controller.py
│   │   │   ├── product_router.py
│   │   │   ├── product_controller.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   └── __init__.py
│   ├── main.py
│   └── __init__.py
├── domain/
│   ├── abstracts/
│   │   ├── user.py
│   │   ├── product.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── product.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   └── __init__.py
├── infrastructure/
│   ├── db/
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── product.py
│   │   │   └── __init__.py
│   │   ├── database.py
│   │   ├── user_repository.py
│   │   ├── product_repository.py
│   │   └── __init__.py
├── tests/
│   ├── test_user.py
│   ├── test_product.py
│   ├── __init__.py
├── .env
├── requirements.txt
└── README.md
```

### Description

- **app/**: Application layer containing API routes and main configuration.
  - **api/**: API routes and controllers.
  - **core/**: Main application configurations.
  - **main.py**: Application entry point.

- **domain/**: Domain layer containing business logic.
  - **abstracts/**: Domain abstracts representing communication and inverse responsabilities.
  - **schemas/**: Domain Schemas for data validation.
  - **services/**: Domain services containing business logic.

- **infrastructure/**: Infrastructure layer containing database interactions.
  - **db/**: Database configuration and repository implementations.
    - **models/**: Databse models representing business entities.

- **tests/**: Test files for unit and integration tests.

## Database Migrations with Alembic

### 1. Install Alembic

If not already installed, add Alembic to your `requirements.txt` and install the dependencies:

```bash
alembic
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 2. Apply the Migration

Apply the migration to create the tables in the database:

```bash
alembic upgrade head
```

## Endpoints

### User Endpoints

- **POST /users/**: Create a new user
  - Request Body:

    ```json
    {
      "username": "john",
      "email": "john@example.com",
      "password": "password"
    }
    ```

- **GET /users/{user_id}**: Get a user by ID

### Product Endpoints

- **POST /products/**: Create a new product
  - Request Body:

    ```json
    {
      "name": "Product1",
      "price": 100.0
    }
    ```

- **GET /products/{product_id}**: Get a product by ID

## Running Tests

1. To run the tests, use the following command:

    ```bash
    pytest
    ```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
