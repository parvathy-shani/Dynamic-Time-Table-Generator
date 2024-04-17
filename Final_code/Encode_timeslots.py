timeslots = {
    'Monday': [
        '09:00am - 10:00am',
        '10:00am - 11:00am',
        '11:00am - 12:00pm',
        '01:00pm - 02:00pm',
        '02:00pm - 03:00pm',
        '03:00pm - 04:00pm'
    ],
    'Tuesday': [
        '09:00am - 10:00am',
        '10:00am - 11:00am',
        '11:00am - 12:00pm',
        '01:00pm - 02:00pm',
        '02:00pm - 03:00pm',
        '03:00pm - 04:00pm'
    ],
    'Wednesday': [
        '09:00am - 10:00am',
        '10:00am - 11:00am',
        '11:00am - 12:00pm',
        '01:00pm - 02:00pm',
        '02:00pm - 03:00pm',
        '03:00pm - 04:00pm'
    ],
    'Thursday': [
        '09:00am - 10:00am',
        '10:00am - 11:00am',
        '11:00am - 12:00pm',
        '01:00pm - 02:00pm',
        '02:00pm - 03:00pm',
        '03:00pm - 04:00pm'
    ],
    'Friday': [
        '09:00am - 09:50am',
        '09:50am - 10:40am',
        '10:40am - 11:30am',
        '11:40am - 12:30pm',
        '02:00pm - 03:00pm',
        '03:00pm - 04:00pm'
    ]
}

# Encode timeslots into gene positions
gene_positions = {}
gene_count = 1
for day, slots in timeslots.items():
    for slot in slots:
        gene_positions[f'{day} {slot}'] = gene_count
        gene_count += 1

# Write the gene positions mapping to a text file
with open('encode_timeslots_output.txt', 'w') as file:
    for timeslot, gene_pos in gene_positions.items():
        file.write(f"G{gene_pos}\n")

print("Gene positions mapping has been stored in encode_timeslots_output.txt.")

