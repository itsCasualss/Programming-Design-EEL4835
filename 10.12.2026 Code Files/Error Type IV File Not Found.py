try:
    with open("nofile.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found! Creating a new one.")
    with open("nofile.txt", "w") as file:
        file.write("This is a new file.")
