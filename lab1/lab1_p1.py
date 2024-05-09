import math

class Length():
    allData = []
    total_lengths = 0 
    CONVERSION_FACTORS = {
        'mm': {'cm': 0.1, 'm': 0.001, 'km': 0.000001},
        'cm': {'m': 0.01, 'km': 0.00001},
        'm': {'km': 0.001},
        'km': {'km': 1}
    }

    @staticmethod
    def get_total_lengths():
        return 'Total length is: ' + f"{Length.total_lengths}"

    def convert_to(self, target_type, diff):
        conversion_factor = self.CONVERSION_FACTORS[self.type][target_type]
        return Length(self.value * conversion_factor, target_type, diff)
        

    def __init__(self, value, type, diff):
        self.value = value
        self.type = type
        self.diff = diff
        Length.allData.append(self)
        Length.total_lengths += 1 

    def __str__ (self):
        return 'Length is: ' + str(self.value) + str (self.type)

    def __add__ (self, other):
        if self.type == other.type:
            return Length(self.value + other.value, self.type, self.diff)
        elif self.type != other.type:
            if (self.diff > other.diff):
                converted_other = other.convert_to(self.type, self.diff)
                return Length(self.value + converted_other.value, self.type, self.diff)
            elif (self.diff < other.diff):
                converted_self = self.convert_to(other.type, other.diff)
                return Length(other.value + converted_self.value, other.type, other.diff)
            else:
                return 'Wrong type!'

    def __sub__(self, other):
        if self.type == other.type:
            return Length(self.value - other.value, self.type, self.diff)
        elif self.type != other.type:
            if (self.diff > other.diff):
                converted_other = other.convert_to(self.type, self.diff)
                return Length(self.value - converted_other.value, self.type, self.diff)
            else:
                return 'You try to subtract bigger number from smaller!'

    def __mul__(self, number):
        self.value = self.value * number
        return self

    def __truediv__ (self, number):
        if (number != 0):
            self.value = self.value / number
            return self
        else:
            print('Warning! You are trying to divide by zero!')

    def __floordiv__  (self, number):
        if (number != 0):
            self.value = self.value // number
            return self
        else:
            print('Warning! You are trying to divide by zero!')

    def round(self, direction):
        if(direction == "up"):
            self.value = math.ceil(self.value)
            print('Length is:', self.value, self.type)
        if(direction == "down"):
            self.value = math.floor(self.value)
            print('Length is:', self.value, self.type)


    

# * Create "Lengths"
length1 = Length(5, 'mm', 1)
length2 = Length(10, 'cm', 2)
length3 = Length(3, 'm', 3)
length4 = Length(2, 'km', 4)

# * Make operations
print(length1)
print(length2)
print(length3)
print(length4)

print('\n')
length5 = length2 + length1
print(length5)

length6 = length2 - length1
print(length6)

length7 = length2 * 2
print(length7)

length8 = length1 / 2
print(length8)

all_length = Length.get_total_lengths()
print(all_length)