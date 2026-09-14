-- SmartHireAI demo database
-- SQLite-compatible schema and sample data for screenshots/documentation.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    qualification TEXT NOT NULL,
    experience INTEGER NOT NULL,
    specialization TEXT NOT NULL,
    score INTEGER NOT NULL,
    status TEXT NOT NULL,
    interview_score INTEGER DEFAULT 0,
    interview_status TEXT DEFAULT 'Not Completed',
    selection_status TEXT DEFAULT 'Under Review'
);

CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Demo login used by the current application.
INSERT OR IGNORE INTO admins (username, password)
VALUES ('admin', 'admin123');

-- Five sample records for the dashboard and screenshots.
INSERT OR IGNORE INTO candidates
    (name, email, qualification, experience, specialization, score, status,
     interview_score, interview_status, selection_status)
VALUES
    ('Dr. Ananya Sharma', 'ananya.sharma@example.com', 'PhD Computer Science', 8,
     'Artificial Intelligence', 92, 'Shortlisted', 88, 'Strong Interview Performance', 'Selected'),
    ('Prof. Daniel Wilson', 'daniel.wilson@example.com', 'M.Tech Software Engineering', 6,
     'Software Engineering', 84, 'Shortlisted', 78, 'Good Interview Performance', 'Selected'),
    ('Dr. Meera Patel', 'meera.patel@example.com', 'PhD Information Systems', 5,
     'Data Science', 79, 'Shortlisted', 70, 'Good Interview Performance', 'Under Review'),
    ('Mr. James Carter', 'james.carter@example.com', 'M.Sc Computer Science', 3,
     'Cybersecurity', 68, 'Under Review', 58, 'Good Interview Performance', 'Under Review'),
    ('Ms. Sofia Khan', 'sofia.khan@example.com', 'MCA', 2,
     'Web Technologies', 61, 'Under Review', 45, 'Needs Further Review', 'Rejected');

-- Useful screenshot queries:
-- SELECT * FROM admins;
-- SELECT * FROM candidates ORDER BY (score + interview_score) DESC;
