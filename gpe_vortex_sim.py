import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ==============================================================================
# PROJECT VORTEX: Microgravity BEC Topology Simulator
# ------------------------------------------------------------------------------
# Physics: Time-Dependent Gross-Pitaevskii Equation (TDGPE)
# Method: Split-Step Fourier Method (SSFM)
# Scenario: Rb-87 Condensate, Vortex Imprinting, Trap Release (Microgravity)
# ==============================================================================

def initialize_simulation():
    # --- 1. Physical Constants (Rubidium-87) ---
    hbar = 1.0545718e-34      # J*s
    m_Rb = 1.443160e-25       # kg (Mass of Rb-87 atom)
    a_s = 100.4e-12           # m (Scattering length of Rb-87)

    # --- 2. Simulation Grid Parameters ---
    # We use a normalized grid for numerical stability
    N = 256                   # Grid resolution (256x256)
    L = 10.0                  # Box size in micrometers (um)
    dx = L / N
    dt = 0.001                # Time step (in units of 1/omega)
    steps = 200               # Number of time steps per frame

    x = np.linspace(-L/2, L/2, N)
    y = np.linspace(-L/2, L/2, N)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y, X)

    # --- 3. Interaction Strength (g) ---
    # g = 4 * pi * hbar^2 * a_s / m
    # Scaled for dimensionless simulation
    g = 1000.0

    # --- 4. Initial State: Thomas-Fermi Profile ---
    # A BEC in a harmonic trap looks like an inverted parabola (density)
    # We initialize a Gaussian that will relax into Thomas-Fermi
    psi = np.exp(-(X**2 + Y**2) / 4.0)

    # --- 5. The "Vinyl" Press: Phase Imprinting ---
    # We multiply the wavefunction by e^(i * theta) to create a vortex (winding number = 1)
    # This creates a phase singularity (a hole) in the center of the condensate
    psi = psi * np.exp(1j * Theta)

    # Normalize the wavefunction so total atoms = 1
    psi = psi / np.sqrt(np.sum(np.abs(psi)**2))

    return N, L, dx, dt, steps, X, Y, R, Theta, psi, g

def calculate_potential(X, Y, trap_on=True):
    """
    Simulates the Cold Atom Physics Rack Optical Trap.
    If trap_on=False, we are in the 'Microgravity Expansion' phase.
    """
    if trap_on:
        # Harmonic Trap: V = 0.5 * r^2
        return 0.5 * (X**2 + Y**2)
    else:
        # Free Space (Microgravity Drop)
        return np.zeros_like(X)

def split_step_fourier(psi, V, g, dx, dt):
    """
    The core engine: Evolves the wavefunction in time.
    """
    N = len(psi)

    # Kinetic Energy Operator in Fourier Space: K = -hbar^2 k^2 / 2m
    # In dimensionless units: K = k^2
    kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    ky = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    KX, KY = np.meshgrid(kx, ky)
    K2 = KX**2 + KY**2

    # Step 1: Half-step Potential + Nonlinear Interaction
    # Nonlinearity: g * |psi|^2
    density = np.abs(psi)**2
    V_eff = V + g * density

    psi = psi * np.exp(-0.5j * V_eff * dt)

    # Step 2: Full-step Kinetic Evolution (Fourier Space)
    psi_k = np.fft.fft2(psi)
    psi_k = psi_k * np.exp(-0.5j * K2 * dt)
    psi = np.fft.ifft2(psi_k)

    # Step 3: Half-step Potential + Nonlinear Interaction
    density = np.abs(psi)**2
    V_eff = V + g * density
    psi = psi * np.exp(-0.5j * V_eff * dt)

    # Renormalize to prevent numerical drift
    psi = psi / np.sqrt(np.sum(np.abs(psi)**2))

    return psi

def run_simulation():
    # Initialize
    N, L, dx, dt, steps, X, Y, R, Theta, psi, g = initialize_simulation()

    # Setup Plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle('Project VORTEX: Microgravity BEC Topology Simulation')

    # Simulation Loop
    # Phase 1: Relax in Trap (Stabilize the Vortex)
    print("Phase 1: Stabilizing Vortex in Trap...")
    V_trap = calculate_potential(X, Y, trap_on=True)
    for _ in range(50):
        psi = split_step_fourier(psi, V_trap, g, dx, dt)

    # Phase 2: The Tiangong Drop (Trap Release)
    print("Phase 2: Releasing Trap (Simulating 7-second freefall)...")
    V_free = calculate_potential(X, Y, trap_on=False)

    density_plot = ax1.imshow(np.abs(psi)**2, extent=[-L/2, L/2, -L/2, L/2], cmap='inferno')
    phase_plot = ax2.imshow(np.angle(psi), extent=[-L/2, L/2, -L/2, L/2], cmap='twilight')

    ax1.set_title('Density |ψ|² (The "Record")')
    ax2.set_title('Phase ∠ψ (The "Groove")')

    # Animate the expansion
    try:
        for i in range(100):
            # Evolve
            psi = split_step_fourier(psi, V_free, g, dx, dt)

            # Update Plots
            density_plot.set_data(np.abs(psi)**2)
            phase_plot.set_data(np.angle(psi))
            plt.pause(0.05)

    except KeyboardInterrupt:
        print("Simulation stopped by user.")

    plt.show()

if __name__ == "__main__":
    run_simulation()
