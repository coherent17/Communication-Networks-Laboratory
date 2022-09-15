def credit_check(full_number):

    #using flag to check whether is even/odd digit
    isEven = False
    sum = 0

    for i in range(len(full_number) - 1, -1, -1):
        digit = int(full_number[i])
        
        if isEven:
            digit *= 2
        
        sum += digit // 10      #for odd digit, +0
        sum += digit % 10

        isEven = ~isEven
    
    if sum % 10 == 0:
        print("Valid")
    else:
        print("Invalid")

        
n = int(input())

for i in range(n):
    cards_number = list(map(str, input().split(" ")))

    #concatenate the string without space
    full_number = ""
    for number in cards_number:
        full_number = full_number + number
    
    credit_check(full_number)