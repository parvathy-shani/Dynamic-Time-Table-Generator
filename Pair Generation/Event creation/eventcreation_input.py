def create_text_file(data, filename):
    with open(filename, 'w') as f:
        for item in data:
            f.write(item + '\n')

# Data for lecturers, classes, and sets of students
lecturers_data = [
    "Shama-Das: CSPP01",
    "Ahammed-Siraj-K-K: CSAP01",
    "Anjitha-P: CSAA01",
    "Syeatha-Merlin-Thampy: CSAA02",
    "Vishnu-S-Kumar: CSAA03",
    "Ameena-A: CSAA04",
    "Leya-G: CSAA05",
    "Chinchu-M-Pillai: CSAA06",
    "Sushitha-Susan-Joseph: CSAA07",
    "Neethu-Treesa-Jacob: CSAA08",
    "Shiny-B: CSAA09",
    "Sreelekshmi-K-R: CSAA10"
]

classes_data = [
    "Distributed-computing: S8CST402",
    "Soft-computing: S8CST444",
    "Data-Compression-Techniques: S8CST446",
    "Blockchain-technologies: S8CST428",
    "Comprehensive-course-viva: S8CST404",
    "Project-phase-2: S8CST404"
]

students_data = [
    "S8D: D",
    "S8C: C"
]

# Create text files for lecturers, classes, and sets of students
create_text_file(lecturers_data, 'lecturers.txt')
create_text_file(classes_data, 'classes.txt')
create_text_file(students_data, 'students.txt')

print("Text files created successfully.")
