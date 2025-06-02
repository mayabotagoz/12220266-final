import requests
import random

# Prepare API endpoint
url = "http://127.0.0.1:5000/api/v1/books"

# Generate 25 random books with ISBN
for i in range(20, 45):  # IDs 20-44 (just avoid conflict with earlier books)
    isbn = f"{random.randint(1000000000000, 9999999999999)}"
    payload = {
        "id": i,
        "title": f"Random Book {i}",
        "author": f"Author {i}",
        "isbn": isbn
    }
    response = requests.post(url, json=payload)
    print(response.json())

