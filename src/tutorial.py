from dataclasses import dataclass

arr: list[int] = [1, 2, 3, 4, 5]

text: str = "Hello, World!"

boolean: bool = True


def add(a: int, b: int) -> int:
    return a + b


def none() -> None:
    pass  # meaning return None


# object define
userInfo: dict[str, int | str] = {"name": "John", "age": 25}


@dataclass
class User:
    name: str
    age: int


info: User = User(name="John", age=25)
info.age = 26

# for i in range(0,200,10):
#     print(i)

array: list[int] = [1, 2, 3, 4, 5]
text = "Hello, World!"
print(array,text,sep=" ")

