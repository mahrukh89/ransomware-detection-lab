# Telemetry Evidence

The original captures are retained unchanged.

| Capture | Timing visible in image | What it establishes |
|---|---|---|
| `14-simulator-process-telemetry.png` | 2026-09-07 01:55:57.729–01:55:59.456 | Wazuh alert rows showing rule `92154` for `taskschd.dll` activity. The evidence does not establish that this activity came from the simulator. |
| `15-file-activity-telemetry.png` | 2026-09-07 01:54:51.733–01:54:52.820 | Wazuh file activity for the lab path, including synthetic document and simulated-note paths; rules `553` and `554` are visible. |

The 01:54:51–01:54:52 activity is the strongest supplied evidence that the synthetic file activity was observable in Wazuh.
