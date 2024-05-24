class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    

    def show(self):
        return f"Vehicle name:{self.name} Speed:{self.max_speed} Mileage:{self.mileage}"
    

Bus=(Vehicle("School Volvo",180,12))
print(Bus.show())

        


