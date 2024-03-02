def is_palindrome(data):
    return data[::-1] == data


def lex_compare(a, b):
    return (a > b)*b + (a < b)*a

def count_successive(string):
    if string == "":
        return []
    result = []
    count = 1

    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            result.append((string[i], count))
            count = 1
    result.append((string[len(string) - 1], count))
    return result


def find_positions(items):
    result = {}
    for idx, item in enumerate(items):
        if item in result:
            result[item].append(idx)
        else:
            result[item] = [idx]
    return result



def invert_dictionary(dictionary):
    result = {}
    for key, value in dictionary.items():
        if value in result:
            return None
        else:
            result[value] = key
    return result
