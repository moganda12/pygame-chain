class Sprite :
    def __init__(self, see_force) :
        self.eye_chanell = see_force

    showList = []
    hideList = []

    def show(self, name, coord) :
        Surface = None
        Surface.name = name
        Surface.coord = coord
        self.showList.append(Surface)

    def update(self) :
        for surface in self.showList :
            self.eye_chanell.blit(surface.name, surface.coord) 