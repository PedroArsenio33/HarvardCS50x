from cs50 import get_int

# prompts user for a card number
card = str(get_int("Card number: "))

c0 = card[0]
c1 = card[1]
cardName = ""

# checks card type
if c0 == "3" and c1 in "47":
    cardName = "AMEX"
elif c0 == "4":
    cardName = "VISA"
elif c0 == "5" and c1 in "12345":
    cardName = "MASTERCARD"

# invalidates cards with no name or incorrect length
if cardName == "" or len(card) not in [13, 15, 16]:
    print("INVALID")

# runs Luhn’s Algorithm to check validity
else:
    even = len(card) % 2 == 0
    temp = ""
    sum = 0

    for i in card:
        if even:
            temp += str(2 * int(i))
        else:
            temp += i
        even = not even

    for i in temp:
        sum += int(i)

    if str(sum)[-1] == "0":
        print(cardName)
    else:
        print("INVALID")
