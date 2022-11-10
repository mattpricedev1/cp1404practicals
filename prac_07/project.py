"""Project class."""


class Project:
    """Represent information about a project."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return a string representation of a Project"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Return a Project if priority is less than another priority"""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if completion percentage of a Project is 100%"""
        return self.completion_percentage == 100


def run_tests():
    """Run various tests using the Project class"""
    p1 = Project("Build Car Park", "12/09/2021", 2, 600000.0, 95)
    p2 = Project("Organise Pantry", "20/07/2022", 1, 25.0, 55)
    print(p1)
    print(p1 < p2)


if __name__ == "__main__":
    run_tests()
