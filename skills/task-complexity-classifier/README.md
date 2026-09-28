# Task Complexity Classifier

Uses Jev (TypeSafe AI) to figure out how complex a task is. Works with any AI agent — devin, cline, kilo, codex, you name it.

## What it does

- Takes a task description
- Classifies it as routine, standard, or complex using Jev
- Returns the classification with probability scores and reasoning
- Doesn't tell you which model to use — that's your call
- Falls back to "complex" if the API is down

## Quick start

### 1. Install dependencies

```bash
# Using uv (recommended)
uv add typesafe-sdk python-dotenv

# Or using pip
pip install typesafe-sdk python-dotenv
```

### 2. Set up your API key

```bash
mkdir -p ~/.config/task-complexity-classifier
chmod 700 ~/.config/task-complexity-classifier
touch ~/.config/task-complexity-classifier/.env
chmod 600 ~/.config/task-complexity-classifier/.env
```

Add your TypeSafe API key to `.env`:
```
TYPESAFE_API_KEY=your_key_here
```

Or just set it as an environment variable:
```bash
export TYPESAFE_API_KEY=your_key_here
```

### 3. Use it

```bash
# Direct usage
python classifier.py "Fix a typo in the README"

# From a file
echo "Add input validation to the user endpoint" | python classifier.py

# Pretty output
python classifier.py "Investigate race condition in job worker" --pretty

# Dry run (no API call)
python classifier.py --dry-run "Explain how the main function works"
```

## What you get back

```json
{
  "classification": "standard",
  "probability": 0.87,
  "confidence": 0.92,
  "reasoning": "Task involves multiple components and requires domain knowledge",
  "distribution": {
    "routine": 0.05,
    "standard": 0.87,
    "complex": 0.08
  },
  "fallback_used": false
}
```

## Using it with different agents

### Devin

Pick the right model based on complexity:

```python
import json
import subprocess

task = "Add authentication to the API"
result = json.loads(subprocess.run(
    ["python", "classifier.py", task],
    capture_output=True,
    text=True
).stdout)

if result["classification"] == "complex":
    model = "claude-sonnet-4"  # Heavy-duty
elif result["classification"] == "routine":
    model = "claude-haiku-4"  # Fast
else:
    model = "claude-opus-4"  # Standard
```

### Cline

Route to the right skill:

```javascript
const classification = await classifyTask(taskDescription);

if (classification.classification === "complex") {
  await invokeSkill("specialist-review");
} else {
  await invokeSkill("general-assistant");
}
```

### Kilo

Allocate resources based on complexity:

```python
complexity = classify(task)
if complexity["classification"] == "complex":
    allocate_more_resources()
    set_longer_timeout()
```

### Codex

Map to your model tiers:

```python
MODEL_MAP = {
    "routine": "gpt-5.6-luna",
    "standard": "gpt-5.6-terra",
    "complex": "gpt-6-astra"
}

result = classify(task)
model = MODEL_MAP.get(result["classification"], "gpt-6-astra")
```

## Configuration

### Custom complexity classes

Edit `~/.config/task-complexity-classifier/config.json`:

```json
{
  "classes": {
    "trivial": "One-line fixes, typos, formatting",
    "routine": "Simple changes with clear steps",
    "standard": "Moderate complexity",
    "complex": "Requires deep reasoning"
  },
  "thresholds": {
    "min_probability": 0.75,
    "fallback_class": "standard"
  }
}
```

### Thresholds

- `min_probability`: Minimum confidence to accept the classification (default: 0.8)
- `fallback_class`: What to return when uncertain (default: "complex")

## Fallback behavior

The classifier never blocks. If anything goes wrong — no API key, API down, bad response, low confidence — it returns a safe fallback:

```json
{
  "classification": "complex",
  "probability": 0.0,
  "confidence": 0.0,
  "reasoning": "API unavailable - using safe fallback",
  "distribution": {"routine": 0.0, "standard": 0.0, "complex": 1.0},
  "fallback_used": true
}
```

Check `fallback_used` to know if the classification is real or a fallback.

## Testing

Run tests (no API key needed):

```bash
python -m unittest discover -s tests -v
```

Test with the live API (requires a key):

```bash
python classifier.py "Explain a small function"
```

## Why this is agnostic

The original Codex Router had two parts:
1. Jev classification — this part is agnostic
2. Codex-specific routing — this part is not

This skill keeps only the agnostic part. It outputs classification data and lets each agent decide what to do with it — which models to use, how to route tasks, what "complex" means in their context.

## Dependencies

- Python 3.8+
- `typesafe-sdk` — Jev API client
- `python-dotenv` — Config file support

## License

MIT
