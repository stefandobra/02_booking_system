# 02 Booking System

A command-line client booking system built in Python as part of a portfolio project series targeting a £90k+ AI/tech role in London.

## Features

- Add new clients with optional fields (date of birth, gender, source, notes)
- View all saved clients
- Search clients by email or phone number
- Update any client field with input validation
- Delete clients
- Data persists between sessions via JSON file

## Project Structure

```
02_booking_system/
│
├── client.py            # Client class with UUID, field definitions and safe list defaults
├── client_service.py    # All client logic: CRUD, search, save/load, validation functions
├── booking_system.py    # Main entry point — menu loop and user interaction
└── data.json            # Auto-generated data file (not committed)
```

## Concepts Demonstrated

- Object-oriented programming — Client class with UUID
- Separation of concerns — logic split across three files
- JSON persistence — save and load client data
- Input validation — date format, gender, Y/N prompts
- Reusable validation functions — `validate_dob`, `validate_gender`
- Boolean flags — tracking search results cleanly
- Error handling — `try/except` for file and JSON errors
- Date serialization — converting `date` objects to strings for JSON compatibility

## How to Run

```bash
cd 02_booking_system
python booking_system.py
```

## Next Steps

- Notes management (add, view, delete notes per client)
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