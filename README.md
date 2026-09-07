# Ransomware Detection & Incident Response Lab

A controlled Windows SOC/Blue Team lab demonstrating **safe ransomware-like file activity**, endpoint telemetry, Wazuh monitoring, alert investigation, and evidence-based validation.

> **Safety:** The simulator is a harmless training component. It creates synthetic files, renames them to `.locked`, and creates `SIMULATED_RANSOM_NOTE.txt`. It does **not** encrypt data, delete files, establish persistence, steal credentials, evade controls, or propagate over a network.

## Objective

Build and document an end-to-end defensive workflow:

1. Generate controlled ransomware-like activity in a dedicated test directory.
2. Observe Windows endpoint telemetry with Sysmon and Wazuh.
3. Investigate file activity and related alerts.
4. Preserve screenshots as evidence.
5. Validate what the captured evidence actually proves, without inventing rule IDs, Event IDs, timestamps, or detection results.

## Architecture / Workflow

```text
Python safe simulator
        |
        v
C:\RansomwareLab\TestData
        |
        +--> Windows / Sysmon telemetry
        |
        +--> Wazuh Agent
                |
                v
          Wazuh Manager / Dashboard
                |
                +--> FIM / security alerts
                |
                v
          Analyst investigation
                |
                +--> Timeline
                +--> Indicators
                +--> Validation
                +--> ATT&CK assessment
```

See [`architecture/README.md`](architecture/README.md) and [`architecture/architecture.png`](architecture/architecture.png).

## Technologies

| Technology | Role |
|---|---|
| Windows 11 Pro | Lab endpoint |
| Python 3.14.7 | Harmless behavior simulator |
| Sysmon 15.21 | Endpoint process/file telemetry |
| Wazuh Agent | Endpoint collection |
| Wazuh Manager / Dashboard | Monitoring, FIM and alert investigation |
| MITRE ATT&CK | Behavior-mapping reference |
| Git / GitHub | Portfolio delivery |

## Detection Methodology

The intended detection model is **behavioral correlation**, rather than treating a single filename or extension as proof of ransomware.

The simulator produces three useful synthetic signals:

- creation of 30 synthetic documents;
- rename of those documents to `.locked`;
- creation of `SIMULATED_RANSOM_NOTE.txt`.

The repository's Wazuh custom rules are retained as lab engineering material, but the supplied screenshots do **not** prove that those custom rule IDs triggered. The captured Wazuh evidence instead shows file-integrity/security telemetry, including rule IDs **553** and **554**, and other unrelated background alerts.

Therefore, this final repository does **not** claim successful custom-rule ransomware detection.

## Investigation

The evidence was reviewed in sequence:

- endpoint and tooling readiness;
- Sysmon configuration and representative process telemetry;
- Wazuh agent health and dashboard visibility;
- clean baseline;
- simulator execution and post-simulation file state;
- Wazuh file-activity telemetry;
- alert details and surrounding alerts;
- final dashboard validation.

The investigation documentation explicitly separates **simulator activity** from **unrelated Wazuh alerts** so that background events are not misattributed to the simulation.

## Validation / Results

### Confirmed by the supplied evidence

- Windows 11 Pro is visible in the environment evidence.
- Python 3.14.7 is visible.
- Sysmon service/configuration evidence is present.
- Wazuh Agent `001` is shown as Active.
- The simulator completed and reported that no encryption/destructive action occurred.
- The post-simulation directory contains the synthetic `.locked` files and simulated ransom note.
- Wazuh telemetry shows file activity for the lab path, including rules **553** and **554**.
- Alert-detail evidence shows rule **553** for a file-deletion event in the lab path.

### Not proven by the supplied evidence

- A successful match of custom rules `100100` / `100101`.
- A ransomware-specific Wazuh rule firing.
- Sysmon Event ID 1 for the simulator itself.
- Encryption or destructive ransomware behavior.
- A validated MITRE ATT&CK ransomware technique.
- A complete raw-event export or simulator execution log.

The final conclusion is therefore: **the lab execution and telemetry collection are evidenced; ransomware-specific custom detection is not conclusively validated by the supplied screenshots.**

## Evidence / Screenshots

All captured screenshots are retained under [`screenshots/`](screenshots/), grouped by phase. Each folder contains a short evidence README.

| Evidence | What it covers |
|---|---|
| SS-01–03 | Environment and Python |
| SS-04–06 | Sysmon |
| SS-07–09 | Wazuh agent and dashboard visibility |
| SS-10–11 | Baseline |
| SS-12–13 | Simulator execution and resulting files |
| SS-14–15 | Wazuh telemetry |
| SS-16–18 | Detection/alert evidence |
| SS-19 | Investigation/correlation |
| SS-20 | Final dashboard validation |

See [`docs/evidence-collection.md`](docs/evidence-collection.md) for the evidence interpretation.

## Project Structure

```text
architecture/       Architecture documentation and diagram
detection/          Detection logic, matrix and validation
docs/               Setup, evidence, troubleshooting and lessons learned
evidence/           Sanitized lab evidence summaries
incident-response/  Response playbook
investigation/      Triage, timeline and indicator records
mitre/              ATT&CK assessment
reports/            Final lab incident report
screenshots/        SS-01 through SS-20
simulator/          Harmless ransomware-behavior simulator
sysmon/             Sysmon configuration and notes
wazuh/              Wazuh rules and decoder notes
```

## Limitations

This is a **controlled lab**, not a production ransomware detection package. The captured evidence is screenshot-based, and some Wazuh alerts visible during the run are unrelated background events. File activity alone is not proof of ransomware, and the simulator deliberately performs no encryption.

## Safety and Scope

Run the simulator only against the configured synthetic directory:

`C:\RansomwareLab\TestData`

Review [`simulator/ransomware_simulator.py`](simulator/ransomware_simulator.py) before execution.

## License

MIT
