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
add_gamer({'name':'Linus','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
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

# Step 2 - Count the number of people every night.
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
# For each day in the gamer's availability, add one to that date on the frequency table.
        for day in gamer['availability']:
            available_frequency[day] += 1

# Best week day night to run Time Travel!
calculate_availability(gamers, count_availability)
print(count_availability)
# output
# {'Monday': 6, 'Tuesday': 9, 'Wednesday': 6, 'Thursday': 9, 'Friday': 7, 'Saturday': 6, 'Sunday': 7}

# Day(s) of week for attendance of most available people 
def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_night = day
            best_availability = availability
    return best_night

# Best day to host game night
game_night = find_best_night(count_availability)
print(game_night)
# output
# Tuesday

# List of all available people on day the game night will be hosted.
def available_on_night(gamers_list, day):
    return [gamer for gamer in gamers_list if day in gamer['availability']]

attending_game_night = available_on_night(gamers, game_night)

print(attending_game_night)
# output
# [{'name': 'Charlie Brown', 'availability': ['Tuesday', 'Wednesday', 'Thursday']}, {'name': 'Snoopy', 'availability': ['Tuesday', 'Thursday', 'Saturday']}, {'name': 'Shermy', 'availability': ['Tuesday', 'Thursday', 'Sunday']}, {'name': 'Linus', 'availability': ['Tuesday', 'Thursday', 'Saturday']}, {'name': 'Schroeder', 'availability': ['Sunday', 'Tuesday', 'Wednesday']}, {'name': 'Peppermint Patty', 'availability': ['Monday', 'Tuesday', 'Thursday']}, {'name': 'Frieda', 'availability': ['Sunday', 'Tuesday', 'Saturday']}, {'name': 'Franklin', 'availability': ['Tuesday', 'Thursday', 'Friday']}, {'name': 'Pig-Pen', 'availability': ['Sunday', 'Monday', 'Tuesday']}]

# Generating an E-mail for the Participants
# To let attendees know that game night is on a night they can attend. 
# Step 1 - Create a form email to send to each of the participants (to be filled out with data later).
form_email = """
Dear {name},

The Time Travel Agency is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Captivatingly Yours,
the Time Travel Agency
"""

# Step 2 - function
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer['name'], day_of_week=day, game=game))
        
send_email(attending_game_night, game_night, "Time Travel!")

# To set-up a second game night during week