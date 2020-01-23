from gamestate import GameState


def test_new_game():
    test_game = GameState()
    assert test_game.bitboards[0] == test_game.NEW_GAME
