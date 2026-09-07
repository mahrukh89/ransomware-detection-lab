# Wazuh

This directory contains the lab's Wazuh detection-engineering material.

## Captured state

- SS-07 shows the Wazuh service running.
- SS-08 shows Wazuh Agent `001` as Active.
- SS-09 shows the Windows endpoint producing a Wazuh alert in the dashboard.

The later evidence (SS-15 through SS-19) shows file-integrity/security alerts for the lab path and other background alerts.

## Important evidence boundary

The repository's `wazuh/rules/local_rules.xml` contains custom rules `100100` and `100101` as lab detection-engineering definitions. The supplied screenshots do **not** demonstrate those rules firing.

The captured alerts include Wazuh rule IDs such as **553**, **554**, **92213**, **92154**, **92217**, and **92219**. These are observed evidence, not replacement custom ransomware rules. Their presence should not be interpreted as proof of ransomware detection.

Always validate rule fields against the actual decoded events before deployment.
