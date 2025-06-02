import requests
url = "http://127.0.0.1:5000/api/v1/books"

# Delete first 5 IDs
for i in range(0, 5):
    response = requests.delete(f"{url}/{i}")
    print(f"Deleted book id: {i}, status code: {response.status_code}")

# Delete last 5 IDs
for i in range(40, 45):
    response = requests.delete(f"{url}/{i}")
    print(f"Deleted book id: {i}, status code: {response.status_code}")

