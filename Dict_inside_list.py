#we have list with 2 dicts nested inside. we want to write func that will be able 
#to add more dicts to the same list (called travel_log)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#to be added to the travel_log.
#we define a func with 3 input 
def add_new_country(name, visit_count, cities_visited):
    #we define empty dict then:
    #we creating new keys which getting their valurs from the input.
    #each line of code 24-26 we adding new key -by the vlue on the string which we giving 
    #and the value which given by user input ,then we append this dict to the list of the dicts 
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_count
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#each dict in the list contains 3 pairs of key value 