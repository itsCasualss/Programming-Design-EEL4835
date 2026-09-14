#Intro to Tuples .. Lists = [] whilte Tuples = ().
wh40k_locations = [
    ("Hive City", (-10.7625, 55.8310)),
    ("Macragge's Honour", (0.0000, -0.0012)),
    ("The Fang", (75.3652, 39.7625)),
    ("Terra", (41.9028, 12.4964)),
    ("Krieg", (-77.0369, 38.9072))
]
# Accessing coordinates and city names
for location, coords in wh40k_locations:
    print(f"{location} Coordinates: {coords}")
    #the 'f' [called: f-string] is important after the print function so it recalls the
    #variables from the Tuple, and must be recaled with the {} brackets.

