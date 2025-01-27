def isDistinct(num: int) -> bool:
    s = str(num)
    digits_used = []

    for char in s: 
        if char in digits_used:
            return False
        digits_used.append(char)
    return True

num = int(input("Enter a 4 digit number: "))
num += 1

while(not isDistinct(num)):
    num += 1

print(num)