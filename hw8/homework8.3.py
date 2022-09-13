class Weapon():
    def __init__(self, barrel_size=0):
        self.barrel = barrel_size

    def __gt__(self, other):
        print('Which barrel is bigger?')
        print('My barrel is', self.barrel)
        print('Others barrel is', other.barrel)
        return self.barrel - other.barrel

    def load(self):
        raise NotImplemented

    def shoot(self):
        raise NotImplemented


class Gun(Weapon):
    @staticmethod
    def shoot():
        print('*BANG!*')


class Rifle(Weapon):
    @classmethod
    def shoot(self):
        print(self)
        print('BAAANG!!!')


class Minigun(Rifle, Gun):
    def mro(self):
        return (Minigun, Gun, Rifle, Weapon)

    def shoot(self):
        for i in range(3):
            super().shoot()


Gun.shoot()
mg = Minigun()
gun = Gun(5)
Rifle.shoot()
rifle = Rifle(4)

result = rifle.barrel - gun.barrel
print(abs(result))

#print(rifle - gun)

#for current_gun in [gun, rifle]:
#    current_gun.shoot()
#mg.shoot()

#print(gun.shoot(), rifle.shoot())
#print(type(a_gun))
#print(Minigun.__mro__)
