# NLP Course — Notebook Collection

This repository is a small, educational NLP course delivered as Jupyter notebooks. Each lesson is a numbered notebook (`01_*.ipynb` → `10_*.ipynb`). Notebooks are the canonical source for code examples and exercises.

## Quick start

1. Create and activate a virtual environment (recommended Python 3.11):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start JupyterLab and open a notebook (for example `04_tokenisation.ipynb`):

```bash
jupyter lab
```

4. Open the notebook in the browser and run cells interactively. Notebooks expect CSV datasets to be present at the repo root: `bbc_news.csv` and `tripadvisor_hotel_reviews.csv`.

## Notes & gotchas

- Notebooks load datasets via relative paths (e.g., `pd.read_csv('bbc_news.csv')`). Do not hardcode absolute paths.
- Some notebooks use spaCy, Hugging Face transformers or other models. You may need to download spaCy models manually; for example:

```bash
python -m spacy download en_core_web_sm
```

- The `requirements.txt` contains many ML/NLP packages and optional GPU-enabled packages — installing on CPU-only machines is fine but may take longer.

## Contributing / editing lessons

- Follow the notebook numeric prefix when adding a new lesson (e.g., `11_new_topic.ipynb`).
- Prefer editing/adding cells in the existing `.ipynb` files rather than converting notebooks to scripts. Keep explanations and outputs inside the notebooks.
- If you add Python modules or scripts, include a short README section and a minimal example runner (e.g., `python -m mymodule`).

## Contact / feedback

If something is missing from this README (per-notebook prerequisites, special model downloads, or reproducible outputs), open an issue or ask in the repository — I'll update the docs accordingly.
