#TASK 1
class City:
    def __init__(self, name, population=0, connectedCities=[],):
        self.name = name
        self.population = population
        self.connectedCities = connectedCities #list of city objects
    
    def setPopulation(self, population):
        self.population = population
    
    def addConnectedCities(self, city):
        self.connectedCities.append(city)




#TASK 3
def archipelagoCount(arr):
    #revision: switched from bfs to dfs
    def dfs(city):
        visited.add(city.name)
        for cc in graph[city.name].connectedCities:
            if cc not in visited:
                dfs(graph[cc])

    if len(arr) < 1:
        raise AssertionError('list of cities cannot be len 0')
    islands = 0
    visited = set()
    for city in arr:
    #revision: since highways are bi-directional, if any of their connected cities are visited,
    # then we can consider cities which have no other cities mapping to them in the text file as visited
        for cc in city.connectedCities:
            if cc in visited:
                visited.add(city.name)
                break

        if city.name not in visited:
            islands += 1
            dfs(city)
    return islands


#cities that have no previous cities mapping to them in the text file
# Philadelphia
# Indianapolis
# Overland Park
# Murfreesboro
# Pearland
# Dothan
# Kissimmee
# Santee
# Anderson
# Euless
# Grapevine
# East Providence
# Glenview
# Prescott
# Carol Stream
# Bozeman
# The Colony
# Montclair
# Dover

#TASK 4
def archipelagoPopulation(arr):
    #revision: switched from bfs to dfs; similarly to task 3
    def dfs(city):
        visited.add(city.name)
        population[city.name] = (int(city.population))
        for cc in graph[city.name].connectedCities:
            if cc not in visited:
                dfs(graph[cc])

    if len(arr) < 1:
        raise AssertionError('list of cities cannot be len 0')
    
    population = {}
    visited = set()
    for city in arr:

        if city.name not in visited:
            dfs(city)
    
    # c = city name, p = population
    return [(c, p) for c, p in population.items()]
    


#TASK 5
def uniqueHighways(city1, city2):
    if city1.name == None or city2.name == None:
        raise AssertionError('Cities must have names')
    minPath = 0
    # bfs
    visited = set()
    q = []

    q.append(city1.name)
    visited.add(city1.name)
    while len(q) > 0:
        for i in range(len(q)): #each level of the graph perform pops from queue
            city = q.pop(0)
            if city == city2.name:
                return minPath
                
            for cc in graph[city].connectedCities: 
                if cc not in visited:
                    q.append(cc)
                    visited.add(cc)

            for cc in graph[city2.name].connectedCities: #considering bidirectional cities
                if cc in visited:
                    return minPath + 2 #add 2: 1 to finish current level and 1 to account for next level

        minPath += 1
    raise AssertionError('No highways connected between islands')



if __name__ == "__main__":
    #TASK 2

    adjacencyCities = {} #dictionary of all cities and their connected cities
    cityPopulations = {}

    #building adjancencyCities dictionary
    with open("road_network.txt", "r") as file:
        for line in file:
            data = line.strip().split(" : ") 
            city_name, connected_city = data[0], data[1]
            
            if city_name not in adjacencyCities:
                adjacencyCities[city_name] = [connected_city]
            else:
                adjacencyCities[city_name].append(connected_city)
    file.close()

            
    # #building cityPopulations dictionary
    with open("city_population_no_dup.txt", "r") as file:
        for line in file:
            data = line.strip().split(" : ")
            city_name, city_population = data[0], data[1]

            cityPopulations[city_name] = city_population

    file.close()



    # building graph
    graph = {} #"New York": NY OBJ ("New York", pop, [adj city names strings])
    for city in cityPopulations: #some cities don't point to others, but we still need to add to our graph to reference it later
        c = City(city, cityPopulations[city], adjacencyCities.get(city, []))
        graph[city] = c

        
    citiesList = list(graph.values())
    

    print("Islands:", archipelagoCount(citiesList)) #1 island

    print(archipelagoPopulation(citiesList)) #return [(city name: 6000), (city name: 7000)...]

    print("New York -> Warwick:", uniqueHighways(graph["New York"], graph["New York"])) #0
    print("New York -> Warwick:", uniqueHighways(graph["New York"], graph["Warwick"])) #1
    print("New York -> Monroe:", uniqueHighways(graph["New York"], graph["Monroe"])) #5 
    print("New York -> Hoover:", uniqueHighways(graph["New York"], graph["Hoover"])) #6 //New York -> Hoover should be 6 
    print("Citrus Heights -> Euless:", uniqueHighways(graph["Citrus Heights"], graph["Euless"])) #3 requires bidirectional checks
    print("Inglewood -> Lodi:", uniqueHighways(graph["Inglewood"], graph["Lodi"])) #2 //Inglewood -> Greenville -> Lodi
    print("Apple Valley -> Florissant:", uniqueHighways(graph["Apple Valley"], graph["Florissant"])) #3 //Apple Valley -> Hanford -> Weymouth Town -> Florissant
    print("Dover -> Harlingen:", uniqueHighways(graph["Dover"], graph["Harlingen"])) #2 //Dover -> Roswell -> Harlingen
    print("Dover -> Roswell:", uniqueHighways(graph["Dover"], graph["Roswell"])) #1 //Dover -> Grand Island -> Yucaipa -> Evanston -> Owensboro -> Spokane Valley -> Harlingen -> Roswell, but Dover -> Roswell
    
