# main.py
import os
from dotenv import load_dotenv
from monitor import run_and_capture_error
from agent import get_fix_from_ai
from github_integration import push_to_github

load_dotenv() # Loads GITHUB_TOKEN and GITHUB_REPO from .env

def main():
    print("🚀 DevOps-Pilot Started.")
    error = run_and_capture_error()
    
    if error:
        with open('target_app.py', 'r') as f:
            code = f.read()
        
        print("🧠 Asking Llama 3 for a patch...")
        patch = get_fix_from_ai(error, code)
        
        print("🛠️ Applying patch...")
        with open('target_app.py', 'w') as f:
            f.write(patch)
        
        print("🔄 Verifying fix...")
        final_check = run_and_capture_error()
        
        if not final_check:
            print("🏆 SUCCESS: System Healed!")
            
            # GitHub Automation
            token = os.getenv("GITHUB_TOKEN")
            repo = os.getenv("GITHUB_REPO")
            if token and repo:
                print("📤 Pushing to GitHub...")
                pr_url = push_to_github(repo, token, "target_app.py", patch)
                print(f"🔗 Pull Request: {pr_url}")
        else:
            print("❌ Healing failed verification.")
    else:
        print("✅ System healthy.")

if __name__ == "__main__":
    main()