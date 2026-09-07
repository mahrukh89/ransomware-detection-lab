# Safe Ransomware-Behavior Simulator

The simulator is intentionally harmless and is for a controlled defensive lab only.

## Actual behavior

`ransomware_simulator.py`:

1. Loads `config.json`.
2. Verifies the target is below the configured allowed root.
3. Creates **30** synthetic `.txt` documents by default.
4. Renames those documents to the configured `.locked` extension.
5. Creates `SIMULATED_RANSOM_NOTE.txt`.
6. Writes simulator messages to the configured log destination when logging is enabled.
7. Prints a completion message stating that no encryption/destructive actions were performed.

## Safety boundary

Default target:

`C:\RansomwareLab\TestData`

The code contains no encryption, deletion, persistence, credential theft, evasion, network propagation, or remote-control behavior.

## Captured run timing

The simulator execution capture does not display a clock timestamp, so no execution time is assigned. The post-simulation directory listing is dated **2026-09-07**, but its exact file times are not sufficiently visible to establish a precise simulation completion time.

Wazuh subsequently shows lab-path file activity at **2026-09-07 01:54:51.733–01:54:52.820**. This is reported as observed telemetry time, not as an invented simulator start time.

The supplied archive does not contain the runtime `simulation.log`; the repository therefore does not claim to provide a raw simulator log.
