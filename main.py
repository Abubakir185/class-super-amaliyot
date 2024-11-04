class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def get_status(self):
        return f"health: {self.health}, damage: {self.damage}, speed: {self.speed}"
    
    def take_damage(self, other_char):
        if (self.health > other_char.damage):
            self.health -= other_char.damage
            self.speed *= 0.8
            self.damage *= 0.7
        else:
            self.health = 0
        
    def attact(self, other_char):
        if (self.health > 0): 
            other_char.take_damage(self)


class Halk(Character):
    def __init__(self):
        super().__init__(1000, 200, 25)

    def recovery(self):
        self.health *= 1.3


class Iron_Man(Character):
    def __init__(self):
        super().__init__(500, 300, 50)


halk = Halk()
iron_man = Iron_Man()

print(halk.get_status())
iron_man.attact(halk)
print(halk.get_status())
halk.recovery()
print(halk.get_status())
