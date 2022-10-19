import main

class Sprite :
    showList = []
    hideList = []

    def show(self, name, coord) :
        Surface = None
        Surface.name = name
        Surface.coord = coord
        self.showList.append(Surface)

    def update(self) :
        for surface in self.showList :
            main.see_recepticle.blit(surface.name, surface.coord) 