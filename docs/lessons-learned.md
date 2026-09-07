# Lessons Learned

## What worked

- The Windows lab environment was captured and documented.
- Sysmon was running with the supplied lab configuration.
- Wazuh Agent `001` was active.
- The simulator completed without encryption or destructive behavior.
- The synthetic post-simulation files were visible.
- Wazuh generated observable file-integrity/security telemetry for the lab path at **2026-09-07 01:54:51.733–01:54:52.820**.

## What did not validate

The captured evidence does not show custom ransomware rules `100100` or `100101` firing. The visible lab-path file-deletion alerts at **01:54:51.707–01:54:51.787** use rule `553`, while `taskschd.dll` alerts at **01:55:57.729–01:55:59.456** use rule `92154` and are not attributed to the simulator.

## Detection improvement

A production-quality lab iteration should capture the exact decoded simulator events and then validate a narrowly scoped correlation rule against those fields. The custom rules should not be promoted until their rule IDs are visible in a successful rule test and alert.

## False-positive lesson

Background Wazuh alerts were present during the run. This demonstrates why attribution must use process, path, timestamp, and event correlation rather than assuming every alert near a simulation is caused by the simulator.

## SOC skills demonstrated

Environment verification, endpoint telemetry review, Wazuh agent verification, baseline comparison, alert triage, evidence preservation, attribution discipline, and validation reporting.
