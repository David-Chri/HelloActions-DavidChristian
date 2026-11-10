import os


class Hello:
    def __init__(self, who_to_greet):
        self.who_to_greet = "GitHub Actions Student"

    def greet(self):
        print(f"Hello, {self.who_to_greet}!")
        print("This program is running inside GitHub Actions.")

if __name__ == "__main__":
    Hello(os.getenv("WHO_TO_GREET")).greet()
