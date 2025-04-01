# Write if ellese if x is larger than y Return True if YES
x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

def eval(x, y):
    if x > y:
        return True
    return False

print(eval(x, y))