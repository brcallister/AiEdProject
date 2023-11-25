import os
try:
    import openai
except ImportError:
    print("openai is not correctly installed. Run 'pip install openai' and try again.")
from src import Generate

original_wd = os.getcwd()

# Set the current working directory to the script directory
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except Exception:
    pass

# Run the actual program
if __name__ == "__main__":
    Generate.Start()

# Switch back to original working directory if possible
try:
    os.chdir(original_wd)
except Exception:
    pass
