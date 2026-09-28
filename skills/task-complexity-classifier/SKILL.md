---
name: task-complexity-classifier
type: atomic
license: MIT
description: >
  Classify task complexity using Jev (TypeSafe AI) to help any AI agent decide
  how to handle a task. Returns complexity data without telling you which model
  to use — that's your call. Trigger words: classify complexity, task complexity,
  complexity assessment, how complex is this task.
metadata:
  version: 1.0.0
  user-invocable: "true"
  output: JSON with complexity class, probability, confidence, and reasoning
  constraints: "Requires TYPESAFE_API_KEY; fails gracefully to 'complex' without it."
---

# Task Complexity Classifier

Uses Jev (TypeSafe AI) to figure out how complex a task is, then hands off that judgment to whatever agent you're using. It doesn't pick models or run commands — it just tells you "this is probably complex" and lets you decide what to do with that info.

## What it does (and doesn't do)

**Does:**
- Take a task description and classify it as routine, standard, or complex
- Return the classification with probability scores and a brief explanation
- Fail gracefully if the API is down or you don't have a key set up
- Work with any AI agent — devin, cline, kilo, codex, whatever

**Doesn't:**
- Pick which model to use
- Execute the task
- Call agent-specific tools
- Block your work if something goes wrong

## How it works

1. You give it a task description (text or from a file)
2. It asks Jev to classify the complexity
3. You get back JSON with the classification, probability, confidence, and reasoning
4. If anything breaks, it falls back to "complex" as a safe default

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

The fields:
- `classification`: routine, standard, or complex (you can customize these)
- `probability`: how confident Jev is about this classification
- `confidence`: Jev's internal confidence score
- `reasoning`: why it picked this classification
- `distribution`: the full breakdown across all classes
- `fallback_used`: true if something went wrong and it used the safe default

## Setting it up

### API key

You'll need a TypeSafe API key. Set it as an environment variable:

```bash
export TYPESAFE_API_KEY=your_key_here
```

Or put it in a config file:

```bash
mkdir -p ~/.config/task-complexity-classifier
chmod 700 ~/.config/task-complexity-classifier
touch ~/.config/task-complexity-classifier/.env
chmod 600 ~/.config/task-complexity-classifier/.env
# Then add: TYPESAFE_API_KEY=your_key_here
```

### Complexity classes

By default it uses three classes:
- **routine**: Simple stuff with clear steps
- **standard**: Moderate complexity, needs some domain knowledge
- **complex**: Hard stuff requiring deep reasoning or multiple domains

You can customize these in `config.json` if you want different classes.

### Thresholds

- `min_probability`: 0.8 (if confidence is below this, use the safe default)
- `fallback_class`: "complex" (what to return when uncertain)

## Using it

### From the command line

```bash
# Direct usage
python skills/task-complexity-classifier/classifier.py "Fix a typo in the README"

# From a file
python skills/task-complexity-classifier/classifier.py < task.txt

# With custom config
python skills/task-complexity-classifier/classifier.py --config /path/to/config.json "Add input validation"

# Dry run (no API call)
python skills/task-complexity-classifier/classifier.py --dry-run "Explain how the main function works"
```

### From an agent skill

Your agent's skill system calls this, gets JSON back, and does whatever makes sense for your setup:

```python
classification = json.loads(skill_output)
if classification["classification"] == "complex":
    # Use your heavy-duty model
    use_high_reasoning_model()
elif classification["classification"] == "routine":
    # Quick and dirty is fine here
    use_fast_model()
else:
    # Standard case
    use_standard_model()
```

## Optional work-router integration

If you want `work-router` to consider complexity before routing, just include something like "Classify complexity before routing" in your request. Work-router will:
1. Call this skill
2. Use the result to pick a more appropriate skill (complex stuff might go to specialists)
3. Fall back to normal routing if classification isn't available

## Agent-specific examples

**Devin**: Use the classification to pick between fast/standard/reasoning models based on task complexity
**Cline**: Route complex tasks to specialist skills, routine stuff to generalists
**Kilo**: Allocate more resources to complex tasks
**Codex**: Map the classes to your model tiers (luna/terra/astra or whatever you use)

## When things go wrong

If the API is down, you don't have a key, or anything else breaks, you get a safe fallback:

```json
{
  "classification": "complex",
  "probability": 0.0,
  "confidence": 0.0,
  "reasoning": "API unavailable - using safe fallback",
  "distribution": {
    "routine": 0.0,
    "standard": 0.0,
    "complex": 1.0
  },
  "fallback_used": true
}
```

The key thing: your agent always gets a valid response and can keep working. Check `fallback_used` to know if the classification is real or a fallback.

## Testing

Run the tests:

```bash
python -m unittest discover -s skills/task-complexity-classifier/tests -v
```

The tests cover class mapping, thresholds, error handling, key management, and output format. They don't need a live API key — the important tests use mocks.

## Dependencies

- Python 3.8+
- `typesafe-sdk` (the Jev client)
- `python-dotenv` (for config files)

Install them:

```bash
uv add typesafe-sdk python-dotenv
# or
pip install typesafe-sdk python-dotenv
```

## Things to avoid

- Don't use classification to block work — it's advisory, not a gate
- Don't hardcode model mappings in the skill itself — let each agent decide
- Don't make classification mandatory for routing — it should be optional
- Don't ignore the `fallback_used` flag — it tells you if the classification is trustworthy
- Don't use this for security or authorization decisions — it's not designed for that
