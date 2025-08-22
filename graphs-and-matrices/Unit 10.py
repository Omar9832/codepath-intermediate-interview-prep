
flights={'JFK':['LAX', 'DFW'], 'LAX': ['JFK'],'DFW': ['ATL', 'JFK'], 'ATL': ['DFW'] }
print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])


def get_adj_dict(flights):
    flights_dict={}
    for a, b in flights:
        if a not in flights_dict:
            flights_dict[a]=[]
        if b not in flights_dict:
            flights_dict[b]=[]
        flights_dict[a].append(b)
        flights_dict[b].append(a)
    return flights_dict
        




flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))