def fizzbuzz(num):
    if (num % 3 == 0) & (num % 5 == 0):
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num



def fibonacci(n):
    if (n == 0 | n == 1):
        return n
    currentNum = 0
    nextNum = 1
    result = 0
    for i in range(n-1):
        result = currentNum + nextNum
        currentNum = nextNum
        nextNum = result
    return result


def dot_product(a, b):
    result = 0
    for (i,j) in zip(a,b):
        result += (i * j)
    return result


def redact(data, chars):
    return ''.join(['x' if c in chars else c for c in data])

def count_words(data):
    if data == "":
        return {}
    text = data.split(" ")
    dic = {}
    for word in text:
        dic[word] = dic.get(word,0) + 1
    return dic


def bonus_fizzbuzz(num):
    return 'Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0) or num


def bonus_utf8(cp):
    if cp <= 0x7F:
        return [cp]
    elif cp <= 0x7FF:
        return [0xC0 | (cp >> 6), 0x80 | (cp & 0x3F)]
    elif cp <= 0xFFFF:
        return [0xE0 | (cp >> 12), 0x80 | ((cp >> 6) & 0x3F), 0x80 | (cp & 0x3F)]
    elif cp <= 0x10FFFF:
        return [0xF0 | (cp >> 18), 0x80 | ((cp >> 12) & 0x3F), 0x80 | ((cp >> 6) & 0x3F), 0x80 | (cp & 0x3F)]