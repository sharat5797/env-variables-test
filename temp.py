# get_email.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the email variable
email = os.getenv("EMAIL")

if email:
    print(f"Email from .env: {email}")
else:
    print("Email not found in .env")
