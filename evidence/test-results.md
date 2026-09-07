# Detection Validation

This record reflects only what the authentic screenshots demonstrate. Timing is included where it is visible in the evidence; no missing timestamp is inferred.

| Test | Timing visible in evidence | Result |
|---|---|---|
| Environment readiness | Not displayed | PASS |
| Sysmon service/configuration visible | Not displayed | PASS |
| Representative Sysmon Event ID 1 visible | 2026-09-05 17:25:58.904 UTC | PASS |
| Wazuh agent active | Not displayed | PASS |
| Wazuh dashboard telemetry visible | 2026-09-07 01:06:53.944 alert time | PASS |
| Clean lab baseline captured | Directory/file activity at 01:17–01:18 on 2026-09-07 | PASS |
| Safe simulator completed | Exact execution time not displayed | PASS |
| Post-simulation synthetic artifacts visible | Files dated 2026-09-07; exact times not displayed | PASS |
| File activity visible in Wazuh | 2026-09-07 01:54:51.733–01:54:52.820 | PASS |
| Wazuh rule-test/alert view captured | Visible alert range 01:22:58.569–02:06:38.606 | PASS as evidence capture; relevant visible rule is `92154`, not the custom rules |
| Ransomware-specific custom rule firing | No custom-rule timestamp/rule match is visible | NOT PROVEN; captured alerts show rule `553` file-deletion activity |
| Investigation/correlation view | 2026-09-07 02:00:57.903–02:02:03.965 | PASS as investigation context; simulator attribution is not proven |
| Final dashboard capture | Single capture time not displayed | PASS as dashboard snapshot; not a ransomware-detection success metric |

## Overall validation result

**Validated:** lab readiness, safe simulation execution, synthetic artifact creation, endpoint/Wazuh visibility, and observable file activity.

**Not conclusively validated:** ransomware-specific custom Wazuh detection. The evidence does not show custom rules `100100` or `100101` firing.
