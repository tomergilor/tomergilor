## function that checks if number is palindrome

number = "12321"
num_len = len(number)


def is_pol(num):
    for i in range(num_len // 2):
        if num[i] == num[-i - 1]:
            continue
        else:
            print("NO")
            exit()
    print("yes")


is_pol(number)

