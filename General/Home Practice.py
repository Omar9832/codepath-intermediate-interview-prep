import random
from collections import deque





def max_audience_performances(audiences):
    i=0
    max=audiences[i]
    while i<len(audiences):
        if audiences[i]>max:
            max=audiences[i]
        i=i+1
        
    return audiences.count(max)*max

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))


def lineup(artists, set_times):
    dict={}
    i=0
    while i<len(artists):
        dict[artists[i]]=set_times[i]
        i=i+1
    return dict



artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

     
     
     
def get_artist_info(artist, festival_schedule):
 
    j=0
    while j<len(festival_schedule):
        if artist in festival_schedule:
            return festival_schedule.get(artist)
        j=j+1
    return {'message': 'Artist not found'}

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule)) 

def total_sales(ticket_sales):
    sum=0
    for x in ticket_sales.values():
        sum=sum+x
    return sum


ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))


def identify_conflicts(venue1_schedule, venue2_schedule):
    dict2={}
    for key in venue1_schedule.keys():
        print(key)
        print(venue1_schedule.get(key))
        if key in venue2_schedule and venue1_schedule[key] in venue2_schedule.values():
            
            dict2[key]=venue1_schedule[key]
    return dict2

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))


def best_set(votes):
    dict3={}
    for artist in votes.values():
        dict3[artist]=0

    for artist in votes.values():
        dict3[artist]=dict3.get(artist)+1
    
    max=0
    name=""
    for x in dict3.keys():
        if dict3[x]>max:
            max=dict3[x]
            name=x
    return name
    





votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))

def space_crew(crew, position):
    exp_dict={}
    i=0
    while i<len(crew):
        exp_dict[crew[i]]=position[i]
        i=i+1
    return exp_dict


exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

print(space_crew(exp70_crew, exp70_positions))
print(space_crew(ax3_crew, ax3_positions))




def planet_lookup(planet_name):
    for planet in planetary_info.keys():
        if planet_name==planet:
           return f"Planet {planet_name} has an orbital period of {planetary_info[planet_name]['Orbital Period']} Earth days and has {planetary_info[planet_name]['Moons']} moons."

    return "Sorry, I have no data on that planet."


planetary_info = {
    "Mercury": {
        "Moons": 0,
        "Orbital Period": 88
    },
    "Earth": {
        "Moons": 1,
        "Orbital Period": 365.25
    },
    "Mars": {
        "Moons": 2,
        "Orbital Period": 687
    },
    "Jupiter": {
        "Moons": 79,
        "Orbital Period": 10592
    }
}

print(planet_lookup("Jupiter"))
print(planet_lookup("Pluto"))
              

def check_oxygen_levels(oxygen_levels, min_val, max_val):
    oxygen_list=[]
    for x in oxygen_levels.keys():
        if oxygen_levels.get(x)<min_val or oxygen_levels.get(x)>max_val:
            oxygen_list.append(x)
    return oxygen_list


oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
}

min_val = 19
max_val = 22

print(check_oxygen_levels(oxygen_levels, min_val, max_val))


def data_difference(experiment1, experiment2):
    data_dict={}
    for experiment in experiment1.keys():
        if experiment not in experiment2.keys() or experiment1.get(experiment) not in experiment2.values():
            data_dict.update({experiment: experiment1.get(experiment)})
    return data_dict

exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

print(data_difference(exp1_data, exp2_data))

def get_winner(votes):
    names_dict=dict.fromkeys(votes, 0)
    i=0
    while i<len(votes):
        names_dict[votes[i]]=names_dict[votes[i]]+1
        i=i+1
    max_name=""
    max_val=-999
    for x in names_dict.keys():
        if names_dict.get(x)>max_val:
            max_val=names_dict.get(x)
            max_name=x
    return max_name


    



votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

print(get_winner(votes1))
print(get_winner(votes2))


def check_if_complete_transmission(transmission):
    if len(transmission)>=26:
        for x in transmission:
            if not transmission.count(x)>=1:
                return False
        return True
    else:
        return False


transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"

print(check_if_complete_transmission(transmission1))
print(check_if_complete_transmission(transmission2))





def max_number_of_string_pairs(signals):
    pairs=0
    i=0
    j=0
    while i<len(signals):
        while j<len(signals):
            if signals[i]==signals[j][::-1]:
                pairs=pairs+1
            j=j+1
        i=i+1

    return pairs


signals1 = ["cd", "ac", "dc", "ca", "zz"]
signals2 = ["ab", "ba", "cc"]
signals3 = ["aa", "ab"]

print(max_number_of_string_pairs(signals1))
print(max_number_of_string_pairs(signals2))
print(max_number_of_string_pairs(signals3))

def total_treasures(treasure_map):
    total=0
    for x in treasure_map.values():
        total=total+x
    return total


treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 



