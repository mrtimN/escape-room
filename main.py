from game_logic import start_game
from game_state import INIT_GAME_STATE

if __name__ == "__main__":
    game_state = INIT_GAME_STATE.copy()
    start_game(game_state)