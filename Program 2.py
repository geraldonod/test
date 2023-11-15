import random

name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")

print("Name:", name)
print("Age:", age)
print("Address:", address)

trivia_facts = [
"Did you know? The Python programming language is older than Java",
"Did you know? Python is one of the programming languages that are used at Google",
"Did you know? Python was started as a hobby project."
]

random_fact = random.choice(trivia_facts)

print("Here's a random trivia fact for you:")
print(random_fact)