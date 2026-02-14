# agent.py
import ollama
import re

def get_fix_from_ai(error_log, file_content):
    prompt = f"""
    Fix the following Python bug. 
    ERROR: {error_log}
    CODE: {file_content}
    Return ONLY the corrected code inside triple backticks like this:
    ```python
    (your code)
    ```
    """
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    content = response['message']['content']
    
    # Extract only the code inside backticks
    match = re.search(r"```(?:python)?\n?(.*?)```", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return content.strip()