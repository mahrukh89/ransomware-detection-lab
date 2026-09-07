# Detection Evidence

The original captures are retained unchanged.

| Capture | Timing visible in image | What it establishes |
|---|---|---|
| `16-wazuh-rule-test.png` | Visible alert times range from 2026-09-07 01:22:58.569 to 02:06:38.606 | Wazuh alert/rule-test view. The visible rule in the relevant rows is `92154`, not the repository's custom ransomware rules. |
| `17-ransomware-simulation-alert.png` | 2026-09-07 01:54:51.707–01:54:51.787 | Multiple rule `553` file-deletion alerts for the lab endpoint. |
| `18-alert-details.png` | 2026-09-07 01:54:51.787 | Rule `553` alert detail for a lab-path synthetic file deletion. |

The supplied captures do not prove that custom rules `100100` or `100101` triggered.
