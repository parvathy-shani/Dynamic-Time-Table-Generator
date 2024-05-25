import pandas as pd 
import json
import random
import copy
from collections import Counter


with open("D:\\Dynamic Timetable Generator\\Not django\\Final_code\\combined_data.json", 'r') as json_file:
    combined_data = json.load(json_file)



def encode_timeslots(data: dict) -> dict:
    time_slots = {}  # empty dictionary to store the timeslot with its code sample:'Monday 09:00am - 10:00am': 'G1'
    gene_count = 1  # start the gene_count from 1

    for slot in data:  # Corrected variable name from timeslots to data
        day = slot["day"]
        start_time = slot["startTime"]
        end_time = slot["endTime"]
        time_slots[f'G{gene_count}'] = f'{day} {start_time} - {end_time}'  # stores into dictionary
        gene_count += 1  # increment the gene_count

    return time_slots  # Return the encoded time slots dictionary


def generate_code(room_name, allotted_batch, purpose):
    room_code = room_name[:3]  # Extract first three letters of room name
    batch_code = allotted_batch[:3] # Extract first three letters of allotted batch
    purpose_code = 'l' if purpose.lower() == 'lecture' else 'o' # Generate purpose code 'l' for lecture, 'o' for other purposes
    code = f"{room_code}-{batch_code}-{purpose_code}"   # Combine codes to form 7-character code
    return code  # Return the generated code



def encode_room(data:dict) -> dict:
    # Generate codes for each classroom

    codes = {}  # Empty dictionary to store the classroom code

    for classroom in data:
        room_name = classroom["roomName"]
        allotted_batch = classroom["allottedBatch"]
        purpose = classroom["purpose"]
        code = generate_code(room_name, allotted_batch, purpose)  # Function call to generate the code
        codes[code] = [room_name, allotted_batch, purpose]  # Assign code and details to the room_name key in the dictionary

    return codes

def encode_lectures(data:dict) -> dict:
    lecturer_codes = {}  # dict to store the lecturer codes

    # Generate codes based on the given rules, the rules
    department_code = 'CS'
    position_mapping = {
        'Professor': 'PP',
        'Associate Professor': 'AP',
        'Assistant Professor': 'AA'
    }

    for idx, lecturer_info in enumerate(data):
        lecturer = lecturer_info['lecturerName']
        position = lecturer_info['position']
        position_code = position_mapping.get(position, 'AA')  # Default to Assistant Professor if position not found
        order_code = str(idx + 1).zfill(2)  # Adding 1 to index since index starts from 0, and then zero padding
        preference = lecturer_info['preferredTimeslot']
        preference_code = 'n' if preference == 'NIL' else 'f'  # Assuming 'n' for NIL preference, 'f' for Forenoon
        code = f"{department_code}{position_code}{order_code}{preference_code}"
        lecturer_codes[code] = [[lecturer], [position], [preference]]

    return lecturer_codes

def encode_courses(data: list) -> dict:
    course_codes = {}  # Empty dictionary to store course code

    # Generate codes for all courses
    for course in data:
        course_code, sem_code, batch = course["courseCode"], course["type"], course["allottedBatch"]
        sem_code = "m" if sem_code == "Minor" else "h" if sem_code == "Honours" else sem_code[0]
        code = f"{course_code.replace(' ', '')}-{sem_code}-{batch}"
        course_codes[code] = [course_code, sem_code, batch]

    return course_codes


def format_events(data:list) -> list:
    valid_events = []
    #invalid_events = []

    for mapping in data:
        teacher_code, course_info = mapping[0], mapping[1]
        found = False
        for course in combined_data:
            if course_info.startswith(course['Course code']):
                sem_code = course_info.split('-')[1]
                batch = course_info.split('-')[2]
                if any(teacher['teacher_code'] == teacher_code for teacher in course['lecturers']):
                    valid_event = mapping
                    valid_events.append(valid_event)
                    found = True
                    break
    return valid_events

def format_pairs(data:list) -> list:
    # Create an empty list to store the valid pairs
    valid = []

    # Iterate over each pair in pairs
    for pair in data:
        room = pair[0][1]
        course = pair[1][1]
        room_batch = room.split('-')[1]
        course_batch = course.split('-')[2]
        room_purpose = room.split('-')[2]
        purpose = False

        # Check each item in data for a match
        for item in combined_data:
            course_code = item["Course code"]
            sem_code = item["Sem code"]
            batch = item["batches"]
            code = f'{course_code}-{sem_code}-{batch}'

            if course == code:
                if item["practical/week"] > 0 and room_purpose == 'o':
                    purpose = True
                elif item["lecture/week"] > 0 and room_purpose == 'l':
                    purpose = True

        # Check if the room batch matches the course batch and purpose is True
        if room_batch == course_batch and purpose:
            valid.append(pair)
    
    return valid

def extract_pair_info(pair):
    timeslot = pair[0][0]
    room = pair[0][1]
    lecturer = pair[1][0]
    course = pair[1][1]
    room_batch = room.split('-')[1]
    purpose = room.split('-')[2]
    code = f'{timeslot} {room} {lecturer} {course}'

    return timeslot, room, lecturer, course, room_batch, purpose, code

import random
import copy

