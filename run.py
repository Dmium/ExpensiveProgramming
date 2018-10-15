from monzo.monzo import Monzo

def interpret(instructions):
    data = [0]
    ipointer = 0
    dpointer = 0
    while ipointer < len(instructions):
        if instructions[ipointer] == 1:
            data[dpointer] += 1
        elif instructions[ipointer] == 2:
            data[dpointer] -= 1
        elif instructions[ipointer] == 3:
            dpointer += 1
            if len(data) == dpointer:
                data.append(0)
        elif instructions[ipointer] == 4:
            dpointer -= 1
        elif instructions[ipointer] == 5:
            if data[dpointer] == 0:
                mismatch = 1
                while mismatch > 0:
                    ipointer += 1
                    if instructions[ipointer] == 6:
                        mismatch -= 1
                    elif instructions[ipointer] == 5:
                        mismatch += 1
        elif instructions[ipointer] == 6:
            if data[dpointer] != 0:
                mismatch = 1
                while mismatch > 0:
                    ipointer -= 1
                    if instructions[ipointer] == 6:
                        mismatch += 1
                    elif instructions[ipointer] == 5:
                        mismatch -= 1
        elif instructions[ipointer] == 7:
            data[dpointer] = ord(input("Enter character: "))
        elif instructions[ipointer] == 0:
            print(chr(data[dpointer]))
        ipointer += 1

client = Monzo(input('Please enter Monzo API key: '))
account_id = input('Please enter Monzo account_id: ')
transactions = client.get_transactions(account_id)
instructions = []
pname = input("Please enter name of program: ")
for transaction in transactions['transactions']:
    if pname in transaction['notes']:
        if transaction['amount'] == 0:
            instructions = []
        else:
            instructions.append(abs(transaction['amount']) % 8)
interpret(instructions)
