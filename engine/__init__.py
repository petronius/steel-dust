import engine.wizard


def run():
    name = input("NAME YOUR WIZARD: ")
    color = input("WHAT COLOR MAGIC DOES %s USE? " % name)
    print("WELCOME, %s the %s" % (name, color))

    opponent = wizard.random_wizard()
    print("YOUR OPPONENT IS %s" % opponent)

