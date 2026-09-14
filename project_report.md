# SmartHireAI Project Report

## 1. Introduction
SmartHireAI is an AI-assisted recruitment and screening system designed to simplify candidate evaluation for academic and faculty hiring processes. The project allows applicants to enter their details, automatically evaluates them using rule-based logic, and stores their data in a SQLite database. Administrators can then log in to review ranking results, monitor candidate performance, and update final selection status.

The current version of the project includes a candidate screening module, AI-style interview evaluation, an administrator dashboard, and deployment support for Render. A major issue earlier was the mismatch between local SQLite data and the deployed render environment. This final report reflects the updated application after the database compatibility and deployment fixes were implemented.

---

## 2. Problem Statement
Recruitment at many institutions depends on manually reviewing large numbers of applications. This process can be time-consuming, inconsistent, and subjective. The goal of SmartHireAI is to automate the early screening stage and assist administrators in making faster and more transparent decisions.

The system addresses the following problems:
- Manual screening is slow and inconsistent.
- Recruitment decisions may be biased without structured evaluation.
- Hiring teams need quick access to candidate rankings.
- Interview and screening data should be stored and reviewed systematically.

---

## 3. Objectives
The main objectives of this system are:
1. To collect candidate information and evaluate it using predefined rules.
2. To generate a score and recommendation for each applicant.
3. To conduct a short AI-based interview using keyword-based evaluation.
4. To store results in a database for admin review.
5. To give administrators a dashboard to rank and update candidate selection status.
6. To support deployment on a cloud platform such as Render while preserving database compatibility.

---

## 4. Scope of the Project
The project includes the following major components:
- Front-end web pages for home, login, result, and dashboard screens.
- Candidate screening form.
- Rule-based scoring logic.
- Interview questionnaire and scoring engine.
- SQLite database for storing candidate and admin data.
- Admin login and dashboard for reviewing candidate status.
- Render deployment configuration for a hosted version.

This is a practical prototype focused on automated hiring support, not a full enterprise HRMS.

---

## 5. System Architecture
The application follows a simple Flask web application architecture.

### 5.1 Components
- Frontend: HTML templates rendered using Flask
- Backend: Python with Flask routes and business logic
- Data storage: SQLite database
- Screening engine: rules.py
- Database wrapper: database.py
- Deployment environment: Render hosted web service

### 5.2 Request Flow
1. Candidate enters personal and qualification information.
2. Flask route processes the form submission.
3. The evaluation engine calculates a screening score.
4. The result is saved into the database.
5. Candidate can complete a short interview questionnaire.
6. Interview answers are scored using keyword-based logic.
7. Admin logs in via username and password.
8. Admin reviews dashboard and updates the final selection status.

---

## 6. Project Modules

### 6.1 Home Page
The landing page provides access to the screening form and admin features.

### 6.2 Candidate Screening Module
The candidate submits:
- Name
- Email
- Qualification
- Experience
- Specialization

The system evaluates the candidate based on matching rules and generates:
- score
- status
- reasons

### 6.3 Interview Evaluation Module
After the screening stage, the candidate completes a short interview form with five questions. The system checks answers for relevant keywords such as:
- teaching
- students
- learning
- technology
- explain
- knowledge
- experience
- research
- practical
- project

Each keyword match increases the interview score. The final interview score is then categorized as:
- Strong Interview Performance
- Good Interview Performance
- Needs Further Review

### 6.4 Admin Login Module
The admin login route verifies the credentials against the stored database. The default admin account is:
- Username: admin
- Password: admin123

### 6.5 Admin Dashboard
The dashboard displays candidate records ranked by score and interview score. It also provides summary statistics:
- Total candidates
- Selected
- Rejected
- Under Review

Admins can update the final candidate status through a dropdown.

---

## 7. Database Design
The project uses SQLite with a lightweight schema designed for quick deployment and local development.

### 7.1 Table: candidates
The `candidates` table stores all screening and interview details.

Fields:
- id: Primary key
- name: Candidate name
- email: Candidate email
- qualification: Highest qualification
- experience: Work experience in years
- specialization: Domain specialization
- score: Screening score
- status: Screening result status
- interview_score: Interview performance score
- interview_status: Interview status label
- selection_status: Final admin selection status

### 7.2 Table: admins
The `admins` table stores admin details used for authentication.

Fields:
- id: Primary key
- username: Unique admin username
- password: Admin password

### 7.3 Database Notes
The schema supports a simple recruitment workflow where candidates are evaluated, reviewed, and ranked without needing a more advanced relational system.

---

## 8. Deployment and Database Fixes
A key issue observed during production deployment was caused by a database schema mismatch and deployment environment differences.

### 8.1 Problem Encountered
The dashboard queries `selection_status`, but older SQLite databases did not include this column. As a result, the deployed app on Render could fail when opening the admin dashboard, even though the home page loaded correctly.

### 8.2 Fix Implemented
The database initialization logic was updated to include the `selection_status` column in the schema and to automatically migrate older databases when the column is missing.

This fix ensures compatibility between:
- newly created databases
- older local SQLite databases created before the module update
- Render-hosted deployment instances

### 8.3 Render Deployment Requirements
A root-level `requirements.txt` file was also added so that Render could install dependencies correctly using the standard deployment command:
- pip install -r requirements.txt

The project uses:
- Flask
- gunicorn

This is important because Render needs dependencies to be available at the project root.

---

## 9. Current Implementation Summary
The current project is fully functional as a prototype application and includes the following final features:
- Candidate screening with score generation
- Interview evaluation
- Admin authentication
- Candidate ranking dashboard
- Selection status updates
- SQLite persistence
- Deployment compatibility fixes for local and hosted versions

---

## 10. Tools and Technologies Used
- Python
- Flask
- SQLite
- HTML/CSS
- Render (deployment)
- GitHub (version control)

---

## 11. Screenshots and Demo Database Files
The project also includes demo materials for documentation and presentation:
- `demo_schema.sql` contains the schema and sample data
- `er_diagram.md` contains the ER diagram for the database
- These files can be used for final presentation screenshots and project explanations

---

## 12. Challenges and Lessons Learned
Some major learning outcomes from the project were:
- SQLite is simple and useful for local prototyping, but it is not ideal for large-scale production databases.
- Deployment issues often arise from environment differences, especially when using local database files.
- Database migration logic is essential when app schemas evolve.
- A hosted app must include all required dependencies and correct deployment settings.

---

## 13. Future Enhancements
The system can be improved in future versions by adding:
- Real AI-based candidate analysis using NLP models
- User registration and role-based access control
- PostgreSQL migration for production deployment
- Candidate resume parsing
- Automated report generation
- Email notifications for status updates
- Better admin analytics and charts

---

## 14. Conclusion
SmartHireAI demonstrates how artificial intelligence and web application development can support recruitment decisions in an efficient and structured way. The updated system successfully combines automated candidate evaluation, a short interview assessment, and an admin dashboard for ranking and selection management.

The final project now includes the necessary deployment and database compatibility improvements, making it more reliable for both local use and hosted deployment on Render.

---

## 15. References
- Flask documentation
- SQLite documentation
- Render deployment documentation
- Project source files in the workspace:
  - app.py
  - database.py
  - rules.py
  - templates/
  - static/

---

## 16. Final Note
This report reflects the current version of the SmartHireAI project after resolving the deployed database issue and updating the project for compatibility with local and hosted SQLite environments.
