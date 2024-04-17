import json


def load_course_info(json_file_path):
    with open(json_file_path, 'r') as file:
        course_info = json.load(file)
    return course_info


def calculate_fitness(schedule, weights, room_capacity, lecturer_time_constraints, lecturer_time_preferences,
                      course_info):
    v1 = hc_lecturer_conflict(schedule)
    v2 = hc_class_conflict(schedule)
    v4 = hc_lecturer_time_constraints(schedule, lecturer_time_constraints)
    v5 = hc_lecturer_time_preferences(schedule, lecturer_time_preferences)
    v6 = hc_max_hours_per_position(schedule, course_info)

    total_violation = weights[0] * v1 + weights[1] * v2 + weights[2] * v4 + weights[4] * v5 + weights[5] * v6
    return 1 / (1 + total_violation)


def read_chromosomes(input_file_path):
    chromosomes = []
    with open(input_file_path, 'r') as file:
        chromosome_data = file.read().split('Chromosome ')
        for i, chromosome_str in enumerate(chromosome_data[1:], start=1):
            chromosome_lines = chromosome_str.strip().split('\n')
            schedule = []
            for line in chromosome_lines[1:]:
                if line.strip():
                    schedule_data = line.strip()[3:-1].split("'], ['")
                    schedule.append([slot.split(", ") for slot in schedule_data])
            chromosomes.append(schedule)
    return chromosomes


def read_max_hours_per_position(file_path):
    max_hours = {}
    with open(file_path, 'r') as file:
        for line in file:
            position, hours = line.strip().split(' - ')
            max_hours[position] = int(hours)
    return max_hours

def hc_max_hours_per_position(schedule, max_hours_per_position):
    position_hours = {'PP': 0, 'AP': 0, 'AA': 0}
    for slot in schedule:
        lecturer_position = slot[1][0][2]  # Extracting position from lecturer code
        position_hours[lecturer_position] += 1
    violation_count = sum(1 for hours in position_hours.values() if hours > max_hours_per_position[lecturer_position])
    return violation_count

def write_fitness_scores(chromosomes, fitness_scores, output_file_path):
    with open(output_file_path, 'w') as file:
        for chromosome, fitness in zip(chromosomes, fitness_scores):
            file.write(f"Chromosome: {chromosome}\n")
            file.write(f"Fitness Score: {fitness}\n")
            file.write("\n")

def main():
    input_file_path = "formatted_initial_population_S2C.txt"
    output_file_path = 'fitness_scores_S2C.txt'
    max_hours_file_path = 'max_hours_per_position.txt'
    course_info_file_path = 'combined_data.json'

    chromosomes = read_chromosomes(input_file_path)
    max_hours_per_position = read_max_hours_per_position(max_hours_file_path)
    course_info = load_course_info(course_info_file_path)

    weights = [1, 1, 1, 1, 1, 1]  # Adjust weights as needed
    room_capacity = {'303': 50}  # Populate with room capacities
    lecturer_time_constraints = {'CSAA07': ['9AM-MONDAY']}  # Populate with lecturer time constraints
    lecturer_time_preferences = {}  # Populate with lecturer time preferences

    fitness_scores = []
    for chromosome in chromosomes:
        fitness = calculate_fitness(chromosome, weights, room_capacity, lecturer_time_constraints, lecturer_time_preferences, course_info)
        fitness_scores.append(fitness)

    write_fitness_scores(chromosomes, fitness_scores, output_file_path)
    print("Fitness scores written to:", output_file_path)

if __name__ == "__main__":
    main()