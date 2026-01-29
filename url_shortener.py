# python-url-shortener
import random
import string

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(long_url):
    code = generate_code()
    with open("urls.txt", "a") as file:
        file.write(f"{code},{long_url}\n")
    return code

def retrieve_url(code):
    with open("urls.txt", "r") as file:
        for line in file:
            saved_code, saved_url = line.strip().split(",")
            if saved_code == code:
                return saved_url
    return "URL not found"

while True:
    print("\n1. Shorten URL")
    print("2. Retrieve URL")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        long_url = input("Enter long URL: ")
        short_code = shorten_url(long_url)
        print("Short URL code:", short_code)

    elif choice == "2":
        code = input("Enter short URL code: ")
        print("Original URL:", retrieve_url(code))

    elif choice == "3":
        break
