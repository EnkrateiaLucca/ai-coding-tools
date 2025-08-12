#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///

"""
Interactive calculator demonstrating Python basics.
This script showcases functions, error handling, and user interaction.
"""

import math
import sys

class Calculator:
    """A simple calculator class demonstrating OOP concepts."""
    
    def __init__(self):
        self.history = []
        self.last_result = 0
    
    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        self.log_operation(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers."""
        result = a - b
        self.log_operation(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        self.log_operation(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.log_operation(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, a, b):
        """Raise a to the power of b."""
        result = a ** b
        self.log_operation(f"{a}^{b} = {result}")
        return result
    
    def sqrt(self, a):
        """Calculate square root."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(a)
        self.log_operation(f"√{a} = {result}")
        return result
    
    def log_operation(self, operation):
        """Log the operation to history."""
        self.history.append(operation)
        if len(self.history) > 50:  # Keep only last 50 operations
            self.history.pop(0)
    
    def show_history(self):
        """Display calculation history."""
        if not self.history:
            print("No calculations performed yet.")
        else:
            print("\n📊 Calculation History:")
            print("-" * 30)
            for i, operation in enumerate(self.history[-10:], 1):  # Show last 10
                print(f"{i:2d}. {operation}")
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
        print("✅ History cleared!")

def get_number(prompt):
    """Get a number from user with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")

def get_menu_choice():
    """Display menu and get user choice."""
    print("\n🧮 Calculator Menu:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (×)")
    print("4. Divide (÷)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Show History")
    print("8. Clear History")
    print("9. Exit")
    
    while True:
        try:
            choice = int(input("\nSelect operation (1-9): "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("❌ Please enter a number between 1 and 9!")
        except ValueError:
            print("❌ Please enter a valid number!")

def perform_calculation(calc, choice):
    """Perform the selected calculation."""
    try:
        if choice in [1, 2, 3, 4, 5]:  # Two-number operations
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            
            if choice == 1:
                result = calc.add(a, b)
            elif choice == 2:
                result = calc.subtract(a, b)
            elif choice == 3:
                result = calc.multiply(a, b)
            elif choice == 4:
                result = calc.divide(a, b)
            elif choice == 5:
                result = calc.power(a, b)
            
            print(f"✅ Result: {result}")
            calc.last_result = result
            
        elif choice == 6:  # Square root
            a = get_number("Enter number: ")
            result = calc.sqrt(a)
            print(f"✅ Result: {result}")
            calc.last_result = result
            
        elif choice == 7:  # Show history
            calc.show_history()
            
        elif choice == 8:  # Clear history
            calc.clear_history()
            
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def scientific_mode(calc):
    """Extended scientific calculator functions."""
    print("\n🔬 Scientific Mode")
    print("Available functions:")
    print("sin, cos, tan, log, ln, exp, ceil, floor")
    
    function = input("Enter function name (or 'back' to return): ").lower().strip()
    
    if function == 'back':
        return
    
    try:
        if function in ['sin', 'cos', 'tan']:
            angle = get_number(f"Enter angle in degrees for {function}: ")
            radians = math.radians(angle)
            
            if function == 'sin':
                result = math.sin(radians)
            elif function == 'cos':
                result = math.cos(radians)
            elif function == 'tan':
                result = math.tan(radians)
            
            calc.log_operation(f"{function}({angle}°) = {result}")
            print(f"✅ {function}({angle}°) = {result}")
            
        elif function == 'log':
            num = get_number("Enter number for log10: ")
            if num <= 0:
                print("❌ Logarithm undefined for non-positive numbers!")
                return
            result = math.log10(num)
            calc.log_operation(f"log({num}) = {result}")
            print(f"✅ log({num}) = {result}")
            
        elif function == 'ln':
            num = get_number("Enter number for natural log: ")
            if num <= 0:
                print("❌ Natural logarithm undefined for non-positive numbers!")
                return
            result = math.log(num)
            calc.log_operation(f"ln({num}) = {result}")
            print(f"✅ ln({num}) = {result}")
            
        elif function == 'exp':
            num = get_number("Enter exponent for e^x: ")
            result = math.exp(num)
            calc.log_operation(f"e^{num} = {result}")
            print(f"✅ e^{num} = {result}")
            
        elif function in ['ceil', 'floor']:
            num = get_number(f"Enter number for {function}: ")
            if function == 'ceil':
                result = math.ceil(num)
            else:
                result = math.floor(num)
            calc.log_operation(f"{function}({num}) = {result}")
            print(f"✅ {function}({num}) = {result}")
            
        else:
            print("❌ Unknown function! Available: sin, cos, tan, log, ln, exp, ceil, floor")
            
    except Exception as e:
        print(f"❌ Error in scientific calculation: {e}")

def main():
    """Main calculator program."""
    print("🧮 Python Calculator")
    print("=" * 30)
    print("Welcome to the interactive Python calculator!")
    print("This demonstrates functions, classes, and error handling.")
    
    calc = Calculator()
    
    while True:
        try:
            choice = get_menu_choice()
            
            if choice == 9:  # Exit
                print("\n👋 Thanks for using the calculator!")
                if calc.history:
                    print(f"You performed {len(calc.history)} calculations.")
                break
            
            perform_calculation(calc, choice)
            
            # Offer scientific mode
            if choice in [1, 2, 3, 4, 5, 6]:
                sci_mode = input("\nWould you like to use scientific mode? (y/n): ").lower()
                if sci_mode == 'y':
                    scientific_mode(calc)
            
        except KeyboardInterrupt:
            print("\n\n👋 Calculator interrupted by user. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()