import tkinter as tk
import subprocess

# Function to run a Python file
def run_python_file(file_path):
    subprocess.Popen(["python", file_path])

# Function to run all three Python files
def run_all_files():
    run_python_file("unzip.py")
    run_python_file("rename.py")
    run_python_file("color adjust with document create.py")

# Create the main application window
app = tk.Tk()
app.title("Run Python Files")

# Create a button to run the files
run_button = tk.Button(app, text="Run Files", command=run_all_files)
run_button.pack()

# Start the GUI application
app.mainloop()
