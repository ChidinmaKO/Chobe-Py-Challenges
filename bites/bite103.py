games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won=games_won):
    for k,v in games_won.items():
        if v > 1 or v == 0:
            print(f"{k} has won {v} games")
        else:
            print(f"{k} has won {v} game")
    pass

    # better way:
    games = 'game' if v == 1 else 'games'
    print(f"{k} has won {v} {games}")