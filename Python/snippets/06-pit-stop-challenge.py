# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
race_time = float(input("How long was the race in seconds?"))


# 2. Ask how many pit stops were made.
pit_stops = int(input("How many pit stops did you make?"))


# 3. Ask for the average pit stop duration (in seconds).
pit_stop_time = float(input("How long was the average pit stop time in seconds?"))

#
# Then:
# - Calculate the total pit stop time.
total_pitstop_time = pit_stops * pit_stop_time


# - Calculate the percentage of the race spent in the pits.
total_time_in_pits = (race_time / pit_stops) * 100


# - Round the percentage to 2 decimal places.
# print('correct answer: {:.2%}'.format(total_time_in_pits))
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

print(f"Your total pitstop time was {total_pitstop_time} seconds. Your total percentage of time spent in the pits was {total_time_in_pits * 100}%")
