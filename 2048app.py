from collections import defaultdict
import curses
import board
import action


def main(stdscr):
    def init():
        game_field.reset()
        return "Game"

    def not_game(state):
        # 判断输还是赢
        game_field.draw(stdscr)
        # 等待用户输入，判断下一步操作
        actions = action.get_user_action(stdscr)
        response = defaultdict(lambda: state)
        response["Restart"], response["Exit"] = "Init", "Exit"
        return response[actions]

    def game():
        # 画出当前棋盘
        game_field.draw(stdscr)
        # 等待用户输入
        actions = action.get_user_action(stdscr)
        if actions == "Restart":
            return "Init"
        if actions == "Exit":
            return "Exit"
        if game_field.move(actions):
            if game_field.is_win():
                return "Win"
            if game_field.is_gameover():
                return "Gameover"
        return "Game"

    state_action = {
        "Init": init,
        "Win": lambda: not_game("Win"),
        "Gameover": lambda: not_game("Gameover"),
        "Game": game
    }

    curses.use_default_colors()
    game_field = board.GameField()
    state = "Init"
    while state != "Exit":
        state = state_action[state]()


curses.wrapper(main)
