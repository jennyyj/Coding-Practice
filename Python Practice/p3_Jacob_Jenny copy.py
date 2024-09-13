import random
import time
import matplotlib.pyplot as plt

class Island(object):
    def __init__(self, n, prey_count=0, predator_count=0, human_count=0):
        self.grid_size = n
        self.grid = []
        for i in range(n):
            row = [0] * n
            self.grid.append(row)
        self.init_animals(prey_count, predator_count, human_count)

    def init_animals(self, prey_count, predator_count, human_count):
        count = 0
        while count < prey_count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                new_prey = Prey(island=self, x=x, y=y)
                self.register(new_prey)
                count += 1

        count = 0
        while count < predator_count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                new_predator = Predator(island=self, x=x, y=y)
                self.register(new_predator)
                count += 1

        count = 0
        while count < human_count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if not self.animal(x, y):
                new_human = Human(island=self, x=x, y=y)
                self.register(new_human)
                count += 1
    def count_predators(self):
        count = 0
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                animal = self.animal(x, y)
                if animal and isinstance(animal, Predator):
                    count += 1
        return count

    def count_humans(self):
        count = 0
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                animal = self.animal(x, y)
                if animal and isinstance(animal, Human):
                    count += 1
        return count

    def clear_all_moved_flags(self):
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if self.grid[x][y]:
                    self.grid[x][y].clear_moved_flag()

    def size(self):
        return self.grid_size

    def register(self, animal):
        x = animal.x
        y = animal.y
        self.grid[x][y] = animal

    def remove(self, animal):
        x = animal.x
        y = animal.y
        self.grid[x][y] = 0

    def animal(self, x, y):
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            return self.grid[x][y]
        else:
            return -1

    def __str__(self):
        s = ""
        for j in range(self.grid_size - 1, -1, -1):
            for i in range(self.grid_size):
                if not self.grid[i][j]:
                    s += "{:<2s}".format('.' + " ")
                else:
                    s += "{:<2s}".format((str(self.grid[i][j])) + " ")
            s += "\n"
        return s


class Animal(object):
    def __init__(self, island, x=0, y=0, s="A"):
        self.island = island
        self.name = s
        self.x = x
        self.y = y
        self.moved = False

    def position(self):
        return self.x, self.y

    def __str__(self):
        return self.name

    def check_grid(self, type_looking_for=int):
        offset = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        result = 0
        for i in range(len(offset)):
            x = self.x + offset[i][0]
            y = self.y + offset[i][1]
            if not 0 <= x < self.island.size() or not 0 <= y < self.island.size():
                continue
            if type(self.island.animal(x, y)) == type_looking_for:
                result = (x, y)
                break
        return result

    def move(self):
        if not self.moved:
            location = self.check_grid(int)
            if location:
                self.island.remove(self)
                self.x = location[0]
                self.y = location[1]
                self.island.register(self)
                self.moved = True

    def breed(self):
        if self.breed_clock <= 0:
            location = self.check_grid(int)
            if location:
                self.breed_clock = self.breed_time
                the_class = self.__class__
                new_animal = the_class(self.island, x=location[0], y=location[1])
                self.island.register(new_animal)

    def clear_moved_flag(self):
        self.moved = False


class Prey(Animal):
    breed_time = 3

    def __init__(self, island, x=0, y=0, s="O"):
        Animal.__init__(self, island, x, y, s)
        self.breed_clock = self.breed_time
    
    
    def clock_tick(self):
        ''' Prey only updates its local breed clock '''
        self.breed_clock -= 1
        # print('Tick Prey {},{}, breed:{}'.format(self.x, self.y, self.breed_clock))


class Predator(Animal):
    breed_time = 6
    starve_time = 3

    def __init__(self, island, x=0, y=0, s="X"):
        Animal.__init__(self, island, x, y, s)
        self.starve_clock = self.starve_time
        self.breed_clock = self.breed_time

    def clock_tick(self):
        self.breed_clock -= 1
        self.starve_clock -= 1
        if self.starve_clock <= 0:
            self.island.remove(self)

    def eat(self):
        if not self.moved:
            location = self.check_grid(Prey)
            if location:
                prey = self.island.animal(location[0], location[1])
                self.island.remove(prey)
                self.island.remove(self)
                self.x = location[0]
                self.y = location[1]
                self.island.register(self)
                self.starve_clock = self.starve_time
                self.moved = True


class Human(Animal):
    hunt_time = 5
    starve_time = 10
    breed_time = 8

    def __init__(self, island, x=0, y=0, s="H"):
        Animal.__init__(self, island, x, y, s)
        self.starve_clock = self.starve_time
        self.breed_clock = self.breed_time
        self.hunt_clock = self.hunt_time

    def clock_tick(self):
        self.breed_clock -= 1
        self.starve_clock -= 1
        self.hunt_clock -= 1
        if self.starve_clock <= 0:
            self.island.remove(self)

    def hunt(self):
        if not self.moved and self.hunt_clock <= 0:
            location = self.check_grid(Prey)
            if location:
                prey = self.island.animal(location[0], location[1])
                self.island.remove(prey)
                self.hunt_clock = self.hunt_time
                self.moved = True


def main(predator_breed_time=6, predator_starve_time=3, initial_predators=10,
         prey_breed_time=3, initial_prey=50, human_breed_time=8, initial_humans=5,
         human_hunt_time=5, size=10, ticks=1000):
    Predator.breed_time = predator_breed_time
    Predator.starve_time = predator_starve_time
    Prey.breed_time = prey_breed_time
    Human.breed_time = human_breed_time
    Human.hunt_time = human_hunt_time

    predator_list = []
    prey_list = []
    human_list = []

    isle = Island(size, initial_prey, initial_predators, initial_humans)
    print(isle)

    for i in range(ticks):
        isle.clear_all_moved_flags()

        for x in range(size):
            for y in range(size):
                animal = isle.animal(x, y)
                if animal:
                    if isinstance(animal, Predator):
                        animal.eat()
                        animal.move()
                        animal.breed()
                        animal.clock_tick()
                    elif isinstance(animal, Human):
                        animal.hunt()
                        animal.move()
                        animal.breed()
                        animal.clock_tick()
                    else:
                        animal.move()
                        animal.breed()
                        animal.clock_tick()
                        
        prey_count = isle.count_humans()
        predator_count = isle.count_predators()
        human_count = isle.count_humans()

        prey_list.append(prey_count)
        predator_list.append(predator_count)
        human_list.append(human_count)

        if prey_count == 0:
            print('Lost the Prey population. Quitting.')
            break
        if predator_count == 0:
            print('Lost the Predator population. Quitting.')
            break
        if human_count == 0:
            print('Lost the Human population. Quitting.')
            break

        if not i % 10:
            print(f"Tick {i}: Prey={prey_count}, Predators={predator_count}, Humans={human_count}")

    plt.plot(prey_list, label='Prey')
    plt.plot(predator_list, label='Predators')
    plt.plot(human_list, label='Humans')
    plt.legend()
    plt.show()

    print(isle)

if __name__ == "__main__":
    main()
