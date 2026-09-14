# SmartHireAI ER Diagram

This diagram matches the current SQLite schema in `database.py`.

```mermaid
erDiagram
    ADMINS {
        INTEGER id PK
        TEXT username UK
        TEXT password
    }

    CANDIDATES {
        INTEGER id PK
        TEXT name
        TEXT email
        TEXT qualification
        INTEGER experience
        TEXT specialization
        INTEGER score
        TEXT status
        INTEGER interview_score
        TEXT interview_status
        TEXT selection_status
    }
```

`admins` and `candidates` are separate tables in the current application. There is no foreign-key relationship between them; the administrator manages candidate records through the Flask dashboard.
