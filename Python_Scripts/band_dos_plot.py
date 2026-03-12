import numpy as np
import matplotlib.pyplot as plt

EIGENVAL = "EIGENVAL"
DOSCAR = "DOSCAR"
OUTCAR = "OUTCAR"
KPOINTS = "KPOINTS"

E_MIN = -5
E_MAX = 5


# ------------------------------------------------
# FERMI ENERGY
# ------------------------------------------------
def read_fermi():

    with open(OUTCAR) as f:
        for line in f:
            if "E-fermi" in line:
                return float(line.split()[2])

    raise RuntimeError("Fermi level not found")


# ------------------------------------------------
# READ EIGENVAL
# ------------------------------------------------
def read_eigenval():

    with open(EIGENVAL) as f:
        lines = f.readlines()

    header = lines[5].split()

    nk = int(header[1])
    nb = int(header[2])

    kpoints = []
    bands = np.zeros((nk, nb))

    idx = 7

    for i in range(nk):

        k = list(map(float, lines[idx].split()[:3]))
        kpoints.append(k)

        idx += 1

        for j in range(nb):

            bands[i, j] = float(lines[idx].split()[1])
            idx += 1

        idx += 1

    return np.array(kpoints), bands


# ------------------------------------------------
# READ DOS
# ------------------------------------------------
def read_dos():

    with open(DOSCAR) as f:
        lines = f.readlines()

    header = lines[5].split()

    nedos = int(header[2])
    efermi = float(header[3])

    energy = []
    total = []

    for i in range(6, 6 + nedos):

        parts = lines[i].split()

        energy.append(float(parts[0]))
        total.append(float(parts[1]))

    energy = np.array(energy) - efermi
    total = np.array(total)

    return energy, total, nedos


# ------------------------------------------------
# READ PDOS
# ------------------------------------------------
def read_pdos(nedos):

    with open(DOSCAR) as f:
        lines = f.readlines()

    start = 6 + nedos

    zr_d = np.zeros(nedos)
    se_p = np.zeros(nedos)

    line = start
    atom = 0

    while line < len(lines):

        atom += 1
        line += 1

        for i in range(nedos):

            parts = lines[line].split()

            py = float(parts[2])
            pz = float(parts[3])
            px = float(parts[4])

            dxy = float(parts[5])
            dyz = float(parts[6])
            dz2 = float(parts[7])
            dxz = float(parts[8])
            dx2 = float(parts[9])

            if atom <= 2:
                zr_d[i] += dxy + dyz + dz2 + dxz + dx2
            else:
                se_p[i] += px + py + pz

            line += 1

    return zr_d, se_p


# ------------------------------------------------
# BAND GAP
# ------------------------------------------------
def calculate_bandgap(bands):

    vbm = -1e9
    cbm = 1e9

    for band in bands.T:

        below = band[band <= 0]
        above = band[band > 0]

        if len(below):
            vbm = max(vbm, below.max())

        if len(above):
            cbm = min(cbm, above.min())

    gap = cbm - vbm

    return vbm, cbm, gap


# ------------------------------------------------
# READ KPOINT LABELS
# ------------------------------------------------
def read_kpath_labels():

    labels = []

    with open(KPOINTS) as f:
        lines = f.readlines()

    for line in lines:

        if "!" in line:

            label = line.split("!")[1].strip().upper()

            if label in ["GAMMA", "G"]:
                label = r"$\Gamma$"

            labels.append(label)

    return labels


# ------------------------------------------------
# MAIN
# ------------------------------------------------

print("Reading Fermi level...")
fermi = read_fermi()

print("Reading band structure...")
kpoints, bands = read_eigenval()

bands -= fermi

print("Reading DOS...")
dos_energy, total_dos, nedos = read_dos()

print("Reading PDOS...")
zr_dos, se_pdos = read_pdos(nedos)


# ------------------------------------------------
# KPATH DISTANCE
# ------------------------------------------------

kdist = np.zeros(len(kpoints))

for i in range(1, len(kpoints)):
    kdist[i] = kdist[i-1] + np.linalg.norm(kpoints[i] - kpoints[i-1])


# ------------------------------------------------
# HIGH SYMMETRY DETECTION
# ------------------------------------------------

kpath_labels = read_kpath_labels()

# fallback if no labels
if len(kpath_labels) == 0:

    print("No symmetry labels found → assuming Γ-M-K-Γ")

    kpath_labels = [r"$\Gamma$", "M", "K", r"$\Gamma$"]


nseg = len(kpath_labels) - 1

points_per_segment = int(len(kpoints) / nseg)

ticks = []
tick_labels = []

for i in range(nseg + 1):

    idx = i * points_per_segment

    if idx >= len(kdist):
        idx = len(kdist) - 1

    ticks.append(kdist[idx])
    tick_labels.append(kpath_labels[i])


print("High symmetry points:", tick_labels)


# ------------------------------------------------
# BAND GAP
# ------------------------------------------------

vbm, cbm, gap = calculate_bandgap(bands)

print("\nBandgap results")
print("VBM =", vbm)
print("CBM =", cbm)
print("Gap =", gap, "eV")


# ------------------------------------------------
# PLOT
# ------------------------------------------------

fig, (ax1, ax2) = plt.subplots(
    1,2,
    figsize=(11,6),
    gridspec_kw={'width_ratios':[2,1]},
    sharey=True
)


# ----- BAND STRUCTURE -----

for i in range(bands.shape[1]):
    ax1.plot(kdist, bands[:,i], color="deepskyblue")

ax1.axhline(0, color="black", linestyle="--", linewidth=1)

for t in ticks:
    ax1.axvline(t, color="black", linestyle="--", linewidth=1)

ax1.set_ylim(E_MIN, E_MAX)
ax1.set_xlim(0, ticks[-1])

ax1.set_ylabel("Energy (eV)")
ax1.set_title("Band Structure")

ax1.set_xticks(ticks)
ax1.set_xticklabels(tick_labels)


# ----- DOS -----

ax2.plot(total_dos, dos_energy, color="black", label="Total DOS")
ax2.plot(zr_dos, dos_energy, color="coral", label="Zr-d")
ax2.plot(se_pdos, dos_energy, color="dodgerblue", label="Se-p")

ax2.fill_betweenx(dos_energy, 0, total_dos, color="gray", alpha=0.2)

ax2.axhline(0, color="black", linestyle="--", linewidth=1)

ax2.set_xlim(0,25)

ax2.set_xlabel("DOS (states/eV)")
ax2.set_title("Density of States")

ax2.legend()

plt.tight_layout()
plt.show()
