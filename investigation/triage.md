# SOC Alert Triage — Evidence-Based Record

## Scope

The investigation concerns the controlled simulation under `C:\RansomwareLab\TestData`.

## Confirmed observations

- The simulator completed safely; the console explicitly reported no encryption or destructive actions. The capture does not display an execution timestamp.
- The post-simulation directory is dated 2026-09-07 and contains synthetic `.locked` files and `SIMULATED_RANSOM_NOTE.txt`.
- Wazuh shows lab-path file activity at **2026-09-07 01:54:51.733–01:54:52.820**, with rules `553` and `554` visible.
- Rule `553` file-deletion alerts are visible at **01:54:51.707–01:54:51.787**.

## Attribution caveat

Wazuh also shows `taskschd.dll` activity under rule `92154` at **01:55:57.729–01:55:59.456**. The evidence does not establish that this activity was caused by the simulator, so it is treated as unrelated/background activity.

## Analyst conclusion

**Confirmed:** controlled synthetic file activity was generated and observable in Wazuh.

**Not confirmed:** a ransomware-specific custom Wazuh detection fired as a result of the simulator.

This distinction is the primary investigation finding.
