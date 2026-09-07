# Architecture

The lab has four logical stages:

1. **Simulation** — the Python simulator creates synthetic documents, renames them to `.locked`, and creates `SIMULATED_RANSOM_NOTE.txt`.
2. **Endpoint telemetry** — Windows and Sysmon provide process/file telemetry; Wazuh also monitors the lab directory through its configured collection/FIM path.
3. **Detection and investigation** — Wazuh Manager/Dashboard displays events and alerts for analyst review.
4. **Validation** — the analyst correlates the simulator's known actions with the captured telemetry and records only conclusions supported by the screenshots.

The supplied evidence demonstrates endpoint readiness, Wazuh visibility, simulator execution, and lab-path file activity. It does **not** establish that the repository's custom ransomware rules fired.

The diagram is stored locally as `architecture.png` so the repository has no broken external dependency.
