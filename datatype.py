# Datatypes

number = 100  # int
second = 53.6  # Float
Text = "Hey There"  # String
ispythoniniteresting = True  # Boolean

Cars = ['Toyota', 'Nissan', 'BMW']  # List
Fruits = ('Apple', 'Orange', 'Banana')  # Tuple
Countries = {"Kenya", "Tanzania", "Sudan", "Portugal"}  # Set
details = {
    "FirstName": "Dulgan",
    "Age": "24",
    "Nationality": "Sudanese"
}  # Dictionary

print(Cars)
print(Fruits)
print(Countries)
print(details["FirstName"])
print(details["Age"])

# Determine the Datatype
print(type(Text))
print(type(Cars))
print(type(Fruits))
print(type(details))
print(type(Countries))

# TypeCasting (Converting Datatypes)
print(float(number)) # Covert whole Number into Float
print(int(second)) # Covert Float into whole Number
