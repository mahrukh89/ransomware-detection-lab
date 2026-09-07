# Detection Logic

## Intended objective

Detect ransomware-like behavior through correlated endpoint signals while avoiding the false conclusion that one renamed file or one alert equals ransomware.

## Simulator signals

The simulator intentionally creates:

- 30 synthetic documents;
- `.locked` renamed copies;
- `SIMULATED_RANSOM_NOTE.txt`.

## Observed telemetry

Wazuh shows lab-path file activity at **2026-09-07 01:54:51.733–01:54:52.820**, including synthetic document paths and the simulated note. Rules **553** (file deleted) and **554** (file added) are visible.

Rule **553** file-deletion alerts are visible at **01:54:51.707–01:54:51.787**.

These are the actual captured Wazuh signals. They should not be relabeled as a ransomware-specific detection.

## Custom rule status

`wazuh/rules/local_rules.xml` contains:

- `100100` — simulated ransom-note match;
- `100101` — `.locked` indicator match.

The captured evidence does not show either custom rule triggering. Consequently, their status is **not validated by the captured run**.

## Detection conclusion

The lab demonstrates that synthetic file activity reached Wazuh and generated observable file-integrity/security telemetry. It does not prove a complete ransomware-specific behavioral correlation rule.
