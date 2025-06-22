import pandas as pd
from db.connect import get_engine

# Create engine
engine = get_engine()

# Load data
df = pd.read_sql("SELECT * FROM superstore;", con=engine)

print(f"✅ Data loaded successfully!")
print(f"📊 Shape: {df.shape}")
print(f"📋 Columns: {list(df.columns)}")
print(f"\n🔍 First 5 rows:")
print(df.head()) 