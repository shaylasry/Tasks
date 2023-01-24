
def recursive_digit(num):
    if num == 0:
        return 0

    digit = num % 10
    new_num = (int)(num / 10)
    return digit + recursive_digit(new_num)



if __name__ == '__main__':
    print(recursive_digit(2347623))