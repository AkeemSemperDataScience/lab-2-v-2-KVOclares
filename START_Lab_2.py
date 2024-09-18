def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise

    def palindrome_checker(string):
        return string == string[::-1]
    
    return palindrome_checker(word)
    pass

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number

    def fibonacci_checker(value):
        current_fibonacci = []
        counter = 0
        number_sequence = 1
        n1, n2 = 0, 1

        if value >= 0:
            while counter < number_sequence:
                if n1 <= value:
                    current_fibonacci.append(n1)
                    current_number_sequence = n1 + n2
                    n1 = n2
                    n2 = current_number_sequence
                    number_sequence += 1
                    counter += 1
                else:
                    return current_fibonacci
        else: 
            return current_fibonacci
    
    return fibonacci_checker(number_val)
    pass

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    def string_counter(first_string, second_string):
        lowered_case = first_string.lower()
        return lowered_case.count(second_string)
    
    return string_counter(str1, str2)
    pass

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    def sums_list(list_1, list_2):
        if len(list_1) == len(list_2):
            sum_list = [list_1[i] + list_2[i] for i in range(len(list_1))]
        else:
            sum_list = []
        return sum_list
    
    return sums_list(list1, list2)
    #pass


def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = None
    print("Please Enter Password: ")
    password = input()
    if isValidPassword(password) == True:
        return password
    else:
        lab2Question5()


def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number

    def Count_checker(c_password):
        return len(c_password) >= 8
    
    def Uppercase_checker(u_password):
        return any(count.isupper() for count in u_password)
    
    def Lower_checker(l_password):
        return any(count.islower() for count in l_password)
    
    def Number_checker(n_password):
        return any(count.isnumeric() for count in n_password)
    
    return all([Count_checker(password), Uppercase_checker(password), Lower_checker(password), Number_checker(password)]) 

    pass

lab2Question5()