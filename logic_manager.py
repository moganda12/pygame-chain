class Sprite :
    def __init__(self, see_force) :
        self.eye_chanell = see_force
        self.showList = []
        self.hideList = []

    def show(self, name, coord) :
        self.Surface = None
        self.Surface.name = name
        self.Surface.coord = coord
        self.showList.append(Surface)

    def update(self) :
        for surface in self.showList :
            self.eye_chanell.blit(surface.name, surface.coord) 