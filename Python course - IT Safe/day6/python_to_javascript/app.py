import eel


def user_input():
    eel.get_ready()()

    while True:
        loading = int(input("[+] start loading? 1/0"))
        if loading == 1:
            eel.js_start_loading()()

        elif loading == 0:
            eel.js_stop_loading()()


eel.spawn(user_input)
eel.init('web')
eel.start('main.html', size=(850,360), options={'port': 0})

