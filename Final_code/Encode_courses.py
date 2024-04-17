courses = [
    ("Programming in C", "EST102", "F", "S2C"),
    ("Programming in C", "EST102", "F", "S2D"),
    ("Graph Theory", "MAT206", "A", "S4C"),
    ("Graph Theory", "MAT206", "A", "S4D"),
    ("Computer Organization and Architecture", "CST 202", "B", "S4C"),
    ("Computer Organization and Architecture", "CST 202", "B", "S4D"),
    ("Database Management Systems", "CST 204", "C", "S4C"),
    ("Database Management Systems", "CST 204", "C", "S4D"),
    ("Operating Systems", "CST 206", "D", "S4C"),
    ("Operating Systems", "CST 206", "D", "S4D"),
    ("Constitution of India", "MCN202", "F", "S4C"),
    ("Constitution of India", "MCN202", "F", "S4D"),
    ("Design and Engineering", "EST200", "E", "S4D"),
    ("Design and Engineering", "EST200", "E", "S4C"),
    ("Digital Lab", "CSL 202", "S", "S4C"),
    ("Digital Lab", "CSL 202", "S", "S4D"),
    ("Operating Systems Lab", "CSL 204", "T", "S4C"),
    ("Operating Systems Lab", "CSL 204", "T", "S4D"),
    ("Mathematics for Machine Learning", "CST 284", "Minor", "S4C"),
    ("Number Theory", "CST292", "Minor", "S4C"),
    ("Computational Fundamentals for Machine Learning", "CST 284", "Honours", "S4C"),
    ("Compiler Design", "CST 302", "A", "S6C"),
    ("Compiler Design", "CST 302", "A", "S6D"),
    ("Computer Graphics and Image Processing", "CST 304", "B", "S6D"),
    ("Computer Graphics and Image Processing", "CST 304", "B", "S6C"),
    ("Algorithm Analysis and Design", "CST 306", "C", "S6C"),
    ("Algorithm Analysis and Design", "CST 306", "C", "S6D"),
    ("Foundations of machine learning", "CST 312", "D-Elective1", "S6C"),
    ("Foundations of security in computing", "CST 332", "D-Elective1", "S6C"),
    ("Programming in Python", "CST 362", "D-Elective1", "S6C"),
    ("Programming in Python", "CST 362", "D-Elective1", "S6D"),
    ("Industrial Economics & Foreign Trade", "HUT 300", "E", "S6C"),
    ("Industrial Economics & Foreign Trade", "HUT 300", "E", "S6D"),
    ("Industrial Economics & Foreign Trade", "HUT 300", "E", "S6D"),
    ("Comprehensive Course Work", "CST 308", "F", "S6C"),
    ("Comprehensive Course Work", "CST 308", "F", "S6D"),
    ("Networking Lab", "CSL 332", "S", "S6C"),
    ("Networking Lab", "CSL 332", "S", "S6D"),
    ("Mini Project", "CSD 334", "T", "S6C"),
    ("Mini Project", "CSD 334", "T", "S6D"),
    ("Concepts in deep learning", "CST 384", "Minor", "S6C"),
    ("Network Security", "CST 394", "Honours", "S6C"),
    ("Advanced Topics in Machine Learning", "CST 396", "Honours", "S6C"),
    ("Distributed Computing", "CST 402", "A", "S8C"),
    ("Distributed Computing", "CST 402", "A", "S8D"),
    ("Deep learning", "CST 414", "B-Elective3", "S8C"),
    ("Soft Computing", "CST 444", "B-Elective3", "S8C"),
    ("Soft Computing", "CST 444", "B-Elective3", "S8D"),
    ("Data Compression Techniques", "CST 446", "C-Elective4", "S8C"),
    ("Data Compression Techniques", "CST 446", "C-Elective4", "S8D"),
    ("Mobile Computing", "CST 476", "C-Elective4", "S8C"),
    ("Blockchain Technologies", "CST 428", "D-Elective5", "S8C"),
    ("Blockchain Technologies", "CST 428", "D-Elective5", "S8D"),
    ("Internet Of Things", "CST 448", "D-Elective5", "S8C"),
    ("Comprehensive Course Viva", "CST 404", "T", "S8C"),
    ("Comprehensive Course Viva", "CST 404", "T", "S8D"),
    ("Project Phase II", "CSD 416", "U", "S8C"),
    ("Project Phase II", "CSD 416", "U", "S8D")
]

# Function to convert course data into code
def convert_course_to_code(course_data):
    course_code, sem_code, batch = course_data[1], course_data[2], course_data[3]
    sem_code = "m" if sem_code == "Minor" else "h" if sem_code == "Honours" else sem_code[0]
    return f"{course_code.replace(' ', '')}-{sem_code}-{batch}"

# Generate codes for all courses
course_codes = [convert_course_to_code(course) for course in courses]

# Save the course codes to a text file
with open("encode_courses_output.txt", "w") as file:
    for code in course_codes:
        file.write(f"{code}\n")
