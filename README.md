# Project VORTEX: Microgravity BEC Topology Simulator

**V**ortex **O**bservation, **R**esearch & **T**opological **EX**periments

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Active Development](https://img.shields.io/badge/status-active-success.svg)]()

**Project VORTEX** is an open-source computational framework for simulating the dynamics of topological defects—specifically quantized vortex lattices—in Bose-Einstein Condensates (BECs) under microgravity conditions.

Inspired by recent record-breaking achievements in orbital cold atom physics (e.g., the Tiangong Space Station's 9.7 picokelvin Rb-87 experiment), this project aims to model how long-baseline freefall environments enable the study of quantum turbulence, analog gravity, and topological interferometry impossible on Earth.

---

## 🔭 Scientific Motivation

On Earth, the study of Bose-Einstein Condensates is fundamentally limited by gravity. Once released from a trap, the atomic cloud falls and thermalizes within milliseconds. This severely restricts the observation time of fragile quantum phenomena such as:
1.  **Quantum Turbulence:** The decay and interaction of quantized vortex lines.
2.  **Analog Gravity:** The formation of acoustic event horizons (dumb holes) within the fluid.
3.  **Topological Phase Stability:** The preservation of macroscopic quantum phase information over long durations.

**Project VORTEX** leverages the microgravity environment (simulated here by removing the trap potential $V(r)$ in a zero-g frame) to extend observation windows to **seconds**, modeling the expansion of topologically encoded matter waves.

---

## 🧠 Core Physics Engine

The simulation utilizes a **2D Split-Step Fourier Method (SSFM)** to solve the Time-Dependent Gross-Pitaevskii Equation (TDGPE):

$$ i\hbar \frac{\partial \psi(\mathbf{r},t)}{\partial t} = \left[ -\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r},t) + g|\psi(\mathbf{r},t)|^2 \right] \psi(\mathbf{r},t) $$

Where:
*   $\psi$ is the macroscopic wavefunction.
*   $V(\mathbf{r},t)$ is the time-dependent optical trap potential.
*   $g$ represents the non-linear interaction strength (repulsive scattering).

### The "Topological Imprint" Module
Unlike standard thermal cloud simulators, Project VORTEX includes a specific initialization phase designed to inject **orbital angular momentum** into the ground state. By applying a phase winding of $e^{i\ell\phi}$, the simulator creates a **Phase Singularity**—a quantized vortex core—allowing researchers to track the topological stability of the "hole" in the matter wave during free expansion.

---

## 🚀 Features

*   **Gross-Pitaevskii Solver:** High-performance 2D SSFM implementation using NumPy FFTs.
*   **Microgravity Drop Simulation:** Instantly switches off the harmonic trap potential to simulate free-fall expansion.
*   **Vortex Imprinting:** Automatic initialization of a quantized vortex ($\ell=1$) via phase engineering.
*   **Real-Time Visualization:** Live plotting of Density $|\psi|^2$ and Phase $\angle \psi$ to observe vortex core stability.

---

## 🛠️ Installation & Usage

### Prerequisites
*   Python 3.9 or higher
*   NumPy
*   Matplotlib

### Setup
```bash
# Clone the repository
git clone https://github.com/bordode/Project-VORTEX-Simulator.git
cd Project-VORTEX-Simulator

# Install dependencies
pip install -r requirements.txt
```

### Running the Simulation
To run the baseline vortex expansion simulation:
```bash
python gpe_vortex_sim.py
```

---

## 🗺️ Roadmap

*   [x] **v0.1.0:** Basic 2D GPE Split-Step Solver with Harmonic Trap.
*   [x] **v0.1.1:** Vortex Phase Imprinting and Trap Release (Microgravity) logic.
*   [ ] **v0.2.0:** **Topological Winding Number Calculator.** Implement $\oint \nabla \phi \cdot dl$ integration to mathematically verify topological charge quantization.
*   [ ] **v0.3.0:** **Acoustic Horizon Metrics.** Calculate the local speed of sound vs. fluid velocity to identify analog event horizons.
*   [ ] **v0.4.0:** **3D Visualization.** Extend solver to 3D Cartesian grid (requires GPU acceleration/CuPy).

---

## 📚 References & Inspiration

*   **Tiangong Space Station BEC Record:** Xiong, W. et al., "Quantum gases below 10 picokelvin in space," *Science* (2026). DOI: [10.1126/science.aea5324](https://doi.org/10.1126/science.aea5324) — Rb-87 condensate aboard Tiangong's Cold Atom Physics Rack; 9.7 pK equivalent temperature, 7-second free expansion.
*   **Gross-Pitaevskii Equation:** Pitaevskii, L. P. (1961). "Vortex lines in an imperfect Bose gas." *Soviet Physics JETP*.
*   **Analog Gravity:** Barceló, C., Liberati, S., & Visser, M. (2011). "Analogue Gravity." *Living Reviews in Relativity*.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

*Project VORTEX is an independent research tool and is not affiliated with the China Manned Space Agency (CMSA) or the Tiangong program.
