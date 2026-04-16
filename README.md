# 02 Booking System

A command-line client booking system built in Python as part of a portfolio project series targeting a £90k+ AI/tech role in London.

## Features

- Add new clients with optional fields (date of birth, gender, source, notes)
- View all saved clients with note count
- Search clients by email or phone number (shows notes on match)
- Update any client field with input validation
- Manage client notes — view, add, delete one, delete all (with confirmation)
- Delete clients with confirmation step
- Data persists between sessions via JSON file

## Project Structure

```
02_booking_system/
│
├── client.py            # Client class with UUID, field definitions and safe list defaults
├── client_service.py    # All client logic: CRUD, notes management, save/load, validation
├── booking_system.py    # Main entry point — menu loop and user interaction
└── data.json            # Auto-generated data file (not committed)
```

## Concepts Demonstrated

- Object-oriented programming — Client class with UUID
- Separation of concerns — logic split across three files
- JSON persistence — save and load client data
- Input validation — date format, gender, Y/N prompts with reusable functions
- Notes management — list operations (append, pop, clear) with validation
- Boolean flags — tracking search results cleanly
- Error handling — `try/except` for file, JSON, and integer conversion errors
- Date serialization — converting `date` objects to isoformat strings for JSON
- `enumerate` — clean indexed iteration without manual counters
- Safe mutable defaults — avoiding the Python mutable default argument trap

## How to Run

```bash
cd 02_booking_system
python booking_system.py
```

## Menu Options

```
1. View clients       — lists all clients with note count
2. Add client         — add new client with optional fields
3. Search client      — find by email or phone, shows notes
4. Update client      — edit any field including notes sub-menu
5. Delete client      — delete with confirmation
0. Exit               — saves and exits
```

## Next Steps

- Appointment class and booking logic
- AI receptionist integration (future capstone)

## Part of a Larger Project Series

| # | Project | Status |
|---|---------|--------|
| 01 | Finance Tracker | ✅ Complete |
| 02 | Booking System | 🔄 In Progress |
| 03 | Stock Dashboard | ⏳ Planned |
| 04 | Fraud Detection ML | ⏳ Planned |
| 05 | Security Tool | ⏳ Planned |
| 06 | AI Receptionist (SaaS) | ⏳ Capstone |