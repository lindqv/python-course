class BadTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)

team_A = BadTeam("Team A")
team_B = BadTeam("Team B")

team_A.add_member("Ada")
print("Team A", team_A.members)
print("Team B", team_B.members)

# This results in both Team A and B having Ada as a member, 
# as they were initialised to use the same empty list.
# So every BadTeam instance will have a shared list, 
# and changes to one BadTeam will affect every other BadTeam.


class Team:
    def __init__(self, name, members=None):
        self.name = name
        if members is None:
            self.members = []
        else:
            self.members = members

    def add_member(self, member):
        self.members.append(member)

team_A = Team("Team A")
team_B = Team("Team B")

team_A.add_member("Ada")
print("Team A", team_A.members)
print("Team B", team_B.members)