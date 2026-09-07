# MITRE ATT&CK Assessment

ATT&CK mapping is intentionally conservative.

## Evidence-based assessment

The simulator **renames synthetic files** to `.locked` and creates a synthetic note. It does not encrypt data and therefore does not provide evidence for a real ransomware encryption technique.

The Wazuh screenshots show several ATT&CK labels, including `T1053.005`-like scheduled-task labeling around rule 92154. Those alerts are not demonstrated to originate from the simulator and are therefore **not mapped to this ransomware lab behavior**.

## Result

**No ransomware ATT&CK technique is marked as validated from the supplied screenshots.**

A future iteration should map only behavior that is both actually observed and attributable to the simulator, with the corresponding event and detection evidence captured.
