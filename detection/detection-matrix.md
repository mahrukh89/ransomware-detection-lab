# Detection Matrix

| ID | Signal / use case | Timing / actual evidence | Status |
|---|---|---|---|
| DET-001 | Simulator execution | Execution time not displayed; console reports safe completion | Confirmed simulator completed |
| DET-002 | Synthetic `.locked` files | Post-simulation files dated 2026-09-07; exact times not displayed | Confirmed in directory |
| DET-003 | Simulated ransom note | Visible after simulation; lab-path activity visible at 01:54:51.733–01:54:52.820 | Confirmed as synthetic artifact |
| DET-004 | Wazuh file activity | 2026-09-07 01:54:51.733–01:54:52.820; rules `553`/`554` visible | Confirmed |
| DET-005 | File-deletion alert in lab path | 2026-09-07 01:54:51.707–01:54:51.787; rule `553` | Confirmed |
| DET-006 | Custom rule `100100`/`100101` | No matching custom-rule timestamp or rule ID visible | Not validated |
| DET-007 | Simulator-specific Sysmon Event ID 1 | Representative Event ID 1 is 2026-09-05 17:25:58.904 UTC for `cmd.exe`, not simulator | Not validated |
| DET-008 | Ransomware-specific multi-signal correlation | No conclusive timestamped custom-rule evidence | Not validated |
