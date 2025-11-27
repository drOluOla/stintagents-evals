# StintAgents Evals & Safety

Build multi-agent voice AI systems with distinct personas for realistic workplace scenarios.
Evaluate their performance against expected behaviours and test them for safety, all within a Colab or Jupyter notebook.

As AI reshapes the labour market and as future-of-work trends indicate that AI will augment human capabilities through collaboration, a critical question emerges. How do we prepare people for AI-augmented workplaces while ensuring that these systems remain safe, aligned and trustworthy?

![alt text](assets/stintagents-demo-ui.png)

StintAgents Eval is an very early stage and evolving toolkit that provides everything you need to:
- Create multi-agent voice AI simulations with realistic workplace scenarios
- Evaluate agent performance using Inspect AI’s powerful evaluation framework
- Test for safety vulnerabilities, including prompt injection attacks
- Verify alignment with human values and organisational integrity
- Track conversations through persistent session memory management

Built on OpenAI's Agents SDK and inspired by AISI's open-source safety framework, StintAgents Eval brings enterprise-grade agent development to a Colab notebook. Whether you're researching AI safety, developing workforce training programs, or exploring multi-agent collaboration, this toolkit gives you a foundation to build—and critically evaluate—AI systems that real people will depend on.

*This isn't just another chatbot demo. It's a step toward solving one of the most pressing challenges of our time: preparing humans and AI to work together safely*.

## Usage in Google Colab

### Install the package

```python
!pip install git+https://github.com/drOluOla/stintagents-evals.git
```

> [!NOTE]
> The following sections demonstrate key features of StintAgents Evals. As the tool is in early development, some bugs may be present. For a working demo, see the [minimal example](https://github.com/drOluOla/stintagents-evals/blob/main/StintAgents_Evals_Safety.ipynb) in the StintAgents-Evals repository or access the [shared notebook on Google Colab](https://drive.google.com/file/d/1SqoNdOOFb2KNDSx6ZT3a8zgMSD9dMYvr/view?usp=sharing).

### Customise Agent Personas

```python
# Define personas (Optional)
set_agent_personas({
    "HR Manager": { "voice": "alloy", "description": "Professional & Welcoming" }
})

# Define Tools
@function_tool
def get_welcome_info() -> str:
    """Welcome the new employee."""
    msg = "Welcome to the team!"
    CURRENT_TOOL_EXPECTED["expected"] = msg
    return msg

# Define Agents
hr_manager = Agent(
    name="People Ops",
    instructions="You are a helpful HR Manager.",
    model="gpt-4o-mini",
    tools=[get_welcome_info]
)
```

### Evaluation Performance
Use `inspect_ai` to evaluate agent performance based on conversation history.

```python
from inspect_ai import eval, task
from inspect_ai.scorer import scorer, mean, match
# ... (Import other necessary components as shown in notebook)

@task
def evaluate_response_quality():
    conversation_ids = list(CONVERSATION_SESSIONS.keys())
    return Task(
        dataset=create_dataset_from_conversations(conversation_ids),
        solver=hr_agent_solver(),
        scorer=factual_correctness_scorer()
    )

# Run Evaluation
results = eval(
    [evaluate_response_quality()],
    model="openai/gpt-4o-mini",
    log_dir="./eval_logs"
)
```

### Safety Checks

Evaluate robustness against prompt injection.

![alt text](assets/stintagent_inpect_ai.png)

## Project Structure

```
stintagents-evals/
├── stintagents/
│   ├── __init__.py      
│   ├── config.py        
│   ├── utils.py         
│   └── ui.py            
├── requirements.txt
├── setup.py
└── README.md
```



## Known Issues/To Dos:
- [ ] Enhance generation accuracy by integrating advanced retrieval techniques
- [ ] Implement robust guardrails for content moderation and safety.
- [ ] Reduce latency in the voice AI pipeline with better TTS & STT models/logic.
- [ ] See some in https://github.com/users/drOluOla/projects/3
