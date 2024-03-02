from typing import Callable, Iterator, List, Literal, Optional, Tuple, TypeVar


def is_palindrome(data: str) -> bool:
    return data[::-1] == data


def count_successive(string: str) -> List[Tuple[str, int]]:
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


T = TypeVar("T")


def create_appender(default_value: T) -> Callable[[Optional[T]], List[T]]:
    result = []

    def appender(value: Optional[T] = None) -> List[T]:
        nonlocal result
        if value is not None:
            result.append(value)
        else:
            result.append(default_value)
        return result.copy()

    return appender


def fibonacci_closure() -> Callable[[], int]:
    previous = 0
    current = 0

    def increase() -> int:
        nonlocal previous
        nonlocal current
        if current == 0:
            previous = 0
            current = 1
            return current
        next = previous + current
        previous = current
        current = next
        return current

    return increase


def word_extractor(sentence: str) -> Iterator[str]:
    separators = [' ', '.', '!', '?']
    stop = False
    word = ''

    for char in sentence:
        if char in separators:
            if word == 'stop':
                stop = True
            if word and not stop:
                yield word
            word = ''
        else:
            if not stop:
                word += char

    if word and not stop:
        yield word


def tree_walker(tree, order: Literal["inorder", "preorder", "postorder"]) -> Iterator[int]:
    if tree is None:
        return

    left, value, right = tree

    if order == "inorder":
        yield from tree_walker(left, order)
        yield value
        yield from tree_walker(right, order)
    elif order == "preorder":
        yield value
        yield from tree_walker(left, order)
        yield from tree_walker(right, order)
    elif order == "postorder":
        yield from tree_walker(left, order)
        yield from tree_walker(right, order)
        yield value
