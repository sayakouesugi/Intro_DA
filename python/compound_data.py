elements = {"hydrogen": {"number": 1, 
                         "weight": 1.000794,
                         "symbol": "H"},
            "helium": {"number" : 2, 
                        "weight": 4.003602,
                        "symbol": "He"}}
helium = elements["helium"]
print(helium)

hydrogen_weight = elements["hydrogen"]["weight"]

print(hydrogen_weight)

oxygen = {"number": 8, "weight":15.999, "symbol": "O"} # create a new oxygen dictionary
elements["oxygen"] = oxygen #assign 'oxygen' as a key to the elements dictionary

print('elements = ', elements)
