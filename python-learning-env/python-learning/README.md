# Python Learning Environment with uv

A comprehensive Python learning environment set up with [uv](https://docs.astral.sh/uv/) for dependency management and script execution.

## =Ú What's Included

### 1. Jupyter Notebook
- **`python_basics.ipynb`**: A comprehensive notebook covering all Python basics
  - Variables & Data Types
  - Control Flow (if/else, loops)
  - Functions & Lambda expressions
  - Data Structures (lists, dicts, sets, tuples)
  - String Operations
  - File Handling (text, CSV, JSON)
  - Error Handling
  - Object-Oriented Programming
  - Modules & Packages
  - List Comprehensions & Generators
  - Decorators
  - Built-in Functions
  - Best Practices & Tips

### 2. Standalone Python Scripts
All scripts are configured with uv's standalone script format for easy execution:

#### `scripts/hello_world.py`
- Basic Python script demonstrating input/output
- Shows string manipulation and error handling
- **Dependencies**: None

#### `scripts/file_operations.py` 
- File reading, writing, and analysis
- JSON file handling
- File statistics and cleanup
- **Dependencies**: None

#### `scripts/calculator.py`
- Interactive calculator with scientific functions
- Demonstrates classes, error handling, and user interaction
- Calculation history and advanced math operations
- **Dependencies**: None

#### `scripts/data_analysis.py`
- Data analysis with pandas and visualization with matplotlib
- Sample data generation and statistical analysis
- Charts and graphs creation
- **Dependencies**: `pandas`, `matplotlib`

#### `scripts/web_scraper.py`
- Ethical web scraping demonstration
- HTML parsing and data extraction
- Respects rate limits and robots.txt
- **Dependencies**: `requests`, `beautifulsoup4`

## =€ Getting Started

### Prerequisites
- [uv](https://docs.astral.sh/uv/) installed on your system
- Python 3.8 or higher

### Running the Jupyter Notebook
```bash
# Navigate to the project directory
cd python-learning

# Start Jupyter notebook
uv run jupyter notebook python_basics.ipynb
```

### Running Individual Scripts

Each script can be run directly with uv, which will automatically handle dependencies:

```bash
# Basic hello world script
uv run scripts/hello_world.py

# File operations demo
uv run scripts/file_operations.py

# Interactive calculator
uv run scripts/calculator.py

# Data analysis with charts (installs pandas & matplotlib automatically)
uv run scripts/data_analysis.py

# Web scraping demo (installs requests & beautifulsoup4 automatically)
uv run scripts/web_scraper.py
```

### Making Scripts Executable (Optional)

You can make any script executable and run it directly:

```bash
# Make executable
chmod +x scripts/hello_world.py

# Run directly
./scripts/hello_world.py
```

## =' uv Script Format

All scripts use uv's inline script metadata format:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "requests",
#   "pandas",
# ]
# ///
```

This format allows uv to:
- Automatically create isolated environments
- Install dependencies on-demand
- Ensure consistent Python versions
- Make scripts portable and self-contained

## =Ö Learning Path

1. **Start with the Jupyter Notebook**: `python_basics.ipynb` covers all fundamental concepts with interactive examples

2. **Try the Basic Scripts**:
   - `hello_world.py` - Get comfortable with basic Python
   - `file_operations.py` - Learn file handling
   - `calculator.py` - Practice with classes and functions

3. **Explore Advanced Scripts**:
   - `data_analysis.py` - Data science with pandas/matplotlib
   - `web_scraper.py` - Web scraping with requests/beautifulsoup

4. **Experiment**: Modify the scripts and create your own variations

## =à Development

### Adding New Scripts

Create new scripts with the uv format:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "your-dependency",
# ]
# ///

# Your code here
```

### Installing Additional Dependencies

Add dependencies to the main project:

```bash
uv add numpy scipy matplotlib seaborn
```

## =Ý Notes

- All scripts are designed to be educational and demonstrate best practices
- Dependencies are automatically managed by uv
- Scripts are self-contained and portable
- The web scraper includes ethical guidelines and rate limiting
- All examples include comprehensive error handling

## > Contributing

Feel free to:
- Add more example scripts
- Improve existing examples
- Add new sections to the Jupyter notebook
- Share your own learning projects

Happy coding with Python and uv! =