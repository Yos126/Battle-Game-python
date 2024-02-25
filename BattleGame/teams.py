import random
from characters import Warrior, Tanker

class Team:
    MAX_SIZE = 5  # Maximum number of team members

    def __init__(self, team_size=3):
        if team_size > Team.MAX_SIZE:
            raise ValueError(f"Team size cannot be greater than {Team.MAX_SIZE}.")
        self.members = []
        self.team_size = team_size

    def add_member(self, character):
        if len(self.members) < self.team_size:
            self.members.append(character)
        else:
            print("Team is full. Cannot add more members.")

    def display_team(self):
        print("Team Members:")
        for member in self.members:
            print(f"{member.name}, the {member.__class__.__name__} with {member.health} health and {member.attack} attack.")

def create_character(character_type, name):
    if character_type.lower() == "warrior":
        return Warrior(name)
    elif character_type.lower() == "tanker":
        return Tanker(name)
    else:
        raise ValueError(f"Character type {character_type} is not recognized.")

def generate_ai_team(player_team):
    ai_team = Team(player_team.team_size)
    for _ in range(player_team.team_size):
        character_type = random.choice(["Warrior", "Tanker"])
        ai_member_name = f"AI_{character_type}_{random.randint(1, 100)}"
        ai_member = create_character(character_type, ai_member_name)
        ai_team.add_member(ai_member)
    return ai_team

# Main execution flow
if __name__ == "__main__":
    while True:
        try:
            team_size = int(input(f"Enter your team size (default is 3, max is {Team.MAX_SIZE}): ") or 3)
            if not (1 <= team_size <= Team.MAX_SIZE):
                raise ValueError(f"Team size must be between 1 and {Team.MAX_SIZE}.")
            break
        except ValueError as e:
            print(e)

    player_team = Team(team_size)
    
    # Add members to the player's team
    for i in range(team_size):
        while True:
            character_type = input(f"Choose the type for character {i+1} ('Warrior' or 'Tanker'): ").lower()
            if character_type in ("warrior", "tanker"):
                character_name = input(f"Name your {character_type}: ")
                player_team.add_member(create_character(character_type, character_name))
                break
            else:
                print("Invalid member type. Please choose 'Warrior' or 'Tanker'.")
    
    # Display player's team
    player_team.display_team()
    
    # Generate and display AI team
    ai_team = generate_ai_team(player_team)
    print("\nAI Team:")
    ai_team.display_team()