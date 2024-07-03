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
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
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
│   ├── models/
│   │   ├── user.py
│   │   ├── product.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   └── __init__.py
├── infrastructure/
│   ├── db/
│   │   ├── database.py
│   │   ├── user_repository.py
│   │   ├── product_repository.py
│   │   └── __init__.py
├── schemas/
│   ├── user.py
│   ├── product.py
│   └── __init__.py
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
  - **models/**: Domain models representing business entities.
  - **services/**: Domain services containing business logic.

- **infrastructure/**: Infrastructure layer containing database interactions.
  - **db/**: Database configuration and repository implementations.

- **schemas/**: Schemas for data validation.

- **tests/**: Test files for unit and integration tests.

## Database Migrations with Alembic

### 1. Install Alembic

If not already installed, add Alembic to your `requirements.txt` and install the dependencies:

```
alembic
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 2. Initialize Alembic

Initialize Alembic in your project:

```bash
alembic init alembic
```

This will create an `alembic` directory and an `alembic.ini` file at the root of your project.

### 3. Configure `alembic.ini`

Edit the `alembic.ini` file to point to your database connection string. Replace the `sqlalchemy.url` line with your database URL, like so:

```ini
sqlalchemy.url = sqlite:///./test.db
```

### 4. Configure `env.py`

Edit the `alembic/env.py` file to include your database models. Replace the contents of `env.py` with the following:

```python
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Import the models
from infrastructure.db.database import Base
from domain.models.user import User
from domain.models.product import Product

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

### 5. Create an Initial Migration

Create an initial migration to add the `users` and `products` tables:

```bash
alembic revision --autogenerate -m "Initial migration"
```

This will create a migration file in `alembic/versions` with a unique name. Edit the generated file to ensure the tables are correct. It should look something like this:

```python
"""Initial migration

Revision ID: some_unique_id
Revises: 
Create Date: 2023-10-10 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'some_unique_id'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('users')
    # ### end Alembic commands ###
```

### 6. Apply the Migration

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

## License

This project is licensed under the MIT License.
