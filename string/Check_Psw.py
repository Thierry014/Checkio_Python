def is_acceptable_password(password: str) -> bool:
    # your code here
    count = 0
    for char in password:
        if char.isdigit():
            count += 1
    print(len(password))
    if len(password) > 6 and count > 0:
        return True
    return False



print(is_acceptable_password('muchlonger5'))