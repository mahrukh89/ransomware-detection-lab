# Detection Validation

This record reflects the authentic captured evidence, not an assumed successful test run.

| Test | Timing visible in evidence | Result |
|---|---|---|
| Environment readiness | Not displayed | PASS |
| Sysmon service/configuration visible | Not displayed | PASS |
| Representative Sysmon Event ID 1 visible | 2026-09-05 17:25:58.904 UTC | PASS |
| Wazuh agent active | Not displayed | PASS |
| Wazuh dashboard telemetry visible | 2026-09-07 01:06:53.944 alert time | PASS |
| Clean lab baseline captured | 2026-09-07 01:17–01:18 | PASS |
| Safe simulator completed | Execution time not displayed | PASS |
| Post-simulation synthetic artifacts visible | 2026-09-07; exact times not displayed | PASS |
| File activity visible in Wazuh | 2026-09-07 01:54:51.733–01:54:52.820 | PASS |
| Wazuh rule-test/alert view captured | Visible alert range 01:22:58.569–02:06:38.606 | PASS as an evidence capture; relevant visible rule is `92154`, not the custom rules |
| Ransomware-specific custom rule firing | No custom-rule timestamp/rule match is visible | NOT PROVEN; captured lab-path alerts use rule `553` |
| Investigation/correlation view | 2026-09-07 02:00:57.903–02:02:03.965 | PASS as investigation context; simulator attribution is not proven |
| Final dashboard capture | Single capture time not displayed | PASS as dashboard snapshot; not a ransomware-detection success metric |

## Overall validation result

**Telemetry and simulation workflow: validated.**

**Custom ransomware-specific detection: not conclusively validated.**

No PASS claim is made for a custom ransomware rule because the captured evidence does not show its rule ID.
