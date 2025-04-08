# Write if ellese if x is larger than y Return True if YES
x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
b = 100
def eval(x, y, b):
    if (x > y and x < b):
        return True
    return False

print(eval(x, y, b))