# def fizzbuzz(num):
#     if (num % 3 == 0) & (num % 5 == 0):
#         return 'FizzBuzz'
#     elif num % 3 == 0:
#         return 'Fizz'
#     elif num % 5 == 0:
#         return 'Buzz'
#     else:
#         return num



# def fibonacci(n):
#     if (n == 0 | n == 1):
#         return n
#     currentNum = 0
#     nextNum = 1
#     result = 0
#     for i in range(n-1):
#         result = currentNum + nextNum
#         currentNum = nextNum
#         nextNum = result
#     return result


# def dot_product(a, b):
#     result = 0
#     for (i,j) in zip(a,b):
#         result += (i * j)
#     return result


# def redact(data, chars):
#     result = ''
#     found = False
#     for i in range(len(data)):
#         for j in range(len(chars)):
#             if data[i] == chars[j]:
#                 result += 'x'
#                 found = True
#         if not found:
#             result += data[i]
#         else:
#             found = False
#     return result

# def count_words(data):
#     if data == "":
#         return {}
#     text = data.split(" ")
#     count = 1


#     for i in range(len(text)):
#         if (i != 0) & (text[0] == text[i]):
#             count += 1


#     dic = {text[0]:count}
#     for i in range(len(text)):
#         if text[i] not in dic:
#             count = 1
#             for j in range(len(text)):
#                 if (i != j) & (text[i] == text[j]):
#                     count += 1
#             dic[text[i]] = count
#     return dic


# def bonus_fizzbuzz(num):
#     """
#     Implement the `fizzbuzz` function.
#     `if`, match-case and cycles are not allowed.
#     """
#     pass


# def bonus_utf8(cp):
#     """
#     Encode `cp` (a Unicode code point) into 1-4 UTF-8 bytes - you should know this from `Základy číslicových systémů (ZDS)`.
#     Example:
#         bonus_utf8(0x01) == [0x01]
#         bonus_utf8(0x1F601) == [0xF0, 0x9F, 0x98, 0x81]
#     """
#     pass