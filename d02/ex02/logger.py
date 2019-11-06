import time
import getpass
import os.path
from os import path
from random import randint


def log(func):
    t = time.time()
    line = f"({getpass.getuser()})Running: {func.__name__}\t\t\t[ exec-time = {t:2.2f} ]"
    f = open('machine.log', 'a+')
    f.write(line + '\n')
    f.close()
    return func

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
     if self.water_level > 20:
         return True
     else:
         print("Please add water!")
         return False
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