def find_duplicate_chests(chests):
    
    treasures_ocurances=dict.fromkeys(chests, 0)
    i=0
    while i<len(chests):
        treasures_ocurances[chests[i]]=treasures_ocurances[chests[i]]+1
        i=i+1
    duplicates=[]
    for x in treasures_ocurances.keys():
        if treasures_ocurances.get(x)==2:
            duplicates.append(x)
    return duplicates

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

def is_balanced(code):
    removal=1
    i=0
    code_dict={}
    while i<len(code):
        if code[i] not in code_dict:
            code_dict[code[i]]=code.count(code[i])
            if code_dict.get(code[i])>1 and removal!=0:
                code_dict[code[i]]=code_dict[code[i]]-1
                removal=removal-1
        i=i+1
    for x in code_dict.keys():
        if code_dict.get(x)!=1:
            return False
    return True




        


code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 


def find_treasure_indices(gold_amounts, target):
    i=0
    j=0
    while i<len(gold_amounts):
        j=0
        while j<len(gold_amounts):
            print(gold_amounts[i]+gold_amounts[j])
            if i!=j and (gold_amounts[i]+gold_amounts[j])==target:
                return [i, j]
            j=j+1
        i=i+1
    return -1


gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))
   



def analyze_library(library_catalog, actual_distribution):
    analyze_dict={}
    for x in library_catalog.keys():
        analyze_dict[x]=actual_distribution.get(x)-library_catalog.get(x)
    return analyze_dict


library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


print(analyze_library(library_catalog, actual_distribution))
      

def find_common_artifacts(artifacts1, artifacts2):
    i=0
    common_artifacts=[]
    while i<len(artifacts1):
        if artifacts1[i] in artifacts2:
            common_artifacts.append(artifacts1[i])
        i=i+1
    return common_artifacts

artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))

def declutter(souvenirs, threshold):
    below_threshold=[]
    for x in souvenirs:
        if souvenirs.count(x)<threshold:
            below_threshold.append(x)
    return below_threshold



souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold2 = 2

print(declutter(souvenirs1, threshold1))
print(declutter(souvenirs2, threshold2))


def detect_temporal_anomaly(time_points, k):
    i=0
    j=0
    while i<len(time_points):
        j=0
        while j<len(time_points):
            if i!=j and time_points[i]==time_points[j] and abs(i-j)<=k:
                return True
            j=j+1
        i=i+1
    return False



time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))  
print(detect_temporal_anomaly(time_points2, k2)) 
print(detect_temporal_anomaly(time_points3, k3)) 


def most_endangered(species_list):
    smallest_name=""
    smallest_val=9999999
    for x in species_list:
        if x["population"]<smallest_val:
            smallest_val=x["population"]
            smallest_name=x["name"]
    return smallest_name



species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

def count_endangered_species(endangered_species, observed_species):
    count=0
    endangered_set=set(endangered_species)
    for x in observed_species:
        if x in endangered_set:
            count=count+1
    return count


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2)) 


def navigate_research_station(station_layout, observations):
    total_time = 0
    current_index = 0

    for letter in observations:
        next_index = station_layout.index(letter)
        total_time += abs(current_index - next_index)
        current_index = next_index

    return total_time
          


station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))



def prioritize_observations(observed_species, priority_species):
    extended_list=[]
    total_list=[]
    i=0
    j=0
    while i<len(priority_species):
        j=0
        while j<len(observed_species):
            if priority_species[i]==observed_species[j]:
                total_list.append(observed_species[j])
            j=j+1
        i=i+1
    
    extended_list=list(set(observed_species).difference(set(priority_species)))
    
    total_list.extend(sorted(extended_list))

    return total_list
    


observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 



def distinct_averages(species_populations):
    average_list=[]
    while species_populations!=[]:
        minimum=min(species_populations)
        maximum=max(species_populations)
        species_populations.remove(min(species_populations))
        species_populations.remove(max(species_populations))
        average=(maximum+minimum)/2
        average_list.append(average)
    return len(set(average_list))




species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 


def max_species_copies(raised_species, target_species):
    counter=0
    while target_species in raised_species:
        random1=random.choice(raised_species)
        random2=random.choice(raised_species)
        random3=random.choice(raised_species)
        string=random1+random2+random3
        if string==target_species:
            list1=list(raised_species)
            index1=list1.index(random1)
            index2=list1.index(random2)
            index3=list1.index(random3)
            list1.pop(index1)
            list1.pop(index2)
            list1.pop(index3)
            list1=str(list1)
            counter=counter+1
    return counter


raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2


def remove_low_rated_destinations(destinations, rating_threshold):
    high_dict={}
    for x in destinations.keys():
        if destinations.get(x)>=rating_threshold:
             high_dict[x]=destinations.get(x)
    return high_dict



destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogotá": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

print(remove_low_rated_destinations(destinations, 4.0))
print(remove_low_rated_destinations(destinations2, 4.9))



