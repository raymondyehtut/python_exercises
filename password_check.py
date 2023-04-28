# define the correct ID and Password
correct_id = "user123"
correct_password = "pass123"

# get user input for ID and Password
input_id = input("Enter your ID: ")
input_password = input("Enter your password: ")

# check if the input matches the correct ID and Password
if input_id == correct_id and input_password == correct_password:
    print("Login successful!")
else:
    print("Invalid ID or password.")
