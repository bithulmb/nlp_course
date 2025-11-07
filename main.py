"""NLP Course — informational script.

This small script is a convenience entrypoint that prints a short description
of the repository and how to run the notebooks. The canonical content lives
inside the Jupyter notebooks (`01_*.ipynb` .. `10_*.ipynb`).
"""

def print_project_info():
    """Print a short description and quick-start commands for the course."""
    print("NLP Course — collection of Jupyter notebooks (01_*.ipynb → 10_*.ipynb).")
    print("Datasets at repo root: bbc_news.csv, tripadvisor_hotel_reviews.csv")
    print("")
    print("Quick start:")
    print("  python -m venv .venv && source .venv/bin/activate")
    print("  pip install -r requirements.txt")
    print("  jupyter lab")


if __name__ == '__main__':
    print_project_info()
