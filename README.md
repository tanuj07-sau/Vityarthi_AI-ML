# AI Timetable Generator

A Python-based weekly timetable generator for college/school schedules. It supports both **manual entry** and **AI-powered automatic generation**, with built-in conflict detection, subject tracking, and formatted output.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup & Installation](#setup--installation)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [Subjects & Teachers](#subjects--teachers)
- [How It Works](#how-it-works)
- [Sample Output](#sample-output)
- [Customization](#customization)

---

## Overview

This project automatically generates a conflict-free weekly class timetable for a 5-day week (Monday–Friday) with 7 time slots per day, including a fixed lunch break. You can either fill in the timetable yourself or let the AI engine handle it instantly.

---

## Features

- **AI Auto Mode** — Generates a valid timetable in milliseconds using a randomized constraint-satisfaction approach
- **Manual Mode** — Step-by-step guided entry for each day and time slot
- **Both Mode** — Run both modes side-by-side and compare results
- **Conflict Detection** — Prevents the same subject from appearing twice on the same day
- **Subject Summary** — Verifies that every subject has been scheduled the correct number of times per week
- **Lunch Break Auto-fill** — 12:00 PM – 1:00 PM is automatically reserved every day
- **Free Period Support** — Unfilled slots are neatly labeled as "Free Period"
- **Clean Formatted Output** — Timetable prints as a well-aligned ASCII table in the terminal

---

## Project Structure

```
ai-timetable-generator/
│
└── timetable.py        # Main script — all logic lives here
```

---

## Requirements

- **Python 3.6 or higher**
- No external libraries needed — uses only Python's built-in `random` module

---

## Setup & Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/ai-timetable-generator.git
cd ai-timetable-generator
```

**2. (Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate       
```

**3. No further installation needed** — there are no external dependencies.

---

## How to Run

```bash
python timetable.py
```

You will be greeted with this menu:

```
**************************************************
*   AI TIMETABLE GENERATOR                       *
**************************************************

Choose timetable mode:
  1. Manual   - I will fill in the timetable myself
  2. AI Auto  - Let AI generate the timetable
  3. Both     - Generate both timetables and compare

Enter your choice (1 / 2 / 3):
```

---

## Usage Guide

### Mode 1 — Manual

- You are walked through each day (Monday to Friday) and each time slot one by one.
- A numbered list of subjects is shown. Enter the number corresponding to your chosen subject.
- Enter `0` to mark a slot as a Free Period.
- If you try to place a subject that's already been placed that day, you'll get a warning and a chance to confirm or pick again.

### Mode 2 — AI Auto

- The AI engine generates a complete, valid timetable automatically.
- Each subject is scheduled exactly the required number of times per week.
- No subject appears twice on the same day.
- Generation is almost always instant (typically 1 attempt).

### Mode 3 — Both

- Runs Manual mode first, then AI Auto mode.
- Prints both timetables one after the other so you can compare.

---

## Subjects & Teachers

| Subject                | Teacher          | Classes/Week |
|------------------------|------------------|:------------:|
| Calculus               | Mr. TANUJ        | 4            |
| Computational Physics  | Mr. PRIYANSHU    | 3            |
| Comp. Chemistry        | Dr. AYUSH        | 3            |
| English                | Mr. ANANT        | 3            |
| Transform              | Mr. ANSHU        | 4            |
| PYTHON                 | Mr. PRATEEK      | 2            |
| C++                    | Mr. CHARAN       | 2            |
| **Total**              |                  | **21**       |

---

## Time Slots

| Slot | Time              |
|------|-------------------|
| 1    | 9:00 AM – 10:00 AM  |
| 2    | 10:00 AM – 11:00 AM |
| 3    | 11:00 AM – 12:00 PM |
|      | 12:00 PM – 1:00 PM *(Lunch Break)* |
| 4    | 1:00 PM – 2:00 PM   |
| 5    | 2:00 PM – 3:00 PM   |
| 6    | 3:00 PM – 4:00 PM   |

---

## How It Works

### AI Engine

1. Builds a **pool** of all class sessions (e.g., 4 × Calculus, 3 × English, etc.)
2. Shuffles the pool randomly
3. For each class session, tries random (day, slot) combinations until a valid one is found
4. A placement is valid if:
   - The slot is currently empty
   - The subject hasn't already been placed on that day
5. If placement fails for any subject, the whole attempt is discarded and retried (up to 100 times)
6. Remaining empty slots are filled with "Free Period"

> With 21 classes and 30 available slots across the week, a valid timetable is mathematically guaranteed to exist, and the AI finds one on the **first attempt** virtually every time.

### Constraint Enforced

> **One subject maximum per day** — the same class cannot appear twice on the same day.

---

## Sample Output

```
===========================================================================
  AI GENERATED TIMETABLE
===========================================================================
Time Slot                Monday              Tuesday             Wednesday
---------------------------------------------------------------------------
9:00 AM - 10:00 AM       Calculus            PYTHON              Transform
10:00 AM - 11:00 AM      English             Transform           Calculus
11:00 AM - 12:00 PM      Comp. Chemistry     Calculus            English
12:00 PM - 1:00 PM       Lunch Break         Lunch Break         Lunch Break
1:00 PM - 2:00 PM        Transform           English             PYTHON
2:00 PM - 3:00 PM        Free Period         Comp. Chemistry     Free Period
3:00 PM - 4:00 PM        C++                 Free Period         C++
===========================================================================

  SUBJECT SCHEDULE SUMMARY
------------------------------------------------------------
[OK ] Calculus               | Mr. TANUJ      | 4/4 classes
[OK ] Computational Physics  | Mr. PRIYANSHU  | 3/3 classes
[OK ] Comp. Chemistry        | Dr. AYUSH      | 3/3 classes
[OK ] English                | Mr. ANANT      | 3/3 classes
[OK ] Transform              | Mr. ANSHU      | 4/4 classes
[OK ] PYTHON                 | Mr. PRATEEK    | 2/2 classes
[OK ] C++                    | Mr. CHARAN     | 2/2 classes
------------------------------------------------------------
 All subjects scheduled correctly!
```

---

## Customization

You can easily modify the script to fit your own schedule:

**Change subjects or weekly frequency:**
```python
SUBJECTS = {
    "Mathematics": 5,
    "Physics":     3,
    "History":     2,
}
```

**Change teacher names:**
```python
TEACHERS = {
    "Mathematics": "Ms. Smith",
    "Physics":     "Mr. Johnson",
}
```

**Add or remove days:**
```python
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
```

**Change time slots:**
```python
TIME_SLOTS = [
    "8:00 AM - 9:00 AM",
    "9:00 AM - 10:00 AM",
    ...
]
```

> Make sure `LUNCH_SLOT` matches one of the entries in `TIME_SLOTS` exactly.

---

## License

This project is open source and free to use for educational purposes.

---

## Author

Built as a student scheduling tool. Contributions and suggestions are welcome!
