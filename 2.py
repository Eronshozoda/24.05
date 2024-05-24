class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    

    def seating_capasity(self,capasity):
        return f"The siting of capasity of a {self.name} is {capasity} passengers"
    

Bus=(Vehicle("Volvo",120,40))
print(Bus.seating_capasity(50))

        


