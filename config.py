import os
from dotenv import load_dotenv
load_dotenv()
password = os.environ.get('PASSWORD')
print(password)
class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres.falrgbbdeqynhfgxlywx:{password}@aws-0-us-west-1.pooler.supabase.com:6543/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False