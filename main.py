import eel
eel.init('templates')

@eel.expose
def demo(x):
    return x**2

def random_python():
    print("Random function running")
    return randint(1,100)

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))