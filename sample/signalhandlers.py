from Universe import Universe

class ExitHandler:
    def __init__(self, u: Universe):
        self.universe = u
    def __call__(self, signo, frame):
        self.universe.printAllObjects()
        exit(0)

class PrintHandler:
    def __init__(self, u: Universe):
        self.universe = u
    def __call__(self, signo, frame):
        self.universe.printAllObjects()