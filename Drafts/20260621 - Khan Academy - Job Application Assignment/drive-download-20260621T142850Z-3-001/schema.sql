-- Table to store student details
CREATE TABLE IF NOT EXISTS student_details (
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    contact_number INTEGER NOT NULL,
    email_id    TEXT NOT NULL,
    school_id   TEXT NOT NULL,
    grade       TEXT NOT NULL
);

-- Table to store CMF (Child Monitoring Form) input data
CREATE TABLE IF NOT EXISTS cmf_input (
    id           TEXT PRIMARY KEY,
    child_id     TEXT NOT NULL,
    school_id    TEXT NOT NULL,
    submitted_at TEXT NOT NULL,
    status       TEXT NOT NULL
);

-- Table to store CMF metrics (processed results)
CREATE TABLE IF NOT EXISTS cmf_metrics (
    id              TEXT PRIMARY KEY,
    input_id        TEXT NOT NULL REFERENCES cmf_input(id),
    processed_date  TEXT NOT NULL,
    wpm             INTEGER NOT NULL,
    wcpm            REAL NOT NULL,
    pronunciation   INTEGER NOT NULL,
    fluency         REAL NOT NULL,
    noise           INTEGER NOT NULL
);
