# Dynamic Timetable Generator Backend

Welcome to the backend repository of the Dynamic Timetable Generator, a sophisticated system designed to optimize academic timetabling using advanced genetic algorithms. This system ensures efficient resource allocation, minimizes scheduling conflicts, and provides a flexible framework for evolving academic needs. The following README outlines the key features, setup instructions, and usage guidelines for the backend of this transformative timetabling tool.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [API Documentation](#api-documentation)
7. [Contributing](#contributing)
8. [License](#license)

## Project Overview

The Dynamic Timetable Generator is a web-based platform that automates the creation of academic timetables through the use of genetic algorithm. It features personalized logins for campus managers, teachers, and class representatives, ensuring a tailored and efficient user experience. 

## Key Features

- **Comprehensive Data Collection**: Gathers detailed information on staff, including names, departments, contact details, availability, and qualifications. 
- **Algorithm-Driven Timetable Generation**: Utilizes scheduling algorithms to create conflict-free schedules, addressing staff crossover, consecutive classes, and other constraints.
- **User-Friendly Interface**: Provides intuitive dashboards for campus managers, teachers, and class representatives, enhancing the user experience.
- **Adaptability and Flexibility**: Adapts to changing academic demands, fostering a collaborative and efficient educational environment.
- **Multi-level User Login System**: Implements distinct logins for campus managers, teachers, and class representatives, each with role-specific functionalities.

## Installation

To set up the backend of the Dynamic Timetable Generator, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/dynamic-timetable-generator-backend.git
   cd dynamic-timetable-generator-backend
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**:
   Ensure your database is configured correctly. Update the `DATABASE_URL` in the `.env` file with your database credentials.
   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## Configuration

The backend uses environment variables for configuration. Create a `.env` file in the root directory and add the following variables:

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1
```

## Usage

After setting up the backend, you can interact with the system through its API endpoints. Ensure the frontend application is also set up to provide a complete user interface for campus managers, teachers, and class representatives.

### Example Endpoints:

- **GET /api/timetables**: Retrieve all timetables
- **POST /api/timetables**: Create a new timetable
- **GET /api/timetables/{id}**: Retrieve a specific timetable
- **PUT /api/timetables/{id}**: Update a specific timetable
- **DELETE /api/timetables/{id}**: Delete a specific timetable

## Contributing

We welcome contributions to enhance the Dynamic Timetable Generator. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes.
4. Commit your changes.
   ```bash
   git commit -m "Add your commit message"
   ```
5. Push to the branch.
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a Pull Request.

Keywords: multidepth genetic algorithm, timetable generation, scheduling algorithms, academic timetables, web-based platform
