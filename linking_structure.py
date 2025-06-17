import re
from bs4 import BeautifulSoup

# Mapping from list item text to file path
# Full link_map for the original outline
link_map = {
    # Intro topics
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

    # Gaussian Chain Simulation
    "Hello World of MD Simulation: Gaussian Chain": "/learning/gaussian-chain/",
    "Initializing the Chain": "/learning/gaussian-chain/initializing.html",
    "Simulating the Chain": "/learning/gaussian-chain/simulating.html",
    "Analyzing the Chain": "/learning/gaussian-chain/analyzing.html",
    "Equilibration Time": "/learning/gaussian-chain/theory-validation.html#equilibration",
    "Radius of Gyration": "/learning/gaussian-chain/theory-validation.html#gyration",
    "End-to-End Distance": "/learning/gaussian-chain/theory-validation.html#end-to-end",
    "Validating Simulations with Theory": "/learning/gaussian-chain/theory-validation.html#validation",

    # Martini and Bilayer
    "(My) Introduction to Martini 3": "/learning/martini-intro.html",
    "Hello World of Martini Simulations: Lipid Bilayer": "/learning/lipid-bilayer/",
    "Initializing the Membrane": "/learning/lipid-bilayer/initializing.html",
    "FIRE Energy Minimization": "/learning/lipid-bilayer/fire.html",
    "Simulating the Membrane": "/learning/lipid-bilayer/simulating.html",
    "Analyzing the Membrane": "/learning/lipid-bilayer/analyzing.html",
    "Thickness": "/learning/lipid-bilayer/thickness.html",
    "Area per Lipid": "/learning/lipid-bilayer/apl.html",
    "Order Parameter": "/learning/lipid-bilayer/order.html",

    # Misc simulation tools
    "Using the Cluster": "/learning/cluster-usage.html",
    "Rigid Bodies: Cholesterol": "/learning/rigid-bodies.html",

    # Analysis repository
    "Analysis Repository:": "/learning/analysis/",
    "Dynamic quanties:": "/learning/analysis/dynamics/",
    "Mean Squared Displacement": "/learning/analysis/dynamics/msd.html",
    "Velocity Autocorrelation Function": "/learning/analysis/dynamics/vacf.html",
    "Van Hove Correlation Functions": "/learning/analysis/dynamics/vanhove.html",
    "Membrane Quantities": "/learning/analysis/membrane/",
    "The pressure profile": "/learning/analysis/membrane/pressure.html",
    "Stretching Modulus": "/learning/analysis/membrane/stretching.html",
    "From Pressure Profile": "/learning/analysis/membrane/stretching-from-pressure.html",
    "From Box Fluctuations": "/learning/analysis/membrane/stretching-from-box.html",
    "From Simulated Micropipette Aspiration": "/learning/analysis/membrane/stretching-mpa.html",
    "Bending Modulus": "/learning/analysis/membrane/bending.html",
    "From Splay-Tilt Method": "/learning/analysis/membrane/splay-tilt.html",
    "From fluctuation Analysis": "/learning/analysis/membrane/fluctuation.html",
    "Local Quantities": "/learning/analysis/local/",
    "Local Area per Lipid": "/learning/analysis/local/apl.html",
    "Local Density/Composition": "/learning/analysis/local/density.html",
    "Local Thickness": "/learning/analysis/local/thickness.html",
    "Local Nematic Order": "/learning/analysis/local/nematic.html",
    "Local Surface Area": "/learning/analysis/local/surface-area.html",
    "Binned MSD": "/learning/analysis/local/binned-msd.html",
    "Steinhart Order Parameter": "/learning/analysis/local/steinhart.html",
    "Mesh Based Quantities": "/learning/analysis/mesh/",
    "Constructing the Mesh": "/learning/analysis/mesh/construction.html",
    "Euler Characteristic": "/learning/analysis/mesh/euler.html",
    "Geodesic Distances": "/learning/analysis/mesh/geodesic.html",
    "Local Mean Curvature": "/learning/analysis/mesh/mean-curvature.html",
    "Local Gaussian Curvature": "/learning/analysis/mesh/gaussian-curvature.html",
    "Euler Characteristic from Local Quantities": "/learning/analysis/mesh/euler-from-local.html",
    "Radial Distribution Function and Structure Factor": "/learning/analysis/rdf-structure-factor.html",

    # Figures
    "Plotting Publication Quality Figures": "/learning/figures.html",

    # Curved membranes
    "Simulating Curved Membranes": "/learning/curved-membranes/",
    "Frozen Anchored Patches": "/learning/curved-membranes/anchored.html",
    "Frozen Floating Patches": "/learning/curved-membranes/floating.html",
    "Extracting shape with line": "/learning/curved-membranes/extract-line.html",

    # TPMS
    "Triply Periodic Minimal Surfaces": "/learning/tpms/",
    "Constructing the surface (math and cool links)": "/learning/tpms/construction.html",
    "Facets and Supercells": "/learning/tpms/facets.html",
    "Simulating via ghost particles": "/learning/tpms/ghost.html",
    "Simulating via initalizing near determined structure": "/learning/tpms/near-structure.html",
    "Computing Energies with Thermodynamic Integration": "/learning/tpms/ti.html",

    # Sequence-defined macromolecules
    "Sequence defined macromolecules": "/learning/sequence-macros/",
    "Initializing Sequence Defined Macromolecules": "/learning/sequence-macros/initializing.html",
    "A better way of 'building' polymers (than my Martini implementation)": "/learning/sequence-macros/better-building.html",
    "Random walks and hilbert curves": "/learning/sequence-macros/random-walks.html",
    "Example workflows": "/learning/sequence-macros/workflows.html",

    # Misc
    "Misc Other": "/learning/misc/",
    "Turning images/3D objects into simulations": "/learning/misc/image-to-sim.html",
    "Turning simulations to 3D objects": "/learning/misc/sim-to-3d.html",
}


# Load your HTML (replace with the actual file path if needed)
with open("projects.html", "r", encoding="utf-8") as f:
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

