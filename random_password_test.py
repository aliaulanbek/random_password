import random_password

def test_create_ascii_range_string():
    #setup
    start = 97
    stop = 100
    expected = "abc"

    #invoke
    actual = random_password.create_ascii_range_string(start,stop)

    #analyze
    assert actual==expected

def test_create_uppercase_letters_string():
    #setup
    # start = 65
    # stop = 91
    expected = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #invoke
    actual = random_password.create_uppercase_letters_string()

    #analyze
    assert actual==expected

def test_create_lowercase_letters_string():
    #setup
    # start = 97
    # stop = 123
    expected = "abcdefghijklmnopqrstuvwxyz"

    #invoke
    actual = random_password.create_lowercase_letters_string()

    #analyze
    assert actual==expected

def test_create_digits_string():
    #setup
    # start = 48
    # stop = 58
    expected = "0123456789"

    #invoke
    actual = random_password.create_digits_string()

    #analyze
    assert actual==expected

def test_create_symbols_string():
    #setup
    # start = 33
    # stop = 48
    expected = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    #invoke
    actual = random_password.create_symbols_string()

    #analyze
    assert actual==expected

def test_get_random_char_from_string():
    #setup
    string1 = "abc"
    expected_1 = "a"
    expected_2 = "b"
    expected_3 = "c"

    #invoke
    actual = random_password.get_random_char_from_string(string1)

    #analyze
    assert actual==expected_1 or actual==expected_2 or actual==expected_3
