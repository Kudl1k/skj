import dataclasses
from typing import Callable, Generic, List, Optional, TypeVar


def cached(f):
    """
    Create a decorator that caches up to 3 function results, based on the same parameter values.

    When `f` is called with the same parameter values that are already in the cache, return the
    stored result associated with these parameter values. You can assume that `f` receives only
    positional arguments (you can ignore keyword arguments).

    When `f` is called with new parameter values, forget the oldest inserted result in the cache
    if the cache is already full.

    Example:
        @cached
        def fn(a, b):
            return a + b # imagine an expensive computation

        fn(1, 2) == 3 # computed
        fn(1, 2) == 3 # returned from cache, `a + b` is not executed
        fn(3, 4) == 7 # computed
        fn(3, 5) == 8 # computed
        fn(3, 6) == 9 # computed, (1, 2) was now forgotten
        fn(1, 2) == 3 # computed again, (3, 4) was now forgotten
    """
    cache_order = []
    cache = {}

    def fn(*args):
        if args in cache:
            return cache[args]     
        else:
            if len(cache_order) >= 3:
                last_item = cache_order.pop(0)
                del cache[last_item]
            value = f(*args)
            cache[*args] = value
            cache_order.append(args)
            return value
    return fn




T = TypeVar("T")




@dataclasses.dataclass
class ParseResult(Generic[T]):
    """
    Represents result of a parser invocation.
    If `value` is `None`, then the parsing was not successful.
    `rest` contains the rest of the input string if parsing was succesful.
    """
    value: Optional[T]
    rest: str

    @staticmethod
    def invalid(rest: str) -> "ParseResult":
        return ParseResult(value=None, rest=rest)

    def is_valid(self) -> bool:
        return self.value is not None


"""
Represents a parser: a function that takes a string as an input and returns a `ParseResult`.
"""
Parser = Callable[[str], ParseResult[T]]

"""
Below are functions that create new parsers.
They should serve as LEGO blocks that can be combined together to build more complicated parsers.
See tests for examples of usage.

Note that parsers are always applied to the beginning of the string:
```python
parser = parser_char("a")
parser("a")  # ParseResult(value="a", rest="")
parser("xa") # ParseResult(value=None, rest="xa")
```
"""


def parser_char(char: str) -> Parser[str]:
    """
    Return a parser that will parse a single character, `char`, from the beginning of the input
    string.

    Example:
        ```python
        parser_char("x")("x") => ParseResult(value="x", rest="")
        parser_char("x")("xa") => ParseResult(value="x", rest="a")
        parser_char("y")("xa") => ParseResult(value=None, rest="xa")
        ```
    """
    if not char:
        raise ValueError()

    if len(char) > 1:
        raise ValueError()
    
    def inner_parser(input: str) -> ParseResult[str]:
        if input.startswith(char):
            return ParseResult(value=char,rest=input[len(char):])
        else:
            return ParseResult.invalid(rest=input)
    return inner_parser


def parser_repeat(parser: Parser[T]) -> Parser[List[T]]:
    """
    Return a parser that will invoke `parser` repeatedly, while it still matches something in the
    input.

    Example:
        ```python
        parser_a = parser_char("a")
        parser = parser_repeat(parser_a)
        parser("aaax") => ParseResult(value=["a", "a", "a"], rest="x")
        parser("xa") => ParseResult(value=[], rest="xa")
        ```
    """
    def inner_parser(input: str) -> ParseResult[str]:
        values = []
        temp = input
        while True:
            result = parser(temp)
            if result.is_valid():
                values.append(result.value)
                temp = result.rest
            else:
                break
        return ParseResult(value= values, rest = temp)
    return inner_parser



def parser_seq(parsers: List[Parser]) -> Parser:
    """
    Create a parser that will apply the given `parsers` successively, one after the other.
    The result will be successful only if all parsers succeed.

    Example:
        ```python
        parser_a = parser_char("a")
        parser_b = parser_char("b")
        parser = parser_seq([parser_a, parser_b, parser_a])
        parser("abax") => ParseResult(value=["a", "b", "a"], rest="x")
        parser("ab") => ParseResult(value=None, rest="ab")
        ```
    """
    def inner_parser(input: str) -> ParseResult[str]:
        if not parsers:
            return ParseResult(value=[],rest=input)
        values = []
        temp = input
        for parser in parsers:
            result = parser(temp)
            if result.is_valid():
                values.append(result.value)
                temp = result.rest
            else:
                return ParseResult(value=None, rest=input)

        return ParseResult(value=values,rest=temp)

    return inner_parser


def parser_choice(parsers: List[Parser]) -> Parser:
    """
    Return a parser that will return the result of the first parser in `parsers` that matches something
    in the input.

    Example:
        ```python
        parser_a = parser_char("a")
        parser_b = parser_char("b")
        parser = parser_choice([parser_a, parser_b])
        parser("ax") => ParseResult(value="a", rest="x")
        parser("bx") => ParseResult(value="b", rest="x")
        parser("cx") => ParseResult(value=None, rest="cx")
        ```
    """
    def inner_parser(input: str) -> ParseResult[str]:
        temp = input
        for parser in parsers:
            result = parser(temp)
            if result.is_valid():
                return ParseResult(value= result.value,rest= result.rest)
        return ParseResult(value=None,rest= input) 
    return inner_parser   
        


R = TypeVar("R")


def parser_map(parser: Parser[R], map_fn: Callable[[R], Optional[T]]) -> Parser[T]:
    """
    Return a parser that will use `parser` to parse the input data, and if it is successful, it will
    apply `map_fn` to the parsed value.
    If `map_fn` returns `None`, then the parsing result will be invalid.

    Example:
        ```python
        parser_a = parser_char("a")
        parser = parser_map(parser_a, lambda x: x.upper())
        parser("ax") => ParseResult(value="A", rest="x")
        parser("bx") => ParseResult(value=None, rest="bx")

        parser = parser_map(parser_a, lambda x: None)
        parser("ax") => ParseResult(value=None, rest="ax")
        ```
    """
    def inner_parser(input: str) -> ParseResult[str]:
        result = parser(input)
        if result.is_valid():
            if map_fn(result.value) is None:
                return ParseResult(value=None,rest=input)
            else:
                return ParseResult(value=map_fn(result.value),rest=result.rest)
        else:
            return ParseResult(None,input)
        
    return inner_parser





def parser_matches(filter_fn: Callable[[str], bool]) -> Parser[str]:
    """
    Create a parser that will parse the first character from the input, if it is accepted by the
    given `filter_fn`.

    Example:
        ```python
        parser = parser_matches(lambda x: x in ("ab"))
        parser("ax") => ParseResult(value="a", rest="x")
        parser("bx") => ParseResult(value="b", rest="x")
        parser("cx") => ParseResult(value=None, rest="cx")
        parser("") => ParseResult(value=None, rest="")
        ```
    """
    def inner_parser(input: str) -> ParseResult[str]:
        if not input:
            return ParseResult(None,input)
        result = filter_fn(input[0])
        if not result:
            return ParseResult(None,input)
        else:
            return ParseResult(value= input[0], rest=input[1:])
    return inner_parser

# Use the functions above to implement the functions below.


def parser_string(string: str) -> Parser[str]:
    """
    Create a parser that will parse the given `string`.

    Example:
        ```python
        parser = parser_string("foo")
        parser("foox") => ParseResult(value="foo", rest="x")
        parser("fo") => ParseResult(value=None, rest="fo")
        ```
    """
    def inner_parser(input: str) -> ParseResult[str]:
        value = ""
        temp = input
        for i in string:
            parser = parser_char(i)
            result = parser(temp)
            if result.is_valid():
                value += result.value
                temp = result.rest
            else:
                return ParseResult(None, input)
        return ParseResult(value=value,rest=temp)
        
    return inner_parser


def parser_int() -> Parser[int]:
    """
    Create a parser that will parse a non-negative integer (you don't have to deal with
    `-` at the beginning).

    Example:
        ```python
        parser = parser_int()
        parser("123x") => ParseResult(value=123, rest="x")
        parser("foo") => ParseResult(value=None, rest="foo")
        ```
    """
    def inner_parser(input: str) -> ParseResult[int]:
        num_str = ""
        parser = parser_matches(lambda x: x in ("0123456789"))
        temp = input
        for i in input:
            result = parser(temp)
            if result.is_valid():
                num_str += result.value
                temp = result.rest
            else:
                break
        if num_str == "":
            return ParseResult(value=None,rest=input)
        else:
            return ParseResult(value=int(num_str),rest=input[len(num_str):])
    return inner_parser
        

        