import itertools

# Read encoded timeslots data from file
with open('encode_timeslots_output.txt', 'r') as timeslots_file:
    timeslots_data = timeslots_file.read().splitlines()

# Read encoded rooms data from file
with open('encode_rooms_output.txt', 'r') as rooms_file:
    rooms_data = rooms_file.read().splitlines()

# Generate all possible combinations using itertools.product
all_combinations = list(itertools.product(timeslots_data, rooms_data))

# Save all combinations to a new file
with open('encode_packets_output.txt', 'w') as combinations_file:
    for combination in all_combinations:
        packet = ' '.join(combination)
        combinations_file.write(f"{packet}\n")

print("All possible combinations generated and saved to 'encode_packets_output.txt'")
