from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.logger.logger import logger  # Adjust import as needed

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {e}")
        raise
    finally:
        db.close()

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        # Verify DB connection
        db_gen = get_db()
        db = next(db_gen)
        logger.info("Database connection established successfully.")
        db_gen.close()
        logger.info("Database tables created successfully.")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        raise