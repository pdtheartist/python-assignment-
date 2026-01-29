attempts = 0
while attempts < 5:
    user = input("Username: ")
    pwd = input("Password: ")
    if user == "python" and pwd == "rules":
        print("Welcome")
        break
    attempts += 1
    if attempts == 5:
        print("Access denied")