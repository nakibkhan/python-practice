from Exercises.PasswordGenerator import password_generator

if __name__ == "__main__":

    print("Entering Password Generator")
    passwordLen = int(input("Please enter the length you would like the password to be : "))
    print("Generating password with length %s" %(passwordLen))
    print("-------------------------------------------")

    generator = PasswordGenerator(passwordLen)
    generator.determine()

