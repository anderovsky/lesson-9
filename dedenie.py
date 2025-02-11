class Vehicle:
    def __init__(self, VehicleId, VehicleName, Type):
        self.VehicleID = VehicleId
        self.VehicleName = VehicleName
        self.Type = Type

    def vozidlo(self):
        print(f"Tvoje vozidlo je: {self.VehicleID}, {self.VehicleName}, {self.Type}")

class Car(Vehicle):
    def __init__(self, VehicleId, VehicleName, Type, carModel):
        super().__init__(VehicleId, VehicleName, Type, carModel)
        self.carModel = carModel

class Bus(Vehicle):
    def __init__(self, VehicleId, VehicleName, Type, busModel):
        super().__init__(VehicleId, VehicleName, Type, busModel)
        self.carModel = busModel

toyota = Vehicle(VehicleId="BA-123_CL", VehicleName="Toyota", Type="Avensis")

toyota.vozidlo()

# vime volat iba atributy a metody - nie triedy