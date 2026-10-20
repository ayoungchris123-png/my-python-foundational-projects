#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#program accepts a string input representing an item (dictionary key)
#program accepts an integer input representing the number of items to be purchased
#program outputs the item and total cost of purchase

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

print("Enter the item to purchase from the following list: bananas, steak, cookies, celery, or milk.")
item = str(input()).strip().lower()
print("Enter the quantity of that item:")
quantity = int(input())
total = 0


total = purchase[item] * quantity

if quantity < 10:
    print(f"{quantity} {item} total cost: ${total:.2f}")
elif 10 <= quantity <= 20:
    total = total - (total * .05)
    print(f"{quantity} {item} total cost: ${total:.2f}")  
else:
    total = total - (total * .10)
    print(f"{quantity} {item} total cost: ${total:.2f}")
