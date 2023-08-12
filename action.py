import curses
actions = ['Up', 'Left', "Down", "Right", "Restart", "Exit"]
letter_codes = [ord(ch) for ch in "WASDRQwasdrq"]
actions_dict = dict(zip(letter_codes, actions*2))


def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]
