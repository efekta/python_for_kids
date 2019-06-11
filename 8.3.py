# Функции, вызывающие другие функции

class Things:
    pass

class Inanimate(Things):
    pass



class Animate(Things):
    def breathe(self):
        print('Дышит')
    def move(self):
        print('Двигается')
    def eat_food(self):
        print('Ест')



class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    pass


class Mammals(Animals):
    def feed_young_with_milk(self):
        print('Кормит детенышей молоком')



class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('Ест листья')



reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()


harold = Giraffes()
harold.move()






















