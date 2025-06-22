import os
import psycopg2
from sqlalchemy import text
import pandas as pd
from db.connect import get_engine

def validate_database_connection():
    """
    Validate database connection using the existing connect.py module
    """
    try:
        # Check if all required environment variables are set
        required_vars = ['DB_USER', 'DB_PASS', 'DB_NAME']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
            print("Please check your .env file and ensure all required variables are set.")
            return False
        
        # Test connection using the existing get_engine function
        print("🔍 Testing database connection with existing connect.py...")
        engine = get_engine()
        
        with engine.connect() as connection:
            result = connection.execute(text("SELECT current_database(), current_user, version();"))
            row = result.fetchone()
            print(f"✅ Database connection successful!")
            print(f"   Database: {row[0]}")
            print(f"   User: {row[1]}")
            print(f"   Version: {row[2]}")
        
        print("\n🎉 Database connection validated successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def test_data_operations():
    """
    Test basic data operations with pandas and SQLAlchemy
    """
    try:
        engine = get_engine()
        
        print("\n🔍 Testing data operations...")
        
        # Test reading data (assuming you have a table)
        # You can modify this query based on your actual table structure
        query = "SELECT * FROM information_schema.tables WHERE table_schema = 'public' LIMIT 5;"
        df = pd.read_sql(query, engine)
        
        print(f"✅ Data operations successful!")
        print(f"   Found {len(df)} tables in public schema")
        if not df.empty:
            print(f"   Sample tables: {', '.join(df['table_name'].tolist())}")
        
        return True
        
    except Exception as e:
        print(f"❌ Data operations failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting database connection validation...\n")
    
    # Validate connection
    connection_valid = validate_database_connection()
    
    if connection_valid:
        # Test data operations
        data_ops_valid = test_data_operations()
        
        if data_ops_valid:
            print("\n🎯 All validations passed! Your database is ready for forecasting operations.")
        else:
            print("\n⚠️  Connection works but data operations need attention.")
    else:
        print("\n❌ Database connection validation failed. Please check your configuration.")
