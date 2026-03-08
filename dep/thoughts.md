---
layout: default
title: Thoughts
---

# Thoughts

A pseudo-blog for me to write what I am thinking about:

### 6/16/2025

It seems imperative that I take more action towards documenting my work. 
First, for tasks like mentoring undergraduate students or sharing code within the lab, having a consistant style and location for my files is necessary.
Second, having everything in a common place will allow me to much more effectively initialize, simulate, and analyze my code.
Third, creating this format, for me, will allow me to translate my code from production code to publication quality code
Four, this format will greatly improve my ability to recall what I have done.
Five, there is a lot I haven't learned, primarily with git and optimizing my use of VSCode, that I would like to
Six, I have a lot of odd ideas and things that I do or show or think about that I don't know where to put. Here can be the place.

I wonder if I could use frequent git pushes and documentation to this site to replace my lab notebook. The reason I hesitate is because my current production file structure is not sufficiently neat to support this. Git will never be a repository for my data (too large) and my simulations often rely on reading/writing from local data from multiple clusters.

Goals:
- Document onboarding for new student (using resources from statt lab wiki)
- Document all analysis methods written
- Copy analysis methods to a single git repository that I WILL update frequently. All analysis methods can/should be treated as an Analysis object. 
  - MembraneAnalysis inherits Analysis
  - LocalMembraneAnalysis inherits Analysis
  - DynamicMembraneAnalysis inherits Analysis
  - DynamicAnalysis inherits Analysis
  - MeshMembraneAnalysis inherits Analysis
  - All analysis methods will save data to .h5 files with the exception of Local Analysis, which will save analysis to a .gsd.
- Document all methods of initializing and simulating simulations (including frozen patches, ghost particles, random, mixed, etc.)