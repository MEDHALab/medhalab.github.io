"""Export the Flask site to static HTML in ./docs for GitHub Pages."""
from pathlib import Path
from flask_frozen import Freezer
from app import app

app.config["FREEZER_RELATIVE_URLS"] = True   # works under /MEDHA-lab/ or at the root
app.config["FREEZER_DESTINATION"] = "docs"

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
    Path("docs/.nojekyll").touch()           # tell GitHub Pages not to run Jekyll
    print("Done. Static site written to ./docs")
