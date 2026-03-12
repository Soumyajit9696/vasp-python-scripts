⚛️ VASP Post-Processing Toolkit (Python)
<p align="center"> <img src="https://img.shields.io/badge/Python-3.9+-blue.svg"> <img src="https://img.shields.io/badge/VASP-PostProcessing-green"> <img src="https://img.shields.io/badge/DFT-Materials%20Science-orange"> <img src="https://img.shields.io/badge/License-MIT-red"> </p> <p align="center"> Python scripts for analyzing and visualizing <b>VASP outputs</b> including <b>band structures, density of states, projected bands, optical properties</b> and more. </p>
📌 Overview

This repository contains a collection of Python scripts for post-processing VASP calculations.
It is designed for DFT researchers working on electronic structure calculations, especially in:

Condensed Matter Physics

Materials Science

2D Materials (TMDCs, graphene, etc.)

Semiconductor physics

The scripts automate the extraction and visualization of physical quantities from VASP output files.

🚀 Features

✨ Current and planned capabilities:

📈 Band Structure plotting

🎨 Orbital-projected band structures

📊 Density of States (DOS) plotting

🧲 Spin-resolved electronic structure

💡 Optical properties analysis

🔍 Projected density of states (PDOS)

📂 Automated parsing of:

EIGENVAL

PROCAR

DOSCAR

OUTCAR

vasprun.xml


<img width="1100" height="600" alt="plot" src="https://github.com/user-attachments/assets/4716ad3c-bc65-4061-9e69-11538bd6dc52" />




---
Install required Python packages:

<code> pip install numpy matplotlib scipy pymatgen </code>

▶️ Example Usage
<code>
#Plot Band Structure
python band_dos_plot.py
</code>
Example output:

Publication-quality band structure plots

Customizable Fermi level alignment

High symmetry k-points

📊 Example Output

Typical outputs include:

Electronic band structures

Orbital-projected bands

DOS and PDOS plots

Optical conductivity spectra

All plots are generated using Matplotlib and can be directly used in research papers or theses.

🎯 Future Development

Planned additions:

Wannier90 interface

Automatic high-symmetry k-path generation

Effective mass calculation

Band unfolding

Interactive plots (Plotly)

🐍 Clean Python + Matplotlib visualizations
