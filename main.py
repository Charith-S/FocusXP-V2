"""
FocusXP Main Application Entry Point (FIXED - Settings-Controlled Monitoring)
Launches PyQt5 GUI. Monitor started/stopped via Settings tab only.
"""

import sys
import os
import threading

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication

from src.ui.main_window import MainWindow
from src.detection.os_monitor import OSMonitor
from src.data.database import Database
from src.data.repositories import SessionRepository


def start_monitoring_thread(monitor):
    """Run monitor in background thread."""
    try:
        monitor.start_monitoring()
    except Exception as e:
        print(f"❌ Monitor thread error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Initialize modules
    db = Database()
    repo = SessionRepository(db)
    
    # Explicitly disable auto-start for safety — user controls monitoring via Settings
    monitor = OSMonitor(repo, auto_start=False)
    
    # Create main window (pass monitor for Settings control)
    window = MainWindow(repo, monitor)
    window.show()
    
    print("✅ FocusXP GUI launched! Use Settings tab to start monitoring.")
    
    sys.exit(app.exec_())
