# Evidence Guide

The authentic screenshots are retained under `screenshots/`. This guide uses the visible timing in each image where available instead of relying on screenshot-number references. The raw screenshots themselves are not modified.

## Evidence and timing map

| File | Timing visible in image | Evidence interpretation |
|---|---|---|
| `01-environment/01-windows-vm-system-information.png` | Not displayed | Windows 11 Pro system information. |
| `01-environment/02-hostname-network.jpeg` | Not displayed | Hostname/network command output; the image contains sanitization. |
| `01-environment/03-python-version.png` | Not displayed | Python 3.14.7. |
| `02-sysmon/04-sysmon-service.png` | Not displayed | Sysmon service running. |
| `02-sysmon/05-sysmon-config.png` | Not displayed | Sysmon 15.21 configuration and lab filters. |
| `02-sysmon/06-sysmon-process-event.jpeg` | Event: 2026-09-05 17:25:58.904 UTC; local display 22:25:58 | Representative Sysmon Event ID 1 for `cmd.exe /c whoami`; not simulator-specific. |
| `03-wazuh/07-wazuh-agent-service.png` | Not displayed | Wazuh service running. |
| `03-wazuh/08-wazuh-agent-active.png` | Not displayed | Agent `001` Active. |
| `03-wazuh/09-sysmon-event-wazuh.png` | Visible alert time 2026-09-07 01:06:53.944 | Wazuh alert/dashboard visibility. |
| `04-baseline/10-clean-test-directory.png` | 2026-09-07 01:17–01:18 | Clean synthetic baseline directory and initial files. |
| `04-baseline/11-wazuh-baseline.jpeg` | Displayed file metadata around 03:56:30–03:56:36; capture time not displayed | Wazuh Integrity Monitoring baseline/inventory. |
| `05-simulation/12-simulator-execution.png` | Not displayed | Safe simulator completed and reported no encryption/destructive action. |
| `05-simulation/13-post-simulation-files.png` | File dates 2026-09-07; exact times not displayed | Synthetic `.locked` artifacts and simulated ransom note are visible. |
| `06-telemetry/14-simulator-process-telemetry.png` | 2026-09-07 01:55:57.729–01:55:59.456 | Rule `92154` `taskschd.dll` activity; simulator attribution not established. |
| `06-telemetry/15-file-activity-telemetry.png` | 2026-09-07 01:54:51.733–01:54:52.820 | Lab-path file activity; rules `553`/`554` visible. |
| `07-detection/16-wazuh-rule-test.png` | Visible alert range 01:22:58.569–02:06:38.606 | Wazuh rule-test/alert view; relevant visible rule is `92154`. |
| `07-detection/17-ransomware-simulation-alert.png` | 2026-09-07 01:54:51.707–01:54:51.787 | Rule `553` file-deletion alerts. |
| `07-detection/18-alert-details.png` | 2026-09-07 01:54:51.787 | Rule `553` detail for a lab-path synthetic file deletion. |
| `08-investigation/19-investigation-correlation.png` | 2026-09-07 02:00:57.903–02:02:03.965 | Broader Wazuh correlation view; simulator attribution is not proven for every alert. |
| `09-validation/20-final-validation.png` | Single capture time not displayed | Final Wazuh dashboard snapshot; not a ransomware-detection success metric. |

## Evidence rules

Only claims supported by the screenshots are made in the documentation. No Event ID, rule ID, timestamp, hash, technique, or detection result is invented. Where timing is not visible, the documentation explicitly says so.

The archive does not include raw `.evtx` or simulator runtime logs, so those are not claimed as delivered evidence.
