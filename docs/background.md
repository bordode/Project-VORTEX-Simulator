# Background: what a BEC vortex is — and what it isn't

## No warp drive

A Bose-Einstein condensate vortex does **not** create a vortex in the
space-time continuum, and it cannot be used as an engine for
faster-than-light travel. Warping space-time takes immense mass-energy.
The Tiangong experiment uses about 20,000 Rubidium-87 atoms — a total
mass of roughly $3 \times 10^{-21}$ kg. Its gravitational effect on
space-time is negligible.

## What it is

A **quantized vortex in a quantum fluid**: a phase singularity in the
macroscopic wavefunction, with the phase winding by $2\pi$ around the
core (winding number $\ell = 1$). This simulator imprints exactly that
vortex and watches it evolve after trap release.

## Analog gravity

The vortex core acts as an **acoustic event horizon** for sound waves
(phonons) travelling through the condensate: phonons inside the core
region cannot escape, in the same way light cannot escape a black hole.
Vortices like this are a laboratory route to studying analog Hawking
radiation. The vortex is a desktop black-hole analog, not a real one.

## The real payoff: quantum inertial navigation

The Tiangong result matters because of what the long microgravity window
enables: 7 seconds of free expansion at 9.7 picokelvins
(Xiong et al., *Science* 2026, DOI 10.1126/science.aea5324). A slowly
expanding condensate is an ultra-sensitive gyroscope and accelerometer.
Matter-wave interferometry on such a cloud is the foundation of
**quantum inertial navigation** — drift-free navigation for deep space,
where GPS does not exist. The condensate is not the engine; it is the
compass.

## Scope and non-goals

This repository does not model warp drives, inertial mass reduction, or
dark-matter detection, and it makes no such claims. Exploratory
Assembly Index ($A_c$) sandbox work on BECs — including illustrative
simulated values sometimes quoted for vortex-lattice states — is separate
from this simulator: those numbers are simulations for theoretical
exploration, not measurements, and they are not part of this repo.
Topological charge here is verified by direct calculation of the
circulation $\oint \nabla\phi \cdot dl$ (see Issue #1), not by any
non-integer "Chern number": a genuine Chern number is an integer.
