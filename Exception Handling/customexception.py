class pinError(Exception):
    pass


correctPin = 1212
pin  = int(input("Enter 4 digit pin: "))

try:
    if pin == correctPin:
        print("Account Unblocked")
    else:
        raise pinError("Entered Pin is", pin)
except pinError as e:
    print("Error: ",e)