from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        if not isinstance(name, str):
            raise TypeError(" The Name must be a string.")

    @abstractmethod
    def role (self) -> str:
        pass

    def __str__(self) -> str:
        return f"Name: {self.name}, ID: {self.ID}  And the role is: {self.role()}"
