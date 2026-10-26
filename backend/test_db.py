import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

database_url=os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError("DATABASE_URL environment variable is not set.")

engine = create_engine(database_url, pool_pre_ping=True)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version(), current_database()"))
        version, database = result.one()
        print("Database connection successful.")
        print(f"Database: {database}")
        print(f"PostgreSQL Version: {version}")
except Exception as e:
    print(f"Database connection failed: {e}")
finally:
    engine.dispose()