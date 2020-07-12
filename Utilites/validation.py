def is_num(num):
    if num.isdigit():
        return True
    else:
        return False


def is_choice_valid(option):
    if is_num(option) and option == "1" or option == "2":
        return True
    else:
        return False


def check_if_yes_or_no(user_answer):
    if user_answer.lower() == "yes" or user_answer.lower() == "no":
        return True
    else:
        return False
