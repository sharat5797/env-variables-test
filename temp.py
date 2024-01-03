# temp.py
import os

email = os.getenv("EMAIL", "default_value_if_not_set")
print(f"Email from env: {email}")
