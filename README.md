# FocusXP - Coding Activity Tracker with Gamification

**Version:** 1.0 (Full Release)  
**Platform:** Windows 11 / Linux / macOS  
**Tech Stack:** Python 3.13, PyQt5, SQLite, Matplotlib

## 🎯 Features

### ✅ Core Functionality
- **Auto-Detection:** Tracks VSCode, PyCharm, Sublime, Atom automatically
- **Session Logging:** Records start/end times, duration, project paths
- **Manual Entry:** Add custom sessions with timestamps and notes
- **Session Management:** View, edit, delete sessions in table view
- **CSV Export:** Export full session history with one click

### 💎 Gamification System
- **XP Rewards:** Earn 10 XP per minute coded
- **Level Progression:** Advance levels every 1000 XP
- **Progress Tracking:** Visual progress bar to next level
- **Motivation:** Track cumulative XP and coding milestones

### 📊 Analytics Dashboard
- **Total Coding Time:** Lifetime hours and minutes tracked
- **7-Day Chart:** Bar graph of daily coding activity
- **XP & Level Display:** Real-time gamification stats
- **Auto-Refresh:** Updates when sessions change

### ⚙️ Configuration
- **Monitoring Control:** Start/stop auto-detection via Settings
- **Poll Interval:** Adjust check frequency (1-60 seconds)
- **Multi-IDE:** Supports multiple coding applications

## 🚀 Installation

### Prerequisites
- Python 3.13+ (tested on 3.13.5)
- pip package manager

### Setup
1. Navigate to project directory
cd "path/to/FocusXP"

2. Install dependencies
pip install PyQt5 matplotlib psutil

3. Initialize database (one-time)
python add_notes_column.py
python init_xp_system.py

4. Run application
python main.py


## 📖 Usage Guide

### Auto-Tracking
1. Launch FocusXP: `python main.py`
2. Go to **Settings** tab → Click **"▶️ Start Monitoring"**
3. Open VSCode/IDE → FocusXP auto-detects and starts session
4. Code normally → Session runs in background
5. Close IDE → Session ends automatically with XP awarded

**Console Output Example:**
🚀 New session started: ID=9
App: Code | Project: Unknown | Start: 19:33:49
⏹️ Session ended: ID=9
Duration: 1 min 10 sec | 💎 XP Earned: 10


### Manual Sessions
1. **Sessions** tab → Click **"➕ Add Manual Session"**
2. Fill form:
   - Project path (e.g., "My Project")
   - Application (dropdown: VSCode, PyCharm, etc.)
   - Start/End times (date pickers)
   - Notes (optional journal entry)
3. Click **OK** → Session added with XP

### View Statistics
- **Dashboard Tab:**
  - Total coding time (hours, minutes)
  - Total XP and current level
  - Progress bar (XP to next level)
  - 7-day activity bar chart

### Export Data
- **Sessions Tab** → Click **"📥 Export to CSV"**
- File saved to `exports/focusxp_sessions_[timestamp].csv`
- Open in Excel/Google Sheets for analysis

### Settings
- **Poll Interval:** How often to check for IDE (default: 5s)
- **Monitoring Toggle:** Start/stop auto-detection
- **Save Settings:** Persist configurations (future: config.json)

## 📁 Project Structure
FocusXP/
├── main.py # Application entry point
├── src/
│ ├── data/ # Database layer (SQLite)
│ │ ├── database.py # Connection manager
│ │ └── repositories.py # CRUD + XP operations
│ ├── detection/ # OS monitoring
│ │ └── os_monitor.py # Process detection
│ ├── ui/ # PyQt5 GUI
│ │ ├── main_window.py # Main application window
│ │ ├── dashboard_widget.py # Analytics & charts
│ │ ├── session_widget.py # Session table & forms
│ │ └── settings_widget.py # Configuration panel
│ └── utils/ # Utilities
│ └── export.py # CSV/JSON exporters
├── data/
│ └── focusxp.db # SQLite database
├── exports/ # CSV output folder
├── tests/ # Unit tests
├── docs/ # Documentation
│ ├── README.md
│ └── Design_Code_Alignment.md
└── requirements.txt



## 🐛 Troubleshooting

**GUI Hangs:**  
- Fixed in v1.0 - monitoring runs in background thread

**VSCode Not Detected:**  
- Ensure Code.exe is running (check Task Manager)
- Verify Settings → Monitoring is "🟢 Active"
- Check `TARGET_PROCESSES` in `os_monitor.py`

**Duration Shows 0 Minutes:**  
- Start monitoring via Settings before opening IDE
- Wait 5-10 seconds after closing IDE (poll interval)
- Check console for "Session ended" message

**Database Errors:**  
- Delete `data/focusxp.db` to reset
- Re-run `add_notes_column.py` and `init_xp_system.py`

**Font Warnings (Cosmetic):**  
- Harmless - emoji fallback in chart titles
- Chart renders correctly despite warning

## 📊 Design & Alignment

See `docs/Design_Code_Alignment.md` for:
- UML diagram mappings (Class, Sequence, Use Case)
- Code-to-requirements traceability
- SDLC compliance documentation

## 👨‍💻 Development

**Author:** [Your Name]  
**Course:** OOSE Lab (CSM 416)  
**Institution:** [Your University]  
**Year:** 2025

**Testing:**
Run unit tests
python -m pytest tests/test_database.py

Manual verification
python test_os_monitor.py


## 📜 License

Academic Project - All Rights Reserved (2025)

---

**🎉 Thank you for using FocusXP! Happy coding!**