# 02 Booking System

A command-line client booking system built in Python as part of a portfolio project series targeting a £90k+ AI/tech role in London.

## Features

- Add new clients with optional fields (date of birth, gender, source, notes)
- View all saved clients with note count
- Search clients by email or phone number (shows notes on match)
- Update any client field with input validation
- Manage client notes — view, add, delete one, delete all (with confirmation)
- Delete clients with confirmation step
- Add appointments linked to clients with therapist, treatment and datetime
- View all appointments with formatted date and client name
- Data persists between sessions via JSON files

## Project Structure

```
02_booking_system/
│
├── client.py                # Client class with UUID and safe list defaults
├── client_service.py        # All client logic: CRUD, notes management, save/load, validation
├── appointment.py           # Appointment class with UUID and field definitions
├── appointment_service.py   # Appointment logic: add, view, save/load, datetime validation
├── booking_system.py        # Main entry point — menu loop and user interaction
├── data.json                # Auto-generated client data (not committed)
└── appointments.json        # Auto-generated appointment data (not committed)
```

## Concepts Demonstrated

- Object-oriented programming — Client and Appointment classes with UUID
- Separation of concerns — logic split across multiple files
- JSON persistence — save and load data across two files
- Input validation — date, datetime, gender, Y/N prompts with reusable functions
- Notes management — list operations (append, pop, clear) with validation
- Boolean flags — tracking search results cleanly
- Error handling — `try/except` for file, JSON, and integer conversion errors
- Date serialization — converting datetime objects to isoformat strings for JSON
- `enumerate` — clean indexed iteration without manual counters
- Safe mutable defaults — avoiding the Python mutable default argument trap
- Cross-list lookups — matching appointment client_id to client records

## How to Run

```bash
cd 02_booking_system
python booking_system.py
```

## Menu Options

```
1. View clients             — lists all clients with note count
2. Add client               — add new client with optional fields
3. Search client            — find by email or phone, shows notes
4. Update client            — edit any field including notes sub-menu
5. Delete client            — delete with confirmation
6. Add appointment          — book appointment linked to existing client
7. View all appointments    — list all appointments with formatted date and client name
0. Exit                     — saves and exits
```

## Next Steps

- View appointments by client
- Delete appointment
- AI receptionist integration (future capstone)

## Part of a Larger Project Series

| # | Project | Status |
|---|---------|--------|
| 01 | Finance Tracker | ✅ Complete |
| 02 | Booking System | 🔄 In Progress |
| 03 | Stock Dashboard | ⏳ Planned |
| 04 | Fraud Detection ML | ⏳ Planned |
| 05 | Security Tool | ⏳ Planned |
| 06 | YouTube/TikTok Pipeline | ⏳ Planned |
| 07 | AI Receptionist (SaaS) | ⏳ Capstone |