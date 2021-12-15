path = input("Please enter the path to your file: ")
date = input("Enter the date in which you want to see list to do: ")
dictionary = read_file(path)
def check_date(date, dictionary):
    """
    Checks if this date is in the list.
    If it is -> the list of things to do.
    If it is not -> nothing and message if you wnat to add something on this date.
    """
    next_question = "Do you wnat to add something on this date?"
    if date in dictionary:
        value = dictionary.get(date)
        print(date)
        print(value)
        print(next_question)
    else:
        print("You have nothing planned for this date.")
        print(next_question)
    next_step = input("Print Y/N: ")
    return next_step

next_step = check_date(date, dictionary)
