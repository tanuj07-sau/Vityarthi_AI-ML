import random

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

TIME_SLOTS = [
    "9:00 AM - 10:00 AM",
    "10:00 AM - 11:00 AM",
    "11:00 AM - 12:00 PM",
    "12:00 PM - 1:00 PM",
    "1:00 PM - 2:00 PM",
    "2:00 PM - 3:00 PM",
    "3:00 PM - 4:00 PM",
]

LUNCH_SLOT = "12:00 PM - 1:00 PM"

SUBJECTS = {
    "Calculus":               4,
    "Computational Physics":  3,
    "Comp. Chemistry":        3,   
    "English":                3,
    "Transform":              4,
    "PYTHON":                 2,
    "C++":                    2,
}


TEACHERS = {
    "Calculus":              "Mr. TANUJ",
    "Computational Physics": "Mr. PRIYANSHU",   
    "Comp. Chemistry":       "Dr. AYUSH",
    "English":               "Mr. ANANT",        
    "Transform":             "Mr. ANSHU",
    "PYTHON":                "Mr. PRATEEK",      
    "C++":                   "Mr. CHARAN",
}

SLOT_W    = 25
DAY_W     = 20
SUBJ_W    = 22
TEACHER_W = 15
TABLE_W   = SLOT_W + DAY_W * len(DAYS)


def build_empty_timetable():
    timetable = {}
    for day in DAYS:
        timetable[day] = {}
        for slot in TIME_SLOTS:
            if slot == LUNCH_SLOT:
                timetable[day][slot] = "Lunch Break"
            else:
                timetable[day][slot] = None
    return timetable


def build_class_pool():
    pool = []
    for subject, count in SUBJECTS.items():
        for _ in range(count):
            pool.append(subject)
    return pool


def print_timetable(timetable, title="WEEKLY TIMETABLE"):
    print("\n" + "=" * TABLE_W)
    print(f"  {title}")
    print("=" * TABLE_W)

    print(f"{'Time Slot':<{SLOT_W}}", end="")
    for day in DAYS:
        print(f"{day:<{DAY_W}}", end="")
    print()
    print("-" * TABLE_W)

    for slot in TIME_SLOTS:
        print(f"{slot:<{SLOT_W}}", end="")
        for day in DAYS:
            entry = timetable[day][slot] if timetable[day][slot] else "---"
            
            entry_display = entry[:DAY_W - 2] if len(entry) >= DAY_W else entry
            print(f"{entry_display:<{DAY_W}}", end="")
        print()

    print("=" * TABLE_W)


def print_subject_summary(timetable):
    print("\n  SUBJECT SCHEDULE SUMMARY")
    print("-" * 60)

    count = {}
    for day in DAYS:
        for slot in TIME_SLOTS:
            entry = timetable[day][slot]
           
            if entry and entry not in ["Lunch Break", "Free Period"]:
                count[entry] = count.get(entry, 0) + 1

    all_ok = True
    for subject in SUBJECTS:
        teacher   = TEACHERS.get(subject, "Unknown")
        scheduled = count.get(subject, 0)
        needed    = SUBJECTS[subject]
        status    = "OK " if scheduled == needed else "!!!"
        if status == "!!!":
            all_ok = False
        print(f"[{status}] {subject:<{SUBJ_W}} | {teacher:<{TEACHER_W}} | {scheduled}/{needed} classes")

    print("-" * 60)
    if all_ok:
        print(" All subjects scheduled correctly!")
    else:
        print(" Some subjects were not fully scheduled.")


def get_day_subjects(timetable, day):
    """Helper: returns a set of subjects already placed on a given day."""
    return {
        v for v in timetable[day].values()
        if v and v not in ("Lunch Break", "Free Period")
    }


def is_valid_placement(timetable, day, slot, subject):
    """A slot is valid if it is empty and the subject isn't already on that day."""
    if timetable[day][slot] is not None:
        return False
    if subject in get_day_subjects(timetable, day):
        return False
    return True


