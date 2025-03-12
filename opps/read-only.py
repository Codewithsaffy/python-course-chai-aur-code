class ReadOnly:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self.__value = new_value + "!"
        elif isinstance(new_value, int):
            self.__value = new_value + 1
        else:
            raise ValueError("Unsupported type for value")

# Example usage:
a = ReadOnly(123)
print(a.value)  # prints the initial value (123)

a.value = 456   # updates the value via the setter (456 + 1 = 457)
print(a.value)  # prints the updated value (457)

a.value = "hello"  # updates the value (resulting in "hello!")
print(a.value)     # prints "hello!"
