class Point():
    def __init__(self,input1,input2):
        self.x = input1
        self.y = input2

p = Point(2,8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self,name):
        print(name)
        if self.open_seats() == 0:
            return False
        self.passenger.append(name)
        return True

    def open_seats(self):
        print(self.capacity-len(self.passenger))
        return self.capacity - len(self.passenger)

flight = Flight(3)
people = ["Harry","Ron","Hermione","Ginny","Lily"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to the flight")
    else:
        print(f"No available seats for {person}")