def make_ai_timetable(max_attempts=100):
    print("\n" + "=" * 50)
    print("  AI AUTO TIMETABLE MODE")
    print("  Generating timetable...")
    print("=" * 50)

    for attempt in range(1, max_attempts + 1):
        timetable = build_empty_timetable()
        pool = build_class_pool()
        random.shuffle(pool)

        slots = [
            (day, slot)
            for day in DAYS
            for slot in TIME_SLOTS
            if slot != LUNCH_SLOT
        ]

        failed = False
        for subject in pool:
            random.shuffle(slots)
            placed = False
            for day, slot in slots:
                if is_valid_placement(timetable, day, slot, subject):
                    timetable[day][slot] = subject
                    placed = True
                    break
            if not placed:
                failed = True
                break   

        if not failed:
            
            for day in DAYS:
                for slot in TIME_SLOTS:
                    if timetable[day][slot] is None:
                        timetable[day][slot] = "Free Period"
            print(f"  Done! Timetable generated in {attempt} attempt(s) 👍")
            return timetable

    print(f"  ⚠️  Could not generate a perfect timetable after {max_attempts} attempts.")
    print("  Returning best partial result.")
    for day in DAYS:
        for slot in TIME_SLOTS:
            if timetable[day][slot] is None:
                timetable[day][slot] = "Free Period"
    return timetable


def make_manual_timetable():
    print("\n" + "=" * 50)
    print("  MANUAL TIMETABLE MODE")
    print("  You will assign subjects to each slot.")
    print("=" * 50)

    subject_list = list(SUBJECTS.keys())
    print("\nAvailable subjects:")
    for i, subj in enumerate(subject_list):
        print(f"  {i + 1}. {subj}  (needs {SUBJECTS[subj]} classes/week)")

    timetable = build_empty_timetable()

    for day in DAYS:
        print(f"\n{'─' * 40}")
        print(f"  {day}")
        print(f"{'─' * 40}")
        for slot in TIME_SLOTS:
            if slot == LUNCH_SLOT:
                print(f"  {slot} --> Lunch Break (auto)")
                continue

            
            placed_today = get_day_subjects(timetable, day)
            if placed_today:
                print(f"\n  Already placed today: {', '.join(placed_today)}")

            print(f"\n  Slot: {slot}")
            print(f"  Enter subject number (1-{len(subject_list)}) or 0 for Free Period:")

            while True:
                try:
                    choice = int(input("  Your choice: "))
                    if choice == 0:
                        timetable[day][slot] = "Free Period"
                        break
                    elif 1 <= choice <= len(subject_list):
                        chosen = subject_list[choice - 1]
                       
                        if chosen in placed_today:
                            print(f"  ⚠️  '{chosen}' is already scheduled on {day}.")
                            print("  Are you sure? (y = yes, n = pick again): ", end="")
                            confirm = input().strip().lower()
                            if confirm != "y":
                                continue
                        timetable[day][slot] = chosen
                        break
                    else:
                        print(f"  Please enter a number between 0 and {len(subject_list)}.")
                except ValueError:
                    print("  Invalid input. Please enter a number.")

    return timetable


def main():
    print("\n" + "*" * 50)
    print("*   AI TIMETABLE GENERATOR                  *")
    print("*" * 50)
    print("\nChoose timetable mode:")
    print("  1. Manual   - I will fill in the timetable myself")
    print("  2. AI Auto  - Let AI generate the timetable")
    print("  3. Both     - Generate both timetables and compare")

    while True:
        choice = input("\nEnter your choice (1 / 2 / 3): ").strip()
        if choice in ("1", "2", "3"):
            break
        print("Please enter 1, 2, or 3.")

    if choice == "1":
        timetable = make_manual_timetable()
        print_timetable(timetable, "YOUR MANUAL TIMETABLE")
        print_subject_summary(timetable)

    elif choice == "2":
        timetable = make_ai_timetable()
        print_timetable(timetable, "AI GENERATED TIMETABLE")
        print_subject_summary(timetable)

    elif choice == "3":
        manual_tt = make_manual_timetable()
        ai_tt     = make_ai_timetable()

        print_timetable(manual_tt, "YOUR MANUAL TIMETABLE")
        print_subject_summary(manual_tt)

        print_timetable(ai_tt, "AI GENERATED TIMETABLE")
        print_subject_summary(ai_tt)

        print("\n  Both timetables printed above for comparison!")

    print("\n💡 Tip: Run the script again to get a fresh AI timetable!")


if __name__ == "__main__":
    main()