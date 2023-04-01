# Here i am going to import some Modules, and the first Module is "random" Module, bcz we need to generate the slot machine values kind of randomly.
import random

# To keep this program nice and dynamic, I am gonna add, what's known as a global constant at the top of my programm
# I wrote it all capitals bcz its a constant value, something that is not gonna change
# So now anywhere in my programm where i'm referrencing the number of maximum lines in my slot machine rather than writting 3, i'll write MAX_LINES. and later on i can change it to any number that i want.
MAX_LINES = 3
#some other bets
MAX_BET = 100
MIN_BET = 1

# here i am gonna set some values here that specify the number of rows and columns, we are gonna have in our slot machine.
ROWS = 3
COLS = 3

# Now we need to specify that how many symbols are in each of our reals. so we are using dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
# Now what we need something that's essentially going to generarte what the outcome of the slot machine was using the values above from line 13 to 22,
def get_slot_machine_spin(rows, cols, symbols):
    #So inside of this function, again, what we need to do is generate what symbols are going to be in each column based on the frequency of symbols that we have here
    all_symbols = []
    # below i used "symbol.item" so when we use .items, it gives you both the key and the value asssociated with a dictionary
      #the key, the value
    for symbol, symbol_count in symbols.items():
        #so now i want to add this many symbols to the "symbol list" using a new "for" loop
        for _ in range(symbol_count):
            #below i am appending whatever the symbol is
            all_symbols.append(symbol)

    #now that we have the all symbols list, we need to select what values are goin to go in every single column.
    #i am writting writting a "for" loop that is goin to to do loop over every column.
    # I am using a nested loop bcz typically when you write a nested list, you kinda have all of the interior lists here that are responding our rows.
    columns = []

    #so for every column, we need to generate the values inside of the columns, how many we should generate ? however many rows we have, that's how many values we need.
    # so here if we have three columns, then we need to do everything inside of here 3 times
    for _ in range(cols):
        #now the below code, its picking random values for each, row in our column, so for each value that we are going to have.
        column = []
        # herre i have used "[:]", so it mean i am copying the variable "all _symbols"
        #cure_symbol here means that the one we can currently select.
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            #so here er remove it bcz we dont pick it again
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# Now we need to print out what's inside of our columns.
# This code defines a function called print_slot_machine that takes a single argument columns,
# which is expected to be a list of lists representing the columns of a slot machine.
def print_slot_machine(columns):
    #then i am using a nested for loop to iterate over each row in the columns.
    #so the outer loop iterates over the range of the length of the first column (assuming all columns have the same number of rows)
    for row in range(len(columns[0])):
        #and the inner loop iterates over each column in "columns".
        for i, column in enumerate(columns):
            #For each row, the function prints the symbol at that row for each column, separated by a vertical bar (|).
            #The enumerate() function is used to get both the index of the current column (i) and its corresponding list of symbols (column).
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


# First I am defining a function that is responsible for collecting user input that get the deposit.
def deposit():
    # I'm continually ask the user to enter a deposit amount until they give me a valid amount.
    # So if they don't give me a valid amount, then they need to keep typing in until eventully we get one.
    while True:
        amount = input("What would you like to deposit? $")
        # Now i need to to check if this amount is actually  number
        if amount.isdigit():
            # Convert it to an int because we want to have a numeric value for our balance or for our deposit.
            # However we can type it before but it could potentially fail.
            amount = int(amount)
            # Now i check if the amount is greater than 0.
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount

# Here i wanna collect the bet from the user.
# I need to determine how much i want to bet and then how many lines they wanna bet on, and i would multiply their amount by the number of lines.
def get_number_of_lines():
    # inside of here, i am going to ask them to pick a number between 1 and 3, bcz that will be the number of lines that we have.
    while True:
        #The str() function is used to convert the integer value of "MAX_LINES" into a string, so that it can be concatenated with the rest of the prompt message.
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # Now i need to to check if this amount is actually  number,
        if lines.isdigit():
            # Convert it to an int because we want to have a numeric value for our balance or for our deposit.
            # However we can type it before but it could potentially fail.
            lines = int(lines)
            # Now i am gonna check if the lines is within the bound that i had. so within (1 to 3)
            # So this line is a conditional statement that checks whether the value of the lines variable is between 1 and MAX_LINES (inclusive).
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines


# The next thing i need to get for the user input is the amount that i wanna bet on each line.
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        # Now i need to to check if this amount is actually  number
        if amount.isdigit():
            # Convert it to an int because we want to have a numeric value for our balance or for our deposit.
            # However we can type it before but it could potentially fail.
            amount = int(amount)
            # Now i need to check if the amount is between the minimum and the maximum bet.
            # This is a conditional statement that checks if the value of the variable "amount" is between the values of "MIN_BET" and "MAX_BET", inclusive.
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                # I use "f'String" so inside of the curly braces i can write any variable and it will automatically converted to string if it can be converted.
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")
    return amount
# I'm gonna put my programm in the function main so that if I end the program we can just call this function again and then it will return the program.

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that number, you current balance is: ${balance}.")
        else:
            break
    # we are probably gonna print out here in our main function kind of what they've said so far.
    # so we'll say(you are bettig, e.g $5 on 3 lines, ur total bet is $50, somthing like that.)
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    print(f"You won ${winnings}.")
    print(f"You won on", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()

