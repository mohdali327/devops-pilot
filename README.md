🚀 DevOps-Pilot: Autonomous Self-Healing Code Pipeline
DevOps-Pilot is an AI-driven agent designed to automate fault localization, remediation, and deployment in a CI/CD environment. Using a local LLM (Llama 3), the system intercepts runtime crashes, generates context-aware patches, and automatically submits Pull Requests for human verification.

🛠️ The Tech Stack
Intelligence: Llama 3 (via Ollama)

Orchestration: Python 3.10+

Monitoring: Subprocess-based stderr interception

Automation: PyGithub (GitHub REST API)

Environment: macOS (M-series optimized)

🧠 System Architecture
The Watcher (monitor.py): Continuously monitors target applications for crashes and captures full stack traces.

The Brain (agent.py): Utilizes Llama 3 to analyze the crash and generate a specific, regex-cleaned code patch.

The Orchestrator (main.py): Coordinates the healing loop, applies patches locally, and verifies the fix.

The Muscle (github_integration.py): Automatically creates a new Git branch, commits the fix, and opens a Pull Request.

📊 Performance Metrics
Based on empirical testing, the agent achieved the following benchmarks:

Mean Time to Repair (MTTR): ~11.52 seconds.

Success Rate: 100% on tested KeyError and NameError exceptions.

Deployment: Fully automated PR generation on successful local verification.
📜 Research Context
This project was developed as a study into Autonomous Remediation within Data Science pipelines. It demonstrates that local LLMs can significantly reduce downtime by automating "Tier 1" debugging tasks.
