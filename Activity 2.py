class Vechicle:
    
    def __init__(self, max_speed, milage):

        self.max_speed = max_speed
        self.milage = milage

Hundai = Vechicle(240, 20)
print('Hundai max speed: ', Hundai.max_speed)
print('Hundai milage: ', Hundai.milage)