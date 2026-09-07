# Simulator Evidence

The simulator is a controlled, harmless ransomware-behavior simulation. It creates synthetic files, performs the lab's `.locked` rename behavior, and creates `SIMULATED_RANSOM_NOTE.txt`; it does not encrypt data or perform destructive actions.

- At simulator execution, the console reports successful completion and explicitly states that no encryption or destructive actions were performed. The capture does not display an execution timestamp.
- In the post-simulation directory listing, file dates are 2026-09-07; exact capture/file times are not legible enough to assign a precise time.

The original screenshots remain untouched under `screenshots/05-simulation/`. No raw `simulation.log` was supplied, so none is fabricated.
