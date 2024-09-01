from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructor for Character.
        Parameters:
        first_name (str): The first name of the character.
        is_alive (bool, optional): The health state of the character.
        Default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        This method represents the action of the object dying.
        """
        pass


class Stark(Character):
    """A class representing a member of the Stark family."""

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a new instance of the class.

        Parameters:
        - first_name (str): The first name of the person.
        - is_alive (bool): Indicates whether the person is alive or not.
          Default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Sets the 'is_alive' to False, indicating that the object has died.
        """
        self.is_alive = False