def unique_souvenir_counts(souvenirs):
    pass


souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print(unique_souvenir_counts(souvenirs1))  
print(unique_souvenir_counts(souvenirs2)) 
print(unique_souvenir_counts(souvenirs3))





def reverse_comments_queue(comments):
    deque_comments=deque(comments)
    deque_comments.reverse()
    return list(deque_comments)


print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


def is_symmetrical_title(title):
    pointer1=0
    pointer2=len(title)-1
    while pointer1!=pointer2:
        if title[pointer1]==" " and title[pointer2]==" " or title[pointer1]=="." and title[pointer2]=="." or title[pointer1]=="," and title[pointer2]==".":
            pointer1=pointer1+1
            pointer2=pointer2-1
        elif title[pointer1]==" " or title[pointer1]=="." or title[pointer1]==",":
            pointer1=pointer1+1
        elif title[pointer2]==" " or title[pointer2]=="." or title[pointer2]==",":
            pointer2=pointer2-1
        
        else: 
            if title[pointer1].lower()!=title[pointer2].lower():
                return False
            pointer1=pointer1+1
            pointer2=pointer2-1
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
print(is_symmetrical_title("A ,Santa at NASA"))
print(is_symmetrical_title("Social .Media")) 



def edit_post(post):
    post_q=deque(post)
    post_q.reverse()
    return str(post_q)

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 





def reverse_watchlist(watchlist):
    watchlist_deque=deque(watchlist)
    watchlist_deque.reverse()
    return list(watchlist_deque)


watchlist = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]

print(reverse_watchlist(watchlist)) 






def remove_duplicate_shows(schedule):
    stack=[]
    i=0
    while i<len(schedule):
        if stack!=[]:
            last_item=stack[-1]
            if last_item==schedule[i]:
                stack.pop()
            else:
                stack.append(schedule[i])
        else:
        
            stack.append(schedule[i])

                
            
        i=i+1
    return ''.join(stack)
    

       


print(remove_duplicate_shows("abbaca")) 
print(remove_duplicate_shows("azxxzy")) 


def min_remaining_watchlist(watchlist):
    stack=[]
    i=0
    while i<len(watchlist):
        if stack!=[]:
            last_item=stack[-1]
            if last_item=="A" and watchlist[i]=="B" or last_item=="C" and watchlist[i]=="D":
                stack.pop()
            else:
                stack.append(watchlist[i])
        else:
            stack.append(watchlist[i])
        i=i+1
        string_stack=''.join(stack)
    return len(string_stack)


print(min_remaining_watchlist("ABFCACDB")) 
print(min_remaining_watchlist("ACBBD")) 




def clean_post(post):
    stack=[]
    i=0
    while i<len(post):
        if stack!=[]:
            last_item=stack[-1]
            if last_item.lower() and last_item==post[i].lower() and post[i].upper():
                stack.pop()
            elif last_item.upper() and last_item==post[i].upper() and post[i].lower():
                stack.pop()
            else:
                stack.append(post[i])
                
        else:
            stack.append(post[i])
        i=i+1
    return ''.join(stack)


print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 




def post_compare(draft1, draft2):
    stack1=[]
    stack2=[]
    i=0
    while i<len(draft1):
        if stack1!=[]:
            if draft1[i]=="#":
                stack1.pop()
            else:
                stack1.append(draft1[i])
        else:
            stack1.append(draft1[i])
        i=i+1
    j=0
    while j<len(draft2):
        if stack2!=[]:
            if draft2[j]=="#":
                stack2.pop()
            else:
                stack2.append(draft2[j])
        else:
            stack2.append(draft2[j])
        j=j+1
    if ''.join(stack1)==''.join(stack2):
        return True
    else:
        return False

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 

def is_valid_post_format(posts):
    stack=[]
    format_list=["(", ")", "{", "}", "[", "]"]
    i=0
    while i<len(posts):
        if stack!=[]:
            if posts[i] in format_list:
                last_item=stack[-1]
                if last_item=="(" and not(posts[i]==")"):
                    return False
                elif last_item=="{" and not(posts[i]=="}"):
                    return False
                elif last_item=="[" and not(posts[i]=="]"):
                    return False
                else:
                    stack.append(posts[i])
            else:
                return False
        else:
            stack.append(posts[i])
        i=i+1
    return True
        


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
print(is_valid_post_format("([{}])"))    # Expected: True
print(is_valid_post_format("({[)]}")) 





def booth_navigation(clues):
    stack=[]
    i=0
    while i<len(clues):
        if stack!=[]:
            last_item=stack[-1]
            if clues[i]=="back":
                stack.pop()
            else:
                stack.append(clues[i])
        elif stack==[] and clues[i]!="back":
            stack.append(clues[i])
        i=i+1
    return stack

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) # Expected: False









