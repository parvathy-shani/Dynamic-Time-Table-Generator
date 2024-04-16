import json

# Provided classroom data
classrooms_data = [
    {"room_name": "101", "allotted_batch": "S8C", "purpose": "lecture"},
    {"room_name": "102", "allotted_batch": "S8D", "purpose": "lecture"},
    {"room_name": "CC1", "allotted_batch": "S8C", "purpose": "project"},
    {"room_name": "CC2", "allotted_batch": "S8C", "purpose": "project"},
    {"room_name": "412", "allotted_batch": "S8D", "purpose": "project"},
    {"room_name": "SDPK", "allotted_batch": "S8D", "purpose": "project"},
    {"room_name": "103", "allotted_batch": "S6C", "purpose": "lecture"},
    {"room_name": "104", "allotted_batch": "S6D", "purpose": "lecture"},
    {"room_name": "CC1", "allotted_batch": "S6C", "purpose": "mini-project"},
    {"room_name": "CC2", "allotted_batch": "S6C", "purpose": "mini-project"},
    {"room_name": "412", "allotted_batch": "S6D", "purpose": "mini-project"},
    {"room_name": "SDPK", "allotted_batch": "S6D", "purpose": "mini-project"},
    {"room_name": "CL1", "allotted_batch": "S6D", "purpose": "lab"},
    {"room_name": "CL2", "allotted_batch": "S6D", "purpose": "lab"},
    {"room_name": "105", "allotted_batch": "S4C", "purpose": "lecture"},
    {"room_name": "106", "allotted_batch": "S4D", "purpose": "lecture"},
    {"room_name": "CC1", "allotted_batch": "S4C", "purpose": "lab"},
    {"room_name": "CC2", "allotted_batch": "S4C", "purpose": "lab"},
    {"room_name": "CL1", "allotted_batch": "S4D", "purpose": "lab"},
    {"room_name": "CL2", "allotted_batch": "S4D", "purpose": "lab"},
    {"room_name": "107", "allotted_batch": "S2D", "purpose": "lecture"},
    {"room_name": "108", "allotted_batch": "S2C", "purpose": "lecture"}
]

# Function to generate 7-character code
def generate_code(room_name, allotted_batch, purpose):
    # Extract first three letters of room name
    room_code = room_name[:3]
    # Extract first three letters of allotted batch
    batch_code = allotted_batch[:3]
    # Generate purpose code 'l' for lecture, 'o' for other purposes
    purpose_code = 'l' if purpose.lower() == 'lecture' else 'o'
    # Combine codes to form 7-character code
    code = f"{room_code}-{batch_code}-{purpose_code}"
    return code

# Generate codes for each classroom
codes = []
for classroom in classrooms_data:
    code = generate_code(classroom["room_name"], classroom["allotted_batch"], classroom["purpose"])
    codes.append(code)

# Save codes to a text file
with open('encode_rooms_output.txt', 'w') as file:
    for code in codes:
        file.write(f"{code}\n")

print("Classroom codes saved to 'encode_rooms_output.txt'")
