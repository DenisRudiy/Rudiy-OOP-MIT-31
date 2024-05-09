from abc import ABC, abstractmethod

class TrainWagon(ABC):
    def __init__(self):
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    def get_passengers(self):
        return self.passengers

    @abstractmethod
    def label(self):
        pass

class CompartmentWagon(TrainWagon):
    def label(self):
        return "K"

class PlatWagon(TrainWagon):
    def label(self):
        return "P"

class Train:
    length = 0

    def __init__(self):
        self.cars = []

    def __add__(self, car):
        self.cars.append(car)

    def __setitem__(self, car_number, passenger):
        car = self.cars[car_number]
        car.add_passenger(passenger)

    def __delitem__(self, key):
        car_number, passenger_name = key
        car = self.cars[car_number]
        car.remove_passenger(passenger_name)

    def __str__(self):
        train_str = ""
        for i, car in enumerate(self.cars):
            train_str += f"Wagon {i+1}: {car.label()}\n"
        return train_str

    def __getitem__(self, car_number):
        car = self.cars[car_number]
        passengers = car.get_passengers()
        passengers_str = ""
        for i in range(len(passengers)):
            passengers_str += f"{i+1}: {passengers[i]}\n"
        return passengers_str



active = True
train = Train()
while (active == True):
    print(" 'w' to add a wagon  \n 'a to add a passenger \n 's' to show a passengers \n 'r' to remove a passenger \n 'v' to view all train wagons \n 'q' to quit: ")
    action = input("Enter action: ")
    if (action == 'q'):
        break
    elif(action == 'w'):
        if((Train.length)%2 == 0):      
            train + CompartmentWagon()
        else:
            train + PlatWagon()
        print("") 
        print(train)
        print("")
        Train.length += 1
    elif(action == 'v'):
        print("") 
        print(train)
    elif(action == 'a'):
        print("") 
        number = int(input("Enter wagon number: "))
        if (number >= Train.length):
            print("Wagon doesn't exist \n")
        else:
            name = input("Enter passenger name: ")
            train[number] = name
            print("")
            print(train[number])
            print("")
    elif(action == 's'):
        print("")
        for i in range(train.length):
            print(f"Wagon {i+1}: \n", train[i])
        print("")
    elif(action == 'r'):
        print("") 
        number = int(input("Enter wagon number: "))
        if(number > Train.length):
            print("Wagon doesn't exist \n")
        else: 
            name = input("Enter passenger name: ")
            del train[number, name]
            print("")
            print(f"Wagon {number+1}: \n", train[number])
            print("")