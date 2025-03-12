class Person:
    def __init__(self, name):
        self._name = name  # Private attribute (convention: _name)

    @property
    def name(self):
        """Getter method to access the name attribute."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter method to update the name attribute."""
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

# Usage
p = Person("John")
print(p.name)  # Calls the getter method

p.name = "Alice"  # Calls the setter method
print(p.name)

# p.name = ""  # Raises ValueError
