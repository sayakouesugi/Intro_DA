"""A tuple is another useful container. It's a data type fr immutable ordered sequennce of elements. They are often used to store related pieces of information."""

location = (13.4125, 103.86667)
print("Latitude:", location[0])
print("Longtitude", location[1])



dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} * {} * {} ".format(length, width, height))


length, width, height = 52, 40, 100

print("The dimensions are {} * {} * {}".format(length, width, height))
