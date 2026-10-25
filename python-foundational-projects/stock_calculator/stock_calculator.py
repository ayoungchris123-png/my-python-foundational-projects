#program accepts an integer input representing the number of stock selections
#program accepts string inputs equivalent to the integer input identifying the stock selections
#program outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places


stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

'''
print("Enter a quantity of stocks followed by stock symbol(s): TSLA, BBBY, AAPL, SOFI, KIRK, AURA, AMZN, EMBK, LVLU")
num_items = int(input())
stc_list = []
total = 0.0
exit = 0
'''
exit = 0

while exit != 1:
    try:
        print("Enter a quantity of stocks followed by stock symbol(s): TSLA, BBBY, AAPL, SOFI, KIRK, AURA, AMZN, EMBK, LVLU")
        num_items = int(input())
        stc_list = []
        total = 0.0

        for i in range(num_items):
            item = input()
            stc_list.append(item)


        for symbol in stc_list:
            if symbol in stocks:
                total += stocks[symbol]


        print(f"Total price: ${total:.2f}")

        exit = int(input('Enter 1 if you are finished or any other key to enter a new response: '))
    except:
        print('Invalid entry.')
        exit = int(input('Enter 1 if you are finished or any other key to enter a new response: '))




