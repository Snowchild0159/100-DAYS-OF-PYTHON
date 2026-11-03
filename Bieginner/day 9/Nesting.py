#nesting list inside dictionary
travel_log = { 
    "France" : ["Paris" , "Lille" , "Dijon"],
    "Germany" : ["Stuttgart" , "Munchen" , "Hamburg" , "Berlin"]
}


#nesting dictionary inside dictionary
travel_log2= { 
    "France" : {"city_visited" : ["Paris" , "Lille" , "Dijon"] , "total_visits" : 12},
    "Germany" : {"city_visited" : ["Stuttgart" , "Munchen" , "Hamburg" , "Berlin"] , "total_visits" : 4 }
}


#nesting dictionary inside list
travel_log3 = [
    {
        "country": "France",
        "city_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "city_visited": ["Stuttgart", "Munchen", "Hamburg", "Berlin"],
        "total_visits": 4
    },
    {
        "country": "USA",
        "city_visited": ["New York", "Los Angeles", "Chicago"],
        "total_visits": 8
    },
    {
        "country": "Japan",
        "city_visited": ["Tokyo", "Kyoto", "Osaka"],
        "total_visits": 5
    }
]

def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["total_visits"] = visits
    new_country["city_visited"] = cities
    travel_log3.append(new_country)



add_new_country("russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log3)