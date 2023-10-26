# this function encodes the password inputted by the user
def encode(password): 
  result = ""
  for digit in password:
    # each digit in the 8-digit password is increased by 3
    result_digit = str((int(digit) + 3) % 10)
    result += result_digit
  return result

# this function decodes the password. The password, in this case, being the encoded password.
def decode(password):
  pass
# this is where the main function starts
def main(): 
  while True:
    # menu is printed and user is prompted to choose a menu option
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    menu_option = input("Please enter an option: ")
    if menu_option == "1":
      password = str(input("Please enter your password to encode: "))
      # stores the encoded password if it is a 8-digit string
      if password.isdigit() and len(password) == 8:
        encode(password)
        print("Your password has been encoded and stored!\n")
      else: 
        print("\nInvalid password input. Please input 8-digit password.\n")
    elif menu_option == "2":
      # original password = password
      # original password = decoding the encoded original password
      # prints encoded password and original password
      encoded_password = encode(password)
      print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
      pass
    elif menu_option == "3":
      break

    else:
      print("Invalid selection. Please try again.")


if __name__ == "__main__": 
    main()
