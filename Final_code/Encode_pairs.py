import itertools

# Read encoded packets data from file
with open('encode_packets_output.txt', 'r') as packets_file:
    packets_data = packets_file.read().splitlines()

# Read encoded events data from file
with open('format_events_output.txt', 'r') as events_file:
    events_data = events_file.read().splitlines()

# Generate all possible combinations using itertools.product
all_combinations = list(itertools.product(packets_data, events_data))

# Save all combinations to a new file
with open('encode_pairs_output.txt', 'w') as combinations_file:
    for combination in all_combinations:
        packet = ' '.join(combination)
        combinations_file.write(f"{packet}\n")

print("All possible combinations generated and saved to 'encode_pairs_output.txt'")
