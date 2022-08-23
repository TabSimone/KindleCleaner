
# C:\Users\taban\OneDrive\Documents\Amazon.txt


# path = input("Enter your value: ")

# phrase = input("Enter your value: ")

with  open(r'C:\Users\SEDD\Downloads\Tribe.txt', encoding="mbcs") as f:
    lines = f.readlines()



with open(r'C:\Users\SEDD\Downloads\Tribe.txt', 'w', encoding="mbcs") as f:
    for line in lines:
       if line.strip("\n") == "La tua evidenziazione alla posizione":
            f.write(line)
