# Assignment 4.2 step 4
import random

def create_ascii_range_string(start, stop):
    i = 0
    char_string = ""
    for i in range(start,stop):
        char_string += chr(i)
        i+=1
    
    return char_string

def create_uppercase_letters_string():
    return create_ascii_range_string(65, 91)

def create_lowercase_letters_string():
    return create_ascii_range_string(97, 123)
     
def create_digits_string():
    return create_ascii_range_string(48, 58)

def create_symbols_string():
    return create_ascii_range_string(33, 48) + create_ascii_range_string(58, 65)+create_ascii_range_string(91, 97)+create_ascii_range_string(123, 127)

def get_random_char_from_string(string):
    random_char_index = random.randrange(0, len(string))
    return string[random_char_index]

def generate_random_password(num_uppercase, num_lowercase, num_digits, num_symbols):
    password_length = num_uppercase + num_lowercase + num_digits + num_symbols
    password_string = ""
    
    i=0
    
    while i < password_length:
        string_class = random.randint(1,4)
        if string_class == 1 and num_uppercase>0:
            num_uppercase-=1
            password_string += get_random_char_from_string(create_uppercase_letters_string())
            i+=1
        elif string_class == 2 and num_lowercase>0:
            num_lowercase-=1
            password_string += get_random_char_from_string(create_lowercase_letters_string())
            i+=1
        elif string_class == 3 and num_digits>0:
            num_digits-=1
            password_string += get_random_char_from_string(create_digits_string()) 
            i+=1
        elif string_class == 4 and num_symbols>0:
            num_symbols-=1
            password_string+= get_random_char_from_string(create_symbols_string())  
            i+=1
        else:
            i+=0
    return password_string


def main():
    while True: 
        length = input("\nExample: \"4 3 1 5\"\nEnter <num uppers> <num lowers> <num digits> <num symbols> with spaces in between (press 'enter' to quit):\n")
        tokens = length.split()
        if len(tokens) == 0:
            print("Goodbye!")
            return
        elif len(tokens) != 4:
            print("You must enter exactly 4 values")
        elif len(tokens) == 4:
            print("\nGenerated Password:", generate_random_password(int(tokens[0]),int(tokens[1]),int(tokens[2]),int(tokens[3])))
        else:
            break

if __name__ == "__main__":
    main()