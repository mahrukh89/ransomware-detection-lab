# Evidence Timeline

This timeline uses only times visibly present in the authentic evidence. The time column describes either an event/alert time shown in the screenshot or displayed file metadata; it is not automatically the screenshot capture time.

| Time | Observation | Interpretation |
|---|---|---|
| 2026-09-05 17:25:58.904 UTC (22:25:58 local display) | Sysmon Event ID 1 for `cmd.exe /c whoami` | Representative process telemetry; not simulator-specific. |
| 2026-09-07 01:06:53.944 | Wazuh dashboard alert time | Endpoint security telemetry is visible in Wazuh. |
| 2026-09-07 01:17–01:18 | Baseline directory/file timestamps | Synthetic baseline directory and files were created/populated. |
| 2026-09-07 01:54:51.733–01:54:52.820 | Wazuh file activity for the lab path | Synthetic document and simulated-note activity was observable; rules `553`/`554` are visible. |
| 2026-09-07 01:54:51.707–01:54:51.787 | Wazuh rule `553` file-deletion alerts | File-deletion activity was recorded for the lab endpoint. |
| 2026-09-07 01:55:57.729–01:55:59.456 | Wazuh rule `92154` `taskschd.dll` alerts | Background activity; the evidence does not attribute it to the simulator. |
| 2026-09-07 02:00:57.903–02:02:03.965 | Multiple Wazuh alerts in investigation view | Investigation/correlation context. |
| 2026-09-07 02:06:38.606 | Latest visible alert in the rule-test/alert view | Wazuh alert view captured; relevant visible rule is not a custom ransomware rule. |

The supplied screenshots do not provide enough timestamped information to build a complete simulator-start-to-alert causal timeline. No unsupported event times are added.
