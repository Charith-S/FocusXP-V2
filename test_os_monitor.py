"""
FocusXP OS Monitor Test (CORRECTED - Fixed Paths)
"""

import sys
import os

# FIXED: Add project root to path (assuming run from project root)
project_root = os.path.abspath('.')
sys.path.insert(0, project_root)

# Debug: Print current dir and paths
print(f"📁 Current directory: {os.getcwd()}")
print(f"📁 Project root added: {project_root}")
print(f"📂 src folder exists: {os.path.exists('src')}")
print(f"📂 src/detection exists: {os.path.exists('src/detection')}")
print(f"📂 os_monitor.py exists: {os.path.exists('src/detection/os_monitor.py')}")

try:
    from src.detection.os_monitor import OSMonitor
    print("✅ OSMonitor imported successfully!")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    print("\n🔧 Troubleshooting:")
    print("   - Run from 'New folder' directory")
    print("   - Verify src/detection/os_monitor.py has the code")
    print("   - Python 3.13 sometimes needs 'python -m' for paths")
    print("\n💡 Try the standalone test below instead")
    sys.exit(1)

# Import database for session test
try:
    from src.data.database import Database
    from src.data.repositories import SessionRepository
    print("✅ Database imports successful!")
except ImportError as e:
    print(f"❌ Database import failed: {e}")
    sys.exit(1)

if __name__ == "__main__":
    print("\n🧪 Testing OS Monitor...")
    
    monitor = OSMonitor()
    
    print("\n1. 🔍 VSCode Detection:")
    running = monitor.is_vscode_running()
    if running:
        print("✅ VSCode DETECTED!")
        print(f"   PID: {monitor.vscode_process['pid'] if monitor.vscode_process else 'Unknown'}")
        print(f"   Name: {monitor.vscode_process['name'] if monitor.vscode_process else 'Unknown'}")
    else:
        print("❌ VSCode not detected")
        print("   💡 Open VSCode and re-run to test!")
    
    print("\n2. 📊 Active Processes:")
    procs = monitor.get_active_processes()
    if procs:
        for p in procs:
            print(f"   • {p['name']} (PID: {p['pid']})")
    else:
        print("   No targets found")
    
    print("\n3. 🧪 Manual Session Test:")
    try:
        monitor.manual_start_session("Test Project")
        print("✅ Manual session created!")
        print("   Check data/focusxp.db for entry (ID should print)")
    except Exception as e:
        print(f"❌ Session error: {e}")
    
    print("\n✅ Test complete! Paste this output in reply.")
