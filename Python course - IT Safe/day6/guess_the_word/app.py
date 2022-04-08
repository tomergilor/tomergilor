import eel
import random

@eel.expose
def start_game():
    global game_word
    game_word = list(random.choice(["roman", "itsafe", "hacking", "cyber", "python"]))
    for data in range(len(game_word)):
        game_state.append("_")

    print (game_word)

@eel.expose
def guess_character(character):
    global tries
    tries += 1

    if game_word.count(character):

        for index,data in enumerate(game_word):
            if character == data:
                game_state[index] = character

    if game_state.count("_") == 0:
        return "You win! the word was '{0}', in {1} tries".format("".join(game_word), tries)

    return ",".join(game_state)

tries = 0
game_word = []
game_state = []

eel.init('web')
eel.start('main.html', size=(850,360), options={'port': 0})

