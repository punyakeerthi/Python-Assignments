import sys

def find_python_path():
    python_path = sys.executable
    return python_path

if __name__ == "__main__":
    python_path = find_python_path()
    print("Python is installed at:", python_path)
