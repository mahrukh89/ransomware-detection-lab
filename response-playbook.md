# Ransomware Simulation Incident Response Playbook

## 1. Preparation

- Use an isolated Windows VM.
- Restrict simulation to `C:\RansomwareLab\TestData`.
- Enable endpoint telemetry before execution.
- Preserve screenshots and raw logs where available.

## 2. Detection

- Review Wazuh alerts.
- Record the exact rule ID and timestamp.
- Correlate the alert with the simulator's known activity and lab path.

## 3. Analysis

- Confirm the process responsible using endpoint telemetry.
- Review affected synthetic files.
- Build a timestamped timeline.
- Separate simulator-caused activity from unrelated background alerts.

## 4. Containment

In this lab: stop the simulator and preserve evidence.

In a real incident: isolate the endpoint and preserve forensic evidence.

## 5. Eradication

In this lab: remove only synthetic artifacts after evidence preservation.

In a real incident: remove malicious artifacts and address persistence/initial access as appropriate.

## 6. Recovery

Restore trusted data if needed, verify endpoint health, and confirm monitoring.

## 7. Lessons Learned

The supplied run demonstrates why alert proximity is not enough for attribution. Wazuh file-activity alerts were visible, but the screenshots do not prove that the repository's custom ransomware rules fired.
