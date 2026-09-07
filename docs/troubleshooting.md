# Troubleshooting

## Sysmon is not running

Run `Get-Service Sysmon*` and review the Sysmon installation/configuration output. The captured Sysmon service state was obtained without a displayed capture timestamp.

## Sysmon events are missing

Check:

`Event Viewer → Applications and Services Logs → Microsoft → Windows → Sysmon → Operational`

Confirm the active configuration contains the filters required by the lab. The representative process event in the supplied evidence is timestamped **2026-09-05 17:25:58.904 UTC**.

## Wazuh Agent is not Active

Check the Wazuh agent service and connectivity to the Wazuh Manager. The supplied service and agent-state captures show a healthy state, but their capture times are not displayed.

## Wazuh does not show lab file activity

Verify that the Windows agent is collecting the configured lab path/FIM telemetry. The supplied file-activity capture shows lab-path activity at **2026-09-07 01:54:51.733–01:54:52.820**.

## Custom rule does not trigger

Inspect the exact decoded event first. The supplied evidence shows rules `553`/`554` for file activity and rule `92154` for `taskschd.dll`; it does not show custom rules `100100`/`100101` firing. Do not change fields or rule IDs based on assumptions.

## Too many alerts

Treat background Wazuh alerts as separate until process, path, and timestamp correlation proves attribution. The captured `taskschd.dll` activity occurred at **01:55:57.729–01:55:59.456**, after the visible lab-path file activity, but proximity alone does not prove causality.
