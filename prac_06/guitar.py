import datetime

TODAY = datetime.date.today()  # get today's date
VINTAGE_AGE = 50


class Guitar:
    """Guitar class"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string formatting of a guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of a guitar based on current year"""
        year = TODAY.strftime("%Y")  # get the year from today's date
        return int(year) - self.year

    def is_vintage(self):
        """Determine if guitar is vintage based on age"""
        return self.is_vintage(self) >= VINTAGE_AGE
