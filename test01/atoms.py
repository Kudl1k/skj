import playground
import random


class Atom:
    def __init__(self, x, y,speedx,speedy, rad, color,bounce):
        """
        Inicializator třídy Atom
        :param x: souřadnice X
        :param y: soouřadnice Y
        :param rad: poloměr
        :param color: barva
        """
        self.x = x
        self.y = y
        self.radius = rad
        self.color = color
        self.speedx = speedx
        self.speedy = speedy
        self.bounce = bounce

    def to_tuple(self):
        """Vrátí n-tici hodnot 
        příklad: x = 10, y = 12, rad = 15, color = 'green' -> (10,12,15,'green')
        """
        return tuple(self.xPos,self.yPos,self.radius,self.color)

    def move(self, width, height):
        if (self.x + self.speedx > width or self.x + self.speedx < 0 ):
            if self.bounce:
                self.speedx = -self.speedx
            else:
                self.speedx = -self.speedx
                self.speedy = -self.speedy
        else:
            self.x += self.speedx
        if (self.y + self.speedy > height or self.y + self.speedy < 0):
            if self.bounce:
                self.speedy = -self.speedy
            else:
                self.speedx = -self.speedx
                self.speedy = -self.speedy
        else:
            self.y += self.speedy


class ExampleWorld(object):

    def __init__(self, size_x, size_y, count):
        self.width = size_x
        self.height = size_y
        self.count = count
        self.random_atom()

    def random_atom(self):
        self.list_of_atoms = []
        colors = ['green','red','blue']
        bouce_type = [True, False]
        for i in range(self.count):
            radius = random.randint(5,20)
            x = random.randint(0,self.width-(radius*2))
            y = random.randint(0,self.height-(radius*2))
            speedx = random.randint(-20,20)
            speedy = random.randint(-20,20)
            color = colors[random.randint(0,len(colors)-1)]
            bounce = random.randint(0,1)
            self.list_of_atoms.append(Atom(x,y,speedx,speedy,radius,color,bounce))
        pass

    def tick(self):
        """This method is called by playground. Sends a tuple of atoms to rendering engine.

        :param size_x: world size x dimension
        :param size_y: world size y dimension
        :return: tuple of atom objects, each containing (x, y, radius) coordinates 
        """
        tuples = ()
        for atom in self.list_of_atoms:
            atom.move(self.width,self.height)
            tuples = tuples + ((atom.x, atom.y, atom.radius, atom.color),)
        return tuples


if __name__ == '__main__':
    size_x, size_y = 700, 400

    world = ExampleWorld(size_x, size_y,20)
    playground.run((size_x, size_y), world)
