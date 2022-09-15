def even_digit_X_2(card_numbers):
    result = []
    for number in card_numbers:
        count = 0
        for i in range(len(number) - 1, -1, -1):
            count = count + 1

            #get the even digit
            if count % 2 == 0:
                result.append(int(number[i]) * 2)

    return result

def sum_digit_in_array(even_digit_sum_X_2):
    result = 0
    for x in even_digit_sum_X_2:
        for digit in str(x):
            result += int(digit)
    return result

def sum_odd_digit(card_numbers):
    result = 0
    for number in card_numbers:
        count = 0
        for i in range(len(number) - 1, -1, -1):
            count = count + 1

            #get the odd digit
            if count % 2 == 1:
                result += int(number[i])

    return result

# read how many data to check for validation
n = int(input())

for i in range(n):
    card_numbers = list(map(str, input().split(" ")))
    even_digit_sum_X_2 = even_digit_X_2(card_numbers)
    digit_sum = sum_digit_in_array(even_digit_sum_X_2)
    odd_digit_sum = sum_odd_digit(card_numbers)
    total = digit_sum + odd_digit_sum

    if(total % 10 == 0):
        print("Valid")
    else:
        print("Invalid")