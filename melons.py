# melon_names = {
#     1: 'Honeydew',
#     2: 'Crenshaw',
#     3: 'Crane',
#     4: 'Casaba',
#     5: 'Cantaloupe',
# }

# melon_prices = {
#     1: 0.99,
#     2: 2.00,
#     3: 2.50,
#     4: 2.50,
#     5: 0.99,
# }

# melon_seedlessness = {
#     1: True,
#     2: False,
#     3: False,
#     4: False,
#     5: False,
# }

# flesh_color = { 1: 'red',
#     2: 'orange',
#     3: 'yellow',
#     4: 'green',
#     5: 'red'

# }

# rind_color = { 1: 'pink',
#     2: 'orange',
#     3: 'yellow',
#     4: 'pink',
#     5: 'red'

# }

# average_weight = {1: '1 pound',
#     2: '3 pounds',
#     3: '3.6 pounds',
#     4: '2 pounds',
#     5: '2.7 pounds'



melons = { "Honeydew": {"melon_price" : 0.99,
                     "melon_seedlessness": False,
                     "flesh_color": "green",
                     "rind_color": "beige",
                      "average_weight": "1 pound"}
                      ,
        "Crenshaw": {"melon_price" : 2.00,
                     "melon_seedlessness": True,
                     "flesh_color": "orange",
                     "rind_color": "orange",
                      "average_weight": "3 pounds"}
                      ,
        "Crane": {"melon_price" : 2.50,
                     "melon_seedlessness": False,
                     "flesh_color": "yellow",
                     "rind_color": "yellow",
                      "average_weight": "3.6 pounds"} }

for attribute, value in melons.items():
        print(f"{attribute} : {value}")