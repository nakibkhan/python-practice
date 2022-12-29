from exercises.password_generator.password_generator import PasswordGenerator

if __name__ == "__main__":

    print("Entering Password Generator")
    passwordLen = int(input("Please enter the length you would like the password to be : "))
    print("Generating password with length %s" %(passwordLen))
    print("-------------------------------------------")

    generator = PasswordGenerator(passwordLen)
    generator.determine()

