#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///

"""
A simple Hello World script using uv standalone script format.
This demonstrates the basic structure for Python scripts with uv.
"""

def main():
    """Main function that prints a greeting."""
    name = input("What's your name? ")
    print(f"Hello, {name}! Welcome to Python programming with uv!")
    
    # Show some basic Python concepts
    print("\nHere are some Python basics:")
    print(f"Your name has {len(name)} characters")
    print(f"In uppercase: {name.upper()}")
    print(f"In title case: {name.title()}")
    
    # Simple calculation
    age = input("What's your age? ")
    try:
        age = int(age)
        next_year = age + 1
        print(f"Next year you'll be {next_year} years old!")
    except ValueError:
        print("Please enter a valid number for age next time!")

if __name__ == "__main__":
    main()