def generate_chromosome(pairs, batch):
    chromosome = []
    gene_number = 1
    used_codes = set()

    random_pairs = random.sample(pairs, len(pairs))  # randomly generated pairs

    # Greedy Initialization
    for pair in random_pairs:  # consider one gene from the randomly generated pool
        timeslot, room, lecturer, course, room_batch, purpose, code = extract_pair_info(pair)  # extract the relevant data

        if (batch == room_batch) and (code not in used_codes) and (timeslot == f'G{gene_number}'):  # check if the batch for which the chromosome generated is same and the gene hasn't been used yet and the timeslot matches the position
            if purpose == 'o' and (gene_number) % 3 == 1:  # checks whether the purpose is others (lab/project) or lecture
                chromosome.append(pair)
                used_codes.add(code)
                gene_number += 1
                for _ in range(2):
                    new_code = f'G{gene_number} {" ".join(code.split()[1:])}'  # Create new pair with incremented gene number
                    new_pair = copy.deepcopy(pair)  # Create a deep copy of the pair
                    new_pair = (['G' + str(gene_number)] + list(new_pair[0][1:]), new_pair[1])  # Modify the gene number in the new pair
                    chromosome.append(new_pair)
                    used_codes.add(new_code)
                    gene_number += 1
                if gene_number > 30:
                    break
            else:
                # If purpose is not 'o', add random pairs with purpose 'l' for the next three consecutive positions
                if purpose != 'o':
                    chromosome.append(pair)
                    used_codes.add(code)
                    gene_number += 1
                    if gene_number > 30:
                        break
            if gene_number > 30:
                break

    return chromosome


def chromosome_generation(data:list) -> dict:
    batches = ['S2C', 'S2D', 'S4C', 'S4D', 'S6C', 'S6D', 'S8C', 'S8D']  # Names of the batches
    num_chromosomes_per_batch = 50  # Number of chromosomes for each batch
    batch_chromosomes = {}  # Dictionary to store chromosomes for each batch


    for batch in batches:
        batch_chromosomes[batch] = []  # Initialize empty list for each batch
        for _ in range(num_chromosomes_per_batch):
            chromosome = generate_chromosome(data, batch)
            batch_chromosomes[batch].append(chromosome)  # Append generated chromosome to the batch list

    return batch_chromosomes

def check_count_constraint(chromosome):
    event = []  # empty event to store teacher-course pair
    processed_courses = set()  # to keep track of processed course codes

    for gene in chromosome:
        event.append(gene[1][1][:6])

    courses_counts = Counter(event)  # counts the number of occurrences of a single subject

    total_deviation = 0
    for course_code in event:
        for course in combined_data:
            if course["Course code"] == course_code and course_code not in processed_courses:
                processed_courses.add(course_code)
                deviation = courses_counts[course_code] - (course["lecture/week"] + course["tutorial/week"] + course["practical/week"])
                total_deviation += deviation


    return total_deviation

def elitism(data:dict) -> dict:
    elite_group={}
    # Iterate through the keys and access the nested lists
    for key in data.keys():
        initial_chromosomes = data[key]

        # Iterate through the nested lists and print their elements
        chromosome_collection = []
        for chromosome in initial_chromosomes:
            deviation = check_count_constraint(chromosome)
            if deviation >0 and deviation < 15 :
                chromosome_collection.append(chromosome)

        elite_group[key] = chromosome_collection

    return elite_group

def selection(data:dict) -> dict:
    parent_timetable1 = {}
    parent_timetable2 = {}

    for key in data.keys():
        initial_chromosomes = data[key]
        parent_timetable1[key] = []
        parent_timetable2[key] = []
        for idx, chromosome in enumerate(initial_chromosomes[:2]):
            if idx == 0:
                parent_timetable1[key].append(chromosome)
            else:
                parent_timetable2[key].append(chromosome)

    crossover={}
    crossover["parent1"] = parent_timetable1
    crossover["parent2"] = parent_timetable2

    return crossover

def crossover(data:dict) -> dict:
    # Retrieve parent data from the loaded JSON
    parent1_data = data["parent1"]
    parent2_data = data["parent2"]

    # Create a dictionary to store the child data
    child_data1 = {}
    child_data2= {}

    # Store the first 15 genes of each chromosome in parent1 as the child data
    for batch_key, chromosomes in parent1_data.items():
        child_data1[batch_key] = []
        child_data2[batch_key] = []
        for chromosome in chromosomes:
            child_data1[batch_key].append(chromosome[:30])
            child_data2[batch_key].append(chromosome[30:])

    # Store the first 15 genes of each chromosome in parent1 as the child data
    for batch_key, chromosomes in parent2_data.items():
        for chromosome in chromosomes:
            child_data2[batch_key].append(chromosome[:30])
            child_data1[batch_key].append(chromosome[30:])

    return child_data1
    #return child_data2

def hc_lecturer_conflicts(timetable):
    violation_count = 0
    for p1 in timetable:
        for p2 in timetable:
            if p1 != p2 and len(p1) > 1 and len(p2) > 1:  # Added length check
                if p1[1][0] == p2[1][0] and p1[0][0] == p2[0][0]:
                    violation_count += 1
    return violation_count

def hc_class_conflicts(timetable):
    violation_count = 0
    for p1 in timetable:
        for p2 in timetable:
            if p1 != p2 and len(p1) > 0 and len(p2) > 0:  # Added length check
                if len(p1[0]) > 2 and len(p2[0]) > 2:  # Added length check for inner list
                    if p1[0][2] == p2[0][2] and p1[0][0] == p2[0][0]:
                        violation_count += 1
    return violation_count

def calculate_fitness(timetable, weights):
    v1 = hc_lecturer_conflicts(timetable)
    v2 = hc_class_conflicts(timetable)
    total_violation = weights[0] * v1 + weights[1] * v2
    return 1 / (1 + total_violation)

def hard_constraints(data:dict) -> list:
    # Assuming data is a list of timetables
    timetables = data

    weights = [1, 1]
    fitness_scores = []

    for timetable in timetables:
        fitness_score = calculate_fitness(timetable, weights)
        fitness_scores.append(fitness_score)

    return fitness_scores