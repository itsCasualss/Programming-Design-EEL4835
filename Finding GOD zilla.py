sentence = input("Enter a sentence: ")

location = sentence.find("Godzilla")

if location != -1:
    print("Starting index:", location)
else:
    print("Godzilla escaped!")