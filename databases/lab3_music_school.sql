CREATE TABLE students (
	student_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	instrument_id INTEGER,
	FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);

CREATE TABLE lessons (
	lesson_id INTEGER PRIMARY KEY,
	teacher_id INTEGER, 
	instrument_id INTEGER, 
	room_id INTEGER,
	lesson_date TEXT,
	lesson_time TEXT,
	FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
	FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
	FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE rooms (
	room_id INTEGER PRIMARY KEY,
	name TEXT,
	capacity INTEGER
);

CREATE TABLE students_lessons (
	student_id INTEGER NOT NULL,
	lesson_id INTEGER NOT NULL,
	PRIMARY KEY (student_id, lesson_id),
	FOREIGN KEY (student_id) REFERENCES students(student_id),
	FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id)
);

CREATE TABLE teachers (
	teacher_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE instruments (
	instrument_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE teacher_instruments (
	teacher_id INTEGER NOT NULL,
	instrument_id INTEGER NOT NULL,
	PRIMARY KEY (teacher_id, instrument_id),
	FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
	FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);