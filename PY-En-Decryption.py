def encrypt(filename, key):
    file = open(filename, "rb")
    data = (file.read())
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open("EF- " + filename, "wb")
    file.write(data)
    file.close()


def decrypt(filename, key):
    file = open(filename, "rb")
    data = (file.read())
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open("DF- " + filename, "wb")
    file.write(data)
    file.close()


choice = ""
while choice != "3":
    print("Please select you option")
    print("1 - Encrypt File")
    print("2 - Decrypt File")
    print("3 - Quit")
    print("")
    choice = input("choice: ")
    if choice == "1" or choice == "2":
        key = int(input("Ask for a key between 1 - 255: "))
        filename = input("Please enter a filename with extension: ")
    if choice == "1":
        encrypt(filename, key)
    if choice == "2":
        decrypt(filename, key)