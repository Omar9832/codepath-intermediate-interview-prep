def lineup(artists, set_times):
    artists_dict={}
    i=0
    while i<len(artists1):
        artists_dict[artists1[i]]=set_times1[i]
        i=i+1
    return artists_dict


artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))



def get_artist_info(artist, festival_schedule):
    for x in festival_schedule.keys():
        if x==artist:
            return festival_schedule.get(x)
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
    total=0
    for x in ticket_sales.values():
        total=total+x
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))


def best_set(votes):
    votes_dict=dict.fromkeys(votes.values(), 0)
    for x in votes.values():
        votes_dict[x]=votes_dict[x]+1
    greatest_name=""
    greatest_val=-999
    for x in votes_dict:
        if votes_dict[x]>greatest_val:
            greatest_val=votes_dict[x]
            greatest_name=x
        

    return greatest_name


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
