import datetime

TODAY = datetime.date.today()
VINTAGE_AGE = 50


class Guitar:
    """Guitar class"""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string formatting"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        year = TODAY.strftime("%Y")
        year = int(year)
        return year - self.year

    def is_vintage(self):
        return self.is_vintage(self) >= VINTAGE_AGE
