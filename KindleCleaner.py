import tkinter as tk
from tkinter import filedialog

# No comment if you want to change default phrase
# phrase = input("Enter phrase: ")
phrase = "tua evidenziazione"

# This opens up file finder
root = tk.Tk()
root.withdraw()
path = filedialog.askopenfilename()

# Open file in python and read it
with open(path, encoding="mbcs") as f:
    lines = f.readlines()

# Process lines, removing every line that is '==========' and the three lines after it
filtered_lines = []
i = 0
while i < len(lines):
    if lines[i].strip() == "==========":
        i += 4  # Skip this line and the next three
    else:
        filtered_lines.append(lines[i])
        i += 1

# Write the filtered content back to the file
with open(path, "w", encoding="mbcs") as f:
    f.writelines(filtered_lines)

print("Processing complete. The file has been updated.")
