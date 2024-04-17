import itertools

# Read encoded lectures data from file
with open('encode_lecturers_output.txt', 'r') as lecturers_file:
    lecturers_data = lecturers_file.read().splitlines()

# Read encoded rooms data from file
with open('encode_courses_output.txt', 'r') as courses_file:
    courses_data = courses_file.read().splitlines()

# Generate all possible combinations using itertools.product
all_combinations = list(itertools.product(lecturers_data, courses_data))

# Save all combinations to a new file
with open('encode_events_output.txt', 'w') as combinations_file:
    for combination in all_combinations:
        packet = ' '.join(combination)
        combinations_file.write(f"{packet}\n")

print("All possible combinations generated and saved to 'encode_packets_output.txt'")
