# Sysmon Evidence

The original captures are retained unchanged.

| Capture | Timing visible in image | What it establishes |
|---|---|---|
| `04-sysmon-service.png` | Capture time not visible | Sysmon service is shown running. |
| `05-sysmon-config.png` | Capture time not visible | Sysmon 15.21 and the active lab configuration are shown, including Python process and `RansomwareLab` file-create filters. |
| `06-sysmon-process-event.jpeg` | Event: 2026-09-05 17:25:58.904 UTC; local display: 2026-09-05 22:25:58 | Representative Sysmon Event ID 1 for `cmd.exe /c whoami`. |

The Event ID 1 capture is representative process telemetry, not proof of the simulator process.
