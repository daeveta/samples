import json

people = {111111: ('Sam', 22), 222222: ('Adam', 24), 333333: ('Jasy', 34), 444444: ('Tom', 18), 555555: ('Lucy', 23)}

with open("homework6.3.1.json", "w") as people_j:
    json.dump(people, people_j)




