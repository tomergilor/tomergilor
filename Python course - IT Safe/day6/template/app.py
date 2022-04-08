import eel

eel.init('web')

try:
    eel.start('index.html', size=(850,400), options={'port': 0})   #python will select free ephemeral ports.
except (SystemExit, MemoryError, KeyboardInterrupt):
    print ("Program Exit, Save Logs if Needed")