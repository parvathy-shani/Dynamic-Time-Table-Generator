import json

def read_chromosome(filename):
  """
  Reads a chromosome from a text file.

  Args:
    filename: The path to the text file containing the chromosome.

  Returns:
    A list of timeslots, where each timeslot is a list containing a course code
    and a room identifier.
  """
  chromosome = []
  with open(filename, 'r') as f:
    for line in f:
      timeslot = line.strip().split(':', 1)[1].strip()[1:-1].split("', '")
      course_code, room = timeslot[0].strip("[]"), timeslot[1].strip("[]")
      chromosome.append([course_code, room])
  return chromosome

def read_course_data(filename):
  """
  Reads course details from a JSON file.

  Args:
    filename: The path to the JSON file containing course data.

  Returns:
    A dictionary where keys are course codes and values are dictionaries
    containing course details.
  """
  course_data = {}
  with open(filename, 'r') as f:
    data = json.load(f)
    for course in data:
      course_code = course['Course code']
      course_data[course_code] = course
  return course_data

def check_course_requirements(chromosome, course_data):
  """
  Calculates the total penalty for unmet course requirements across all courses.

  Args:
    chromosome: The chromosome data (list of timeslots).
    course_data: A dictionary containing course details.

  Returns:
    The total penalty for unmet requirements.
  """
  total_penalty = 0
  for course_code, course_details in course_data.items():
    # Count course occurrences in the chromosome
    lecture_count = 0
    tutorial_count = 0
    practical_count = 0
    for slot in chromosome:
      event, _ = slot
      if event[0] == course_code:
        if 'lecture' in event[1]:
          lecture_count += 1
        elif 'tutorial' in event[1]:
          tutorial_count += 1
        else:
          practical_count += 1

    # Calculate penalty for unmet requirements
    required_lecture = course_details['lecture/week']
    required_tutorial = course_details['tutorial/week']
    required_practical = course_details['practical/week']

    penalty = abs(required_lecture - lecture_count)
    penalty += abs(required_tutorial - tutorial_count)
    penalty += abs(required_practical - practical_count)
    total_penalty += penalty

  return total_penalty


# Example usage (corrected)
chromosome_file = "formatted_initial_population_S2C.txt"
course_data_file = "combined_data.json"

chromosome = read_chromosome(chromosome_file)
course_data = read_course_data(course_data_file)

penalty = check_course_requirements(chromosome, course_data)

print(f"Total penalty for unmet requirements: {penalty}")
