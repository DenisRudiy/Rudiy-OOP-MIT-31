class Tank:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def shoot(self):
        return f"{self.name} shoots {self.gun.fire()}"

    def move(self):
        return f"{self.name} is drive"

class Gun:
    def __init__(self, firepower):
        self.firepower = firepower

    def fire(self):
        return f"from {self.firepower}"

class LightTank(Tank):
    def __init__(self, name):
        super().__init__(name, Gun("Light Cannon"))

class MediumTank(Tank):
    def __init__(self, name):
        super().__init__(name, Gun("Medium Cannon"))
    
    def rotate(self, angle):
        return f"{self.name} rotate at {angle}deg"

class HeavyTank(Tank):
    def __init__(self, name):
        super().__init__(name, Gun("Heavy Cannon"))

    def defend(self):
        pass

light_tank_1 = LightTank("L Tank 1")
print(light_tank_1.shoot())

medium_tank_1 = MediumTank("M Tank 1")
print(medium_tank_1.shoot())
print(medium_tank_1.rotate(90))

heavy_tank_1 = HeavyTank("H Tank 1")
print(heavy_tank_1.shoot())

tank = Tank("Tank", Gun("Cannon"))