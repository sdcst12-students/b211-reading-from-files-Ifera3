#!Python 3

"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol # I only found 18 stocks with symbol AA in it
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

def main():
    fileName = 'task5.csv'
    file = open(fileName,'r')
    data = file.read().split('\n')
    stockSymbols = {}
    for i in data:
        stock = i.split(',',maxsplit=1)
        #print(stock)
        stockSymbols[stock[0]] = stock[1]
    #print(stockSymbols) #fails to print full dictionary
    symbol = input('Enter stock symbol: ').upper()
    repeat = 0
    for i in stockSymbols:
        if symbol in i:
            repeat = repeat + 1
    if repeat != 1:
        print(f'There are {repeat} stocks with the symbol {symbol}')
    elif symbol in stockSymbols:
        print(f'The company with the {symbol} is {stockSymbols[symbol]}')
    else:
        print('No matches found')


if __name__ == '__main__':
    main()