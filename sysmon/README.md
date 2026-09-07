# Sysmon

This directory contains the Sysmon configuration used by the lab.

## Captured state

SS-04 shows the Sysmon service running. SS-05 shows Sysmon 15.21 using `sysmon/sysmon-config.xml`.

The supplied configuration includes:

- `ProcessCreate` filtering for `python.exe` / `pythonw.exe`;
- `FileCreate` filtering for paths containing `RansomwareLab`;
- SHA256 hashing;
- Sysmon configuration schema 4.90.

SS-06 is a representative **Sysmon Event ID 1 Process Create** event, but the captured event is for `cmd.exe` executing `whoami` under SYSTEM. It is not evidence that the simulator process itself generated a Sysmon Event ID 1 event.

Do not treat SS-06 as simulator telemetry.
