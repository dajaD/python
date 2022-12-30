def liters_100km_to_miles_gallon(liters):
    miles = 100 * 1000/1609.344
    gallons = liters / 3.78541178
    return miles / gallons
#
# Write your code here.
#

def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    kilo = miles * 1609.344 / 1000
    km100 = kilo / 100
    return liters / km100
#
# Write your code here
#

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
