# Salon Booking System

A command-line booking management system built in Python, designed based on real salon operations.

## What it does
- Add, view, update and delete clients (CRUD)
- Book, reschedule and cancel appointments
- Persist all data locally using JSON storage
- Built with proper separation of concerns (service layer pattern)

## Tech used
- Python 3.12
- JSON (local data persistence)
- UUID (unique client/appointment IDs)
- python-datetime (date validation)

## Known limitations
- No calendar or real-time availability checking yet
- No validation on phone number or email format
- Appointment booking not yet implemented
- Data only saves on clean exit (option 0)

## Why I built it
Second project in my AI builder journey — building on real experience running a beauty salon. Foundation for the AI Receptionist capstone project.

## Project structure
- `client.py` — Client class definition
- `client_service.py` — Client management functions (add, view, update, delete)
- `booking_system.py` — Main program and menu

## Author
Stefan Dobra — [github.com/stefandobra](https://github.com/stefandobra)