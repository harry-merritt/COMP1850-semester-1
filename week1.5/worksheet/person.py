# Worksheet 1.5: Person class

from datetime import date


class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        """
        Creates a person, with a name and date of birth.
        """
        if name == "":
            raise ValueError

        if not isinstance(name, str):
            raise TypeError

        self.name = name

        if type(birth) != date:
            raise TypeError

        self.birth = birth

    def initials(self):
        """
        Returns the initials of the person.
        """
        return ''.join([word[0] for word in self.name.upper().split(sep=" ")])
        # Horrid one-line solution just to show off

    def is_birthday(self):
        """
        Returns if it is the person's birthday today.
        """
        return (self.birth.day == date.today().day and self.birth.month == date.today().month)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
