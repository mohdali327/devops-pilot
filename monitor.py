# monitor.py
import subprocess

def run_and_capture_error():
    print("🔍 Monitoring target_app.py...")
    # Using python3 for Mac compatibility
    result = subprocess.run(['python3', 'target_app.py'], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("🚨 CRASH DETECTED!")
        return result.stderr 
    return None