full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
       return "The character should have a name"
    if len(name)>10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    stats = [strength, intelligence, charisma]
    if not all(isinstance(s, int) for s in stats):
        return "All stats should be integers"

    # 3. Validate ranges (Python doesn't allow (a, b, c) < 1 directly)
    if any(s < 1 for s in stats):
        return "All stats should be no less than 1"
    if any(s > 4 for s in stats):
        return "All stats should be no more than 4"

    # 4. Validate sum (sum() takes a list/tuple as one argument)
    if sum(stats) != 7:
        return "The character should start with 7 points"
    return (
        f"{name}\n"
        f"STR {strength * full_dot}{(10 - strength) * empty_dot}\n"
        f"INT {intelligence * full_dot}{(10 - intelligence) * empty_dot}\n"
        f"CHA {charisma * full_dot}{(10 - charisma) * empty_dot}"
    )
print(create_character('ren', 4, 2, 1))
