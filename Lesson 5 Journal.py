import datetime as dt
print("--Journal App--")

while True:
    print("Choose an option:")
    print("1. Add/Write an entry")
    print("2. View all entries")
    print("3. Clear all entries")
    print("4. Search for entries by keyword")
    print("5. Exit")
    x = int(input("Enter your choice (1-4): "))
    if x == 1:
        y = str(input("New entry: "))
        with open("Journal.txt", "a") as z:
            z.write("[{}]{}\n".format(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),y))
    elif x == 2:
        with open("Journal.txt", "r") as z:
            print(z.read())
    elif x == 3:
        with open("Journal.txt", "w") as z:
            z.write(" ")
    elif x == 4:
        word = input("Enter the keyword: ")
        with open("Journal.txt", "r") as file:
            x = file.readlines()
            for each_line in x:
                if word.lower() in each_line.lower():
                    print("The keyword is present in the line - ", each_line)
    elif x == 5:
        break
