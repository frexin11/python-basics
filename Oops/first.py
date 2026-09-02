# using Constructor
class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"Your objects are {self.material}, {self.zips}, {self.pockets}")

reebok = Factory("Leather",3,3)
puma= Factory("Nylon",4,5)

print(f"pockts of puma bag : {puma.pockets}")

reebok.show()
