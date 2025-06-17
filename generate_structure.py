import os

# Root folder where everything goes (change if needed)
ROOT = "learning"

# Define the structure: folder or file name and whether it's a folder with index or a flat file
structure = {
    "hoomd-installation.html": None,
    "md-nutshell.html": None,
    "ovito-visualization.html": None,
    "gaussian-chain": ["index.html", "initializing.html", "simulating.html", "analyzing.html", "theory-validation.html"],
    "martini-intro.html": None,
    "lipid-bilayer": ["index.html", "init.html", "minimize.html", "simulate.html", "analyze.html"],
    "cluster-usage.html": None,
    "rigid-bodies.html": None,
    "analysis": ["index.html", "dynamics.html", "membrane.html", "local.html", "mesh.html", "rdf-sf.html"],
    "figures.html": None,
    "curved-membranes": ["index.html", "anchored.html", "floating.html", "shape-extraction.html"],
    "tpms": ["index.html", "construction.html", "ghost.html", "init-near.html", "integration.html"],
    "sequence-macros": ["index.html", "initialization.html", "polymer-building.html", "random-walks.html", "workflows.html"],
    "misc": ["index.html", "image-to-sim.html", "sim-to-3d.html"],
}

# HTML boilerplate
def boilerplate(title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="/assets/style.css">
</head>
<body>
    <header>
        <h1><a href="/">My Site</a></h1>
        <nav>
            <a href="/projects">Projects</a>
            <a href="/thoughts">Thoughts</a>
        </nav>
    </header>
    <main>
        <h1>{title}</h1>
        <p>Content coming soon.</p>
    </main>
    <footer>
        <p>© 2025 James Tallman</p>
    </footer>
</body>
</html>
"""

# Make root dir if needed
os.makedirs(ROOT, exist_ok=True)

for key, value in structure.items():
    if value is None:
        # It's a single HTML file
        path = os.path.join(ROOT, key)
        with open(path, "w") as f:
            title = os.path.splitext(os.path.basename(key))[0].replace("-", " ").title()
            f.write(boilerplate(title))
    else:
        # It's a folder with files
        folder_path = os.path.join(ROOT, key)
        os.makedirs(folder_path, exist_ok=True)
        for file in value:
            path = os.path.join(folder_path, file)
            title = os.path.splitext(file)[0].replace("-", " ").title()
            with open(path, "w") as f:
                f.write(boilerplate(title))

print(f"✅ Generated all files inside ./{ROOT}/")
