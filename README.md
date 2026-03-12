⚛️ VASP Post-Processing Toolkit (Python)
<p align="center"> <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python"> <img src="https://img.shields.io/badge/VASP-PostProcessing-green?style=for-the-badge"> <img src="https://img.shields.io/badge/DFT-Materials%20Science-orange?style=for-the-badge"> <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge"> </p> <p align="center"> <b>Python toolkit for analyzing and visualizing VASP outputs</b><br> Band structures • Density of states • Orbital projections • Optical properties </p>
📌 Overview

This repository provides a collection of Python scripts for post-processing VASP calculations, designed for researchers working in computational materials science and electronic structure theory.

The toolkit helps automate the extraction, processing, and visualization of physical quantities from VASP output files, making it easier to generate publication-quality plots.

🔬 Target Research Areas

🧲 Condensed Matter Physics

🧪 Materials Science

🧬 2D Materials (TMDCs, Graphene, etc.)

💻 Semiconductor Physics

⚛️ Density Functional Theory (DFT)

🚀 Features
Current & Planned Capabilities
Feature	Description
📈 Band Structure Plotting	High-quality electronic band diagrams
🎨 Orbital-Projected Bands	Element and orbital contributions
📊 Density of States (DOS)	Total DOS visualization
🔍 Projected DOS (PDOS)	Orbital and atom resolved DOS
🧲 Spin-Resolved Bands	Spin-polarized calculations
💡 Optical Properties	Dielectric function & optical spectra
📂 Supported VASP Files

The scripts automatically parse important VASP output files:

EIGENVAL
PROCAR
DOSCAR
OUTCAR
vasprun.xml

These files are processed to extract electronic structure information.

📊 Example Output
<p align="center"> <img src="https://github.com/user-attachments/assets/4716ad3c-bc65-4061-9e69-11538bd6dc52" width="900"> </p>

Typical outputs include:

📈 Electronic band structures

🎨 Orbital-projected band structures

📊 Density of States (DOS / PDOS)

💡 Optical conductivity spectra

All figures are generated using Matplotlib and are suitable for thesis or research publications.

⚙️ Installation

Install the required Python dependencies:

pip install numpy matplotlib scipy pymatgen
▶️ Example Usage
Plot Band Structure
python band_dos_plot.py
Output

The script will generate:

Publication-quality band structure plots

Fermi-level aligned bands

High-symmetry k-point labels

🎯 Future Development

Upcoming features planned for the toolkit:

🔗 Wannier90 integration

📍 Automatic high-symmetry k-path generation

⚡ Effective mass calculation

🔄 Band unfolding

📊 Interactive plots with Plotly

🐍 Visualization

All plots are generated using:

Python

Matplotlib

NumPy

The goal is to provide clean, customizable, and reproducible visualizations for DFT research.

⭐ If you find this repository useful, consider starring it!
