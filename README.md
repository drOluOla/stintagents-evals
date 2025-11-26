# StintAgents VoiceAI Evals & Safety

A platform to evaluate and test the safety of voice AI Agents that can interact and simulate workplace tasks and scenarios.

## Features

- 🎙️ Voice transcription using Faster-Whisper
- 🤖 Multi-agent coordination with OpenAI Agents SDK
- 🔊 Text-to-speech with agent-specific voices
- 🎨 Interactive Gradio interface with visual feedback
- 💾 Session management with SQLite storage

## Installation

### From GitHub (for Colab)

```bash
!pip install git+https://github.com/drOluOla/stintagents-evals.git
```

### Local Development

```bash
git clone https://github.com/drOluOla/stintagents-evals.git
cd stint-agents-voice
pip install -e .
```

## Usage in Google Colab

### Step 1: Install the package

```python
!pip install git+https://github.com/drOluOla/stintagents-evals.git
```

### Step 2: Import and initialize

```python
from stint_agents import (
    get_or_create_event_loop,
    create_gradio_interface,
    config
)
from stint_agents.config import CONVERSATION_SESSIONS, CURRENT_TOOL_EXPECTED

# Import your agent dependencies
from openai_agent.runner import Runner
from openai_agent.sessions import SQLiteSession

# Initialize event loop
get_or_create_event_loop()
print("✅ StintAgents Voice AI loaded!")
```

### Step 3: Set up your agents (in notebook)

```python
# Define your agents (HR Manager, IT Staff, etc.)
# This stays in the notebook as it's project-specific

from openai_agent import Agent

hr_manager = Agent(
    name="HR Manager",
    instructions="You are a friendly HR manager...",
    # ... your agent config
)

# Set up session helper
def get_or_create_session(conversation_id: str) -> SQLiteSession:
    if conversation_id not in CONVERSATION_SESSIONS:
        CONVERSATION_SESSIONS[conversation_id] = SQLiteSession(session_id=conversation_id)
    return CONVERSATION_SESSIONS[conversation_id]

# Make Runner and agent available to the package
config.Runner = Runner
config.hr_manager = hr_manager
```

### Step 4: Launch the interface

```python
# Create and launch Gradio interface
iface = create_gradio_interface()
iface.launch(share=True)
```

## Project Structure

```
stintagents-evals/
├── stintagents/
│   ├── __init__.py      # Package exports
│   ├── config.py        # Configuration and constants
│   ├── utils.py         # Audio processing, TTS, transcription
│   └── ui.py            # Gradio interface
├── tests/
│   └── test_utils.py
├── requirements.txt
├── setup.py
└── README.md
```

## Configuration

Agent voices and settings are defined in `stint_agents/config.py`:

```python
AGENT_VOICES = {
    "HR Manager": {
        "voice": "alloy",
        "speed": 1.0,
        "emoji": "👔",
        # ...
    },
    # ...
}
```

## Requirements

- Python 3.8+
- OpenAI API key (set as `OPENAI_API_KEY` environment variable)
- GPU (optional, for faster Whisper transcription)

## License

MIT License