🖥️ System Monitoring Agent

An AI-inspired system monitoring agent built using Python that continuously observes system activity, analyzes events, maintains memory, and sends real-time alerts using Twilio.

The project is designed with a modular, agent-based architecture, making it easy to extend, automate, and scale into a full monitoring or automation product.

🚀 Key Features

🔍 Continuous system observation

🧠 Stateful memory and historical tracking

📊 Intelligent analysis layer

🚨 Real-time alerting via SMS

🧩 Modular, multi-agent design

📁 Persistent logs and history

⚙️ Config-driven behavior

🧠 Agent Architecture

The system is built as a coordinated group of agents, each with a single responsibility.

Module	Description
agent.py	Main orchestrator that runs the agent loop
observer.py	Observes system events and metrics
analyzer.py	Analyzes observed data for conditions
memory.py	Stores historical context and state
notifier.py	Sends alerts and notifications
config.py	Centralized configuration

This separation ensures:

High maintainability

Easy testing

Plug-and-play extensibility

🔄 Workflow

Observer captures system data

Analyzer evaluates data against rules

Memory stores relevant state/history

Notifier triggers alerts when required

Agent coordinates the entire lifecycle

🛠️ Tech Stack

Python 3

Object-oriented design

JSON-based persistence

Environment-based secrets management

External alerting integration

📂 Project Structure
system_agent/
│
├── agent.py
├── observer.py
├── analyzer.py
├── memory.py
├── notifier.py
├── config.py
│
├── logs/
│   └── history.json
│
├── history.json
├── .gitignore
└── README.md

▶️ How to Run
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/system_agent.git
cd system_agent

2️⃣ Create and activate virtual environment
python -m venv .venv


Windows

.venv\Scripts\activate


Mac / Linux

source .venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

📲 Twilio Configuration (Required for Alerts)

This project uses Twilio SMS to send system alerts.

Step 1: Create a Twilio account

Sign up on Twilio

Get:

Account SID

Auth Token

Twilio phone number

Step 2: Create .env file

Create a .env file in the project root:

TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
TARGET_PHONE_NUMBER=+91XXXXXXXXXX


⚠️ Important

.env must NOT be committed

Ensure .env is listed in .gitignore

Step 3: Verify configuration

Check config.py to ensure environment variables are loaded correctly.

4️⃣ Run the agent
python agent.py


You should see logs indicating:

Agent startup

Observation cycle

Analysis events

Notification triggers (if conditions are met)

📨 Notifications

Alerts are sent via SMS

Triggered when defined system conditions are satisfied

Notification layer is easily extendable

🔮 Future Enhancements

📈 CPU, RAM, Disk monitoring

🤖 ML-based anomaly detection

🌐 Web dashboard (React + FastAPI)

📨 Email / WhatsApp / Slack alerts

🧩 Plugin-based agent extensions

🗄️ Database-backed memory (Redis / PostgreSQL)

⏱️ Task scheduling & automation

🔒 Security Best Practices

Store secrets in .env

Never hard-code credentials

Rotate Twilio tokens periodically

Add rate-limiting for alerts

🤝 Contributions & Ideas

Suggestions, improvements, and agent ideas are welcome!

You can contribute by:

Opening issues

Creating pull requests

Proposing new agents or workflows

👨‍💻 Author

Shivam Sharma
B.Tech | AI Agents | Cybersecurity | Automation

🔗 GitHub: https://github.com/cyberbuddyshivam/System-Monitoring-Agent.git
LinkedIn : https://www.linkedin.com/in/cyberbuddyshivam/

⭐ Support

If you found this project useful:

Give it a ⭐ on GitHub

Share feedback or ideas

Use it as a base for your own agents
