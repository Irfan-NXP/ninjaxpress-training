# CLASS
class Car:
    def __init__(self, color, brand, type):
        self.color = color
        self.brand = brand
        self.type = type
        self.jumlah_roda = 4
        self.bbm = 'bensin'
    
    def display_car_info(self):
        print('The car color is', self.color)
        print('The car brand is', self.brand)
        print('The car type is', self.type)
        print('The car tire is', self.jumlah_roda)
        print('The car bbm is', self.bbm)

c1 = Car('Red', 'Ford', 'Mustang')
c2 = Car('Blue', 'Toyota', 'Prius')
c3 = Car('Green', 'Honda', 'Brio')

c3.setbrand('Wuling')
c3.display_car_info()