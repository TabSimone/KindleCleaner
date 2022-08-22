
# C:\Users\taban\OneDrive\Documents\Amazon.txt


# path = input("Enter your value: ")

# phrase = input("Enter your value: ")

with  open(r'C:\Users\taban\OneDrive\Documents\Amazon.txt') as f:
    lines = f.readlines()

with open(r'C:\Users\taban\OneDrive\Documents\Amazon.txt') as f:
    for line in lines:
        if line.strip("\n") != "La tua evidenziazione alla posizione":
            f.write(line)


