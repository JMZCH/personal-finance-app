# Personal Finance App

A command-line personal finance manager built with Python. Track your income and expenses, calculate your balance, and keep your data persistent between sessions.

## Features
- Add and categorize expenses
- Add income entries
- Calculate real-time balance
- Persistent data storage with JSON
- Input validation and error handling

## Tech Stack
- Python 3.14
- JSON

## Project Structure
personal-finance-app/
├── main.py        # Main application logic and menu
├── storage.py     # Data persistence (save/load)
├── utils.py       # Validation utilities
└── data.json      # Local data storage (not tracked)
## How to Run
1. Clone the repository
```bash
git clone https://github.com/JMZCH/personal-finance-app.git
cd personal-finance-app
```
2. Run the app
```bash
python main.py
```

## Roadmap
- [ ] REST API with FastAPI
- [ ] Web interface
- [ ] PostgreSQL database integration
- [ ] Authentication system