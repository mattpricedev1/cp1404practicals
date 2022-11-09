"""
Project Management Program
Time estimate: 3 hours
Actual time:
"""

from project import Project

MENU = "- (L)oad projects\n" \
       "- (S)ave projects\n" \
       "- (D)isplay projects\n" \
       "- (F)ilter projects by date\n" \
       "- (A)dd new project\n" \
       "- (U)pdate project\n" \
       "- (Q)uit"
FILENAME = "projects.txt"
HEADER = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"


def main():
    projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            # TODO: Add filename input
            projects = load_projects(FILENAME)
        elif choice == "S":
            # TODO: Add filename input
            save_projects(projects, FILENAME)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Open, read and append data from txt file to a list using Project class."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
        return projects


def save_projects(projects, filename):
    """Open and write to a text file"""
    with open(filename, "w") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects sorted by percentage completion"""
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if not project.is_complete()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    print("Complete projects:")
    complete_projects = [project for project in projects if project.is_complete()]
    complete_projects.sort()
    for project in complete_projects:
        print(" ", project)


if __name__ == "__main__":
    main()
