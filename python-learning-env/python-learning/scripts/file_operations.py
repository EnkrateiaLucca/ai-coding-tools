#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = []
# ///

"""
File operations demonstration using uv standalone script format.
This script shows how to work with files in Python.
"""

import os
import json
from datetime import datetime

def create_sample_file():
    """Create a sample text file with some content."""
    filename = "sample.txt"
    content = """This is a sample file created with Python!
Date created: {}
Python is a powerful programming language.
File handling is essential for many applications.""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    with open(filename, 'w') as file:
        file.write(content)
    
    print(f"✓ Created {filename}")
    return filename

def read_and_display_file(filename):
    """Read and display file contents."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        print(f"\n📄 Contents of {filename}:")
        print("-" * 40)
        print(content)
        print("-" * 40)
        
    except FileNotFoundError:
        print(f"❌ File {filename} not found!")

def analyze_file(filename):
    """Analyze file statistics."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        file_stats = {
            'filename': filename,
            'size_bytes': os.path.getsize(filename),
            'line_count': len(lines),
            'word_count': sum(len(line.split()) for line in lines),
            'char_count': sum(len(line) for line in lines)
        }
        
        print(f"\n📊 File Analysis for {filename}:")
        for key, value in file_stats.items():
            if key != 'filename':
                print(f"  {key.replace('_', ' ').title()}: {value}")
        
        return file_stats
        
    except FileNotFoundError:
        print(f"❌ Cannot analyze {filename} - file not found!")
        return None

def save_analysis_to_json(analysis_data):
    """Save analysis data to JSON file."""
    if analysis_data:
        json_filename = "file_analysis.json"
        with open(json_filename, 'w') as json_file:
            json.dump(analysis_data, json_file, indent=2)
        print(f"✓ Analysis saved to {json_filename}")

def main():
    """Main function demonstrating file operations."""
    print("🔧 File Operations Demo")
    print("=" * 30)
    
    # Create a sample file
    filename = create_sample_file()
    
    # Read and display the file
    read_and_display_file(filename)
    
    # Analyze the file
    stats = analyze_file(filename)
    
    # Save analysis to JSON
    save_analysis_to_json(stats)
    
    # Clean up option
    cleanup = input("\n🗑️  Delete created files? (y/n): ").lower()
    if cleanup == 'y':
        try:
            os.remove(filename)
            os.remove("file_analysis.json")
            print("✓ Files cleaned up!")
        except FileNotFoundError:
            print("Files already removed or not found.")
    else:
        print("Files kept for your review.")

if __name__ == "__main__":
    main()