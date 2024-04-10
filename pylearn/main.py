from dataclasses import dataclass

arr: list[int] = [1, 2, 3, 4, 5]

text: str = "Hello, World!"

boolean: bool = True


def add(a: int, b: int) -> int:
    return a + b


def none() -> None:
    pass  # meaning return None


userInfo: dict[str, int | str] = {"name": "John", "age": 25}


@dataclass
class User:
    name: str
    age: int


info: User = User(name="John", age=25)
info.age = 26
YouShouldLearn: str = "poetry install"
