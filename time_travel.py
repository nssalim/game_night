# Dictionaries

# Time Travel

# Host a game night to play the tabletop RPG Time Travel! 

# Create a system for organizing and tracking gamer’s availability. Programmatically figure out the best day to host a game night and send out emails to the attendees to let them know when to come. 

# list of people who shall attend game night
gamers = []

# The  add_gamer function takes two parameters: gamer and gamers_list. This function checks that the argument passed to the gamer parameter has both "name" and an "availability" as keys and if so adds gamer to gamers_list.
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical information")

# add gamer
charlie = {
    'name': "Charlie Brown",
    'availability': ["Tuesday", "Wednesday", "Thursday"]
}
add_gamer(charlie, gamers)
print(gamers)
# output
# [{'name': 'Charlie Brown', 'availability': ['Tuesday', 'Wednesday', 'Thursday']}]

# add more gamers to the list of all of the people interested in game night
add_gamer({'name':'Snoopy','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Woodstock','availability': ["Monday", "Thursday", "Friday", "Sunday"]}, gamers)
add_gamer({'name':'Shermy','availability': ["Tuesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Rerun','availability': ["Wednesday", "Saturday"]}, gamers)
add_gamer({'name': 'Eudora', 'availability': ["Monday", "Friday"]}, gamers)
add_gamer({'name':'Sally','availability': ["Friday", "Sunday"]}, gamers)
add_gamer({'name':'Linus','availability': ["Tueday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Lucy','availability': ["Monday", "Wednesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Schroeder','availability': ["Sunday", "Tuesday", "Wednesday"]}, gamers)
add_gamer({'name':'Peppermint Patty','availability': ["Monday", "Tuesday", "Thursday"]}, gamers)
add_gamer({'name':'Frieda','availability': ["Sunday", "Tuesday", "Saturday"]}, gamers)
add_gamer({'name':'Marcie','availability': ["Monday", "Wednesday", "Friday"]}, gamers)
add_gamer({'name':'Franklin','availability': ["Tuesday", "Thursday", "Friday"]}, gamers)
add_gamer({'name':'Violet','availability': ["Friday", "Saturday", "Sunday"]}, gamers)
add_gamer({'name':'Pig-Pen','availability': ["Sunday", "Monday", "Tuesday"]}, gamers)
add_gamer({'name':'Patty','availability': ["Wednesday", "Thursday", "Friday"]}, gamers)

# Finding the perfect availability
# Calculate which nights will have the most participation. 
# Step 1 - create a frequency table which correlates each day of the week with gamer availability.
def build_daily_frequency_table():
    return {
        "Monday":    0,
        "Tuesday":   0,
        "Wednesday": 0,
        "Thursday":  0,
        "Friday":    0,
        "Saturday":  0,
        "Sunday":    0,
    }

count_availability = build_daily_frequency_table()


  