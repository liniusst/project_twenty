# class Person:
#     """Collect data about person and greets a person"""

#     def __init__(self, name: str, surname: str) -> None:
#         self.name = name
#         self.surname = surname

#     def say_hello(self) -> None:
#         """Function greets a person given name"""
#         print(f"hello, {self.name}")


# person = Person(name="first", surname="person")
# person.say_hello()


# def greetings(full_name: str) -> None:
#     """Function greets a person given full name as a string"""
#     print(f"Hello {full_name.split()[0]} {full_name.split()[1]}, How are you today?")


# greetings("Linas Stonkus")


# def age_check(age: int) -> None:
#     if age >= 21:
#         print("Welcome")
#     else:
#         print("Access denied")


# age_check(21)


# For example Number = 50113 => 5+0+1+1+3=10 => 1+0=1 This is a Magic Number
def magic_number(number: int):
    for int in number:
        print(int)


magic_number(15)
