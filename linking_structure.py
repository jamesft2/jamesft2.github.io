import re
from bs4 import BeautifulSoup

# Mapping from list item text to file path
link_map = {
    "Installing HOOMD-Blue": "/learning/hoomd-installation.html",
    "Molecular Dynamics in a Nutshell": "/learning/md-nutshell.html",
    "What is MD?": "/learning/md-nutshell.html#what-is-md",
    "Particles and Interactions": "/learning/md-nutshell.html#particles",
    "Periodic Boundaries": "/learning/md-nutshell.html#boundaries",
    "Units": "/learning/md-nutshell.html#units",
    "Ensembles (Thermostats and Barostats)": "/learning/md-nutshell.html#ensembles",
    "Visualizing MD: Ovito": "/learning/ovito-visualization.html",
    "Pythonic OVITO": "/learning/ovito-visualization.html#pythonic",
    "Simulation to 3D Printable Object": "/learning/ovito-visualization.html#3dprint",
    "Hello World of MD Simulation: Gaussian Chain": "/learning/gaussian-chain/",
    "Initializing the Chain": "/learning/gaussian-chain/initializing.html",
    "Simulating the Chain": "/learning/gaussian-chain/simulating.html",
    "Analyzing the Chain": "/learning/gaussian-chain/analyzing.html",
    "Equilibration Time": "/learning/gaussian-chain/theory-validation.html#equilibration",
    "Radius of Gyration": "/learning/gaussian-chain/theory-validation.html#gyration",
    "End-to-End Distance": "/learning/gaussian-chain/theory-validation.html#end-to-end",
    "Validating Simulations with Theory": "/learning/gaussian-chain/theory-validation.html#validation",
    "Analysis Repository:": "/learning/analysis/",
    # Add more here as needed...
}

# Load your HTML (replace with the actual file path if needed)
with open("learning.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find the <section class="pyscript"> and walk its <li> elements
for li in soup.select("section.pyscript li"):
    text = li.get_text(strip=True)
    if text in link_map:
        href = link_map[text]
        # Replace content with a link
        li.string = ""
        link = soup.new_tag("a", href=href)
        link.string = text
        li.append(link)

# Output to a new file
with open("learning-linked.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("✅ learning-linked.html written with links added.")

