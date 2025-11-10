# SmartName 

**SmartName** is a compact CLI tool to analyze mixed-media files with Ollama and generate
context-aware file name suggestions.

---

## Requirements

Install dependencies:

```bash
pip install requests python-docx python-pptx PyMuPDF
```

Install **Ollama** (https://ollama.ai) and pull a model with vision capabilities:

```bash
ollama pull llama3.2-vision
```

---

## Usage

Run the tool on a folder:

```bash
python smartname.py data/
```

### Options

| Flag | Description | Default |
|------|--------------|----------|
| `--model` | Ollama model name | `llama3.2-vision` |
| `--case` | Casing style (`snake_case`, `kebab-case`, `camelCase`, `PascalCase`, `lowercase`, `Title Case`) | `snake_case` |
| `--execute` | Actually rename files (otherwise dry-run) | False |

### Example

```bash
python smartname data/ --case "Title Case" --model llama3.2-vision
```

Dry-run output example:

```
Scanning: data/

Processing IMG_0023.jpg...
Suggestion: conference_poster_photo.jpg

Processing notes.pdf...
Suggestion: research_notes_october_2025.pdf
```

Execute the rename for real:

```bash
python smartname.py data/ --execute
```

---

## Tip

Start simple: create a small test folder like `data/` with a few files (`.jpg`, `.pdf`, `.md`) and test the dry-run mode first.
