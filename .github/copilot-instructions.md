## Purpose

Short, actionable guidance for AI coding assistants working on this repository (an educational NLP notebook collection).

## Big-picture / architecture

- This repo is a sequence of Jupyter notebooks (01_* through 10_*) that form a small NLP course. Notebooks are the primary source of code and exercises. The repo also includes two CSV datasets at the repo root: `bbc_news.csv` and `tripadvisor_hotel_reviews.csv`.
- There is no multi-module service; the project is a learning workspace. Most code lives inside notebooks; `main.py` is a placeholder script (auto-generated sample).

## Key files and where to look

- Notebooks: `01_lowercase.ipynb` ... `10_tagging_practical.ipynb` — open these in JupyterLab to edit or run cells.
- Datasets at repo root: `bbc_news.csv`, `tripadvisor_hotel_reviews.csv` — notebooks load these directly via relative paths.
- Environment: `requirements.txt` — use this to recreate the Python environment (includes `jupyterlab`, `spacy`, `transformers`, `gensim`, `nltk`, etc.).
- Minimal script: `main.py` — not used by course content; safe to ignore unless adding CLI utilities.

## Developer workflows (explicit)

- Setup environment (recommended):

  1. Create a virtual environment with Python 3.11 (or close): `python -m venv .venv && source .venv/bin/activate`
  2. Install dependencies: `pip install -r requirements.txt` (this installs JupyterLab and NLP libs used in the notebooks).
  3. Start the notebooks: `jupyter lab` and open the specific notebook, e.g. `04_tokenisation.ipynb`.

- Run a notebook cell interactively in Jupyter rather than executing notebooks by running Python files; notebooks are canonical.

## Project-specific conventions & patterns

- Notebook numbering conveys lesson order. When adding material, follow the numeric prefix (e.g., create `11_...` if a new lesson follows).
- Data loading is done with relative paths in notebooks (e.g., `pd.read_csv('bbc_news.csv')`); do not hardcode absolute paths.
- Use `spacy`, `nltk`, `transformers`, and `gensim` APIs in notebooks — examples spread across the tagging and NER notebooks.

## Integration points & external dependencies

- The repo relies on external model/data packages (Hugging Face Transformers, spaCy models). Installing `requirements.txt` is required to run model code; some notebooks may expect additional spaCy models (e.g., `python -m spacy download en_core_web_sm`) — check the notebook that uses spaCy for explicit model names.

## What an AI assistant should do (concise list)

1. Prefer editing or adding notebook cells (`.ipynb`) rather than converting to scripts. Keep explanations and outputs contained in the notebook.
2. When adding new dependencies, update `requirements.txt` and keep entries pinned (follow existing file style).
3. For data operations reference the repo-root CSVs and keep transformations reproducible inside notebooks.
4. If you modify or add Python modules (rare), include a small README section and an example runner (e.g., `python -m mymodule` or `python main.py`).

## Examples from the repo (how to reference)

- To update the tokenisation lesson, open `04_tokenisation.ipynb` and add/modify cells. Use `pandas.read_csv('bbc_news.csv')` to load sample data.
- To add a new lesson after NER, create `11_your_topic.ipynb` and follow the same top-matter structure as existing notebooks.

## Quick notes / gotchas

- There are no CI workflows or tests; keep changes minimal and notebook-focused. If you add scripts or automation, include simple run instructions in the repo root README (or a new `scripts/README.md`).
- Notebooks may assume an environment with GPU-supporting packages listed in `requirements.txt`; these are optional for CPU runs but can increase install time.

---

If anything is missing or you'd like the instructions to emphasize different workflows (e.g., automated notebook execution, CI, or packaging exercises), tell me which parts to expand or examples to add.
