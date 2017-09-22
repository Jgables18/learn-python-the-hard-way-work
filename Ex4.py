# assigns a value to the number of cars
cars = 100
# assigns a value to sapce in a car
space_in_a_cars = 4.0
# assigns a value to the number of drivers
drivers = 30
# assigns a value to the number of passengers
passengers = 90
# The number of car minus the number of drivers, which gives the number of left over cars
cars_not_driven = cars - drivers
# The number of cars driven is the same as the number of drivers
cars_driven = drivers
# The number of cars that can be driven multiplied by the number of people they can drive
carpool_capacity = cars_driven * space_in_a_cars
# Is the averge number of passengers per car, total nuber of passengers divided by the number of cars being driven
average_passengers_per_cars = passengers / cars_driven

# displays the words "There are (the number of cars) available"
print "There are", cars, "cars available."
# displays the words "There are only (the number of drivers) drivers available"
print "There are only", drivers, "drivers available."
# displays the words "There will be ( number of not driven cars) empty cars today "
print "There will be", cars_not_driven, "empty cars today."
# displays the words "we can transport (The total number of passengers that can be taken) people today"
print "We can transport", carpool_capacity, "people today."
# displays the words "we have ( number of passengers) to carpool today"
print "We have", passengers, "to carpool today."
# We need to put about ( average number of people per car) in each car
print "We need to put about", average_passengers_per_cars, "in each car."
