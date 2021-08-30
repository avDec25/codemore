import string

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    digits = digits[::-1]
    mapper = string.ascii_letters + "0123456789"
    return ''.join([mapper[i] for i in digits])

print(numberToBase(12121, 62))