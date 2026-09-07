# Ransomware Detection & Incident Response Lab

> **A controlled Windows SOC / Blue Team laboratory demonstrating safe ransomware-like behavior simulation, endpoint telemetry collection, Wazuh monitoring, alert investigation, incident response, and evidence-based detection validation.**

![Windows](https://img.shields.io/badge/Platform-Windows%2011-blue)
![Python](https://img.shields.io/badge/Python-3.14-yellow)
![Sysmon](https://img.shields.io/badge/Telemetry-Sysmon-red)
![Wazuh](https://img.shields.io/badge/SIEM-Wazuh-00A98F)
![MITRE ATT&CK](https://img.shields.io/badge/Framework-MITRE%20ATT%26CK-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

This project is an end-to-end **ransomware detection and incident-response laboratory** built around an isolated Windows endpoint and a Wazuh monitoring environment.

Instead of using real ransomware, the lab uses a **harmless Python simulator** to generate controlled ransomware-like file activity. Sysmon and Wazuh are then used to observe the resulting telemetry, investigate suspicious activity, preserve evidence, and validate detection conclusions.

The project follows a SOC-style lifecycle:

```text
┌──────────────────────┐
│ Safe Python Simulator│
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Windows Test Endpoint│
│ C:\RansomwareLab\... │
└──────────┬───────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐  ┌─────────────┐
│  Sysmon │  │ File System │
│Telemetry│  │   Activity  │
└────┬────┘  └──────┬──────┘
     │              │
     └──────┬───────┘
            ▼
    ┌───────────────┐
    │  Wazuh Agent  │
    └───────┬───────┘
            │
            ▼
    ┌──────────────────┐
    │ Wazuh Manager &  │
    │    Dashboard     │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │ Detection / FIM  │
    │      Alerts      │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │ SOC Investigation│
    └────────┬─────────┘
             │
       ┌─────┼─────┐
       ▼     ▼     ▼
   Timeline IOCs Validation
```

For the visual architecture, see [`architecture/architecture.png`](architecture/architecture.png).

---

## Objectives

The laboratory was designed to demonstrate five core defensive capabilities:

1. Generate controlled ransomware-like behavior in a dedicated test directory.
2. Collect endpoint telemetry using Sysmon and Wazuh.
3. Investigate file activity and associated security alerts.
4. Preserve technical evidence in a structured repository.
5. Validate detection claims against the evidence actually captured.

> **Core principle:** Evidence comes before conclusions.

---

## Safety & Ethical Scope

> **This repository does not contain real ransomware.**

The simulator is intentionally designed for cybersecurity training. It:

- Creates synthetic test documents
- Renames files to `.locked`
- Creates `SIMULATED_RANSOM_NOTE.txt`
- Operates inside the designated laboratory directory

It does **not**:

- Encrypt real data
- Delete real user files
- Establish persistence
- Steal credentials
- Disable security controls
- Evade detection
- Propagate across a network
- Perform destructive actions

The simulator should only be executed in an isolated, authorized laboratory environment.

Configured test directory:

```text
C:\RansomwareLab\TestData
```

Review [`simulator/ransomware_simulator.py`](simulator/ransomware_simulator.py) before execution.

---

# Architecture

The detection pipeline is intentionally designed to show how endpoint activity travels through a defensive monitoring stack:

```text
                    ┌─────────────────────┐
                    │  Python Simulator   │
                    │ Safe Synthetic Test │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Windows Test Data   │
                    │ C:\RansomwareLab\   │
                    │       TestData      │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │     Sysmon      │        │  File Activity  │
        │ Endpoint Events │        │  / FIM Changes  │
        └────────┬────────┘        └────────┬────────┘
                 │                          │
                 └─────────────┬────────────┘
                               ▼
                    ┌─────────────────────┐
                    │    Wazuh Agent     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Wazuh Manager     │
                    │    + Dashboard     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Detection & Alert   │
                    │      Analysis       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ SOC Investigation   │
                    │                     │
                    │ Timeline → IOCs     │
                    │ Triage → Validation │
                    └─────────────────────┘
```

---

# Technology Stack

| Technology | Role |
|---|---|
| **Windows 11 Pro** | Monitored endpoint |
| **Python 3.14.7** | Safe ransomware-like behavior simulator |
| **Sysmon 15.21** | Endpoint process and file telemetry |
| **Wazuh Agent** | Endpoint telemetry collection |
| **Wazuh Manager** | Event processing and security monitoring |
| **Wazuh Dashboard** | Alert visualization and investigation |
| **MITRE ATT&CK** | Behavioral assessment framework |
| **Git / GitHub** | Version control and project delivery |

---

# Laboratory Workflow

## 01 — Environment Preparation

The endpoint and monitoring components are verified before testing.

Evidence includes:

- Windows system information
- Hostname and network information
- Python version
- Sysmon service
- Sysmon configuration
- Wazuh Agent status

Evidence:

[`screenshots/01-environment/`](screenshots/01-environment/)  
[`screenshots/02-sysmon/`](screenshots/02-sysmon/)  
[`screenshots/03-wazuh/`](screenshots/03-wazuh/)

---

## 02 — Baseline

A clean state is captured before the simulator runs.

This establishes a reference point for comparing activity before and after the controlled simulation.

Evidence:

[`screenshots/04-baseline/`](screenshots/04-baseline/)

---

## 03 — Controlled Simulation

The simulator generates synthetic ransomware-like activity:

```text
30 Synthetic Documents
          │
          ▼
 Controlled Rename Operations
          │
          ▼
     .locked Files
          │
          ▼
SIMULATED_RANSOM_NOTE.txt
```

Evidence:

[`screenshots/05-simulation/`](screenshots/05-simulation/)

---

## 04 — Telemetry Collection

The resulting activity is examined through endpoint and Wazuh telemetry.

The analysis focuses on:

- Process activity
- File activity
- File-integrity events
- Relevant Wazuh alerts
- Event relationships
- Activity within the designated laboratory path

Evidence:

[`screenshots/06-telemetry/`](screenshots/06-telemetry/)

---

## 05 — Detection & Alert Analysis

The project evaluates whether observed activity provides sufficient evidence for a ransomware-related detection.

Detection engineering material:

```text
detection/
├── detection-logic.md
├── detection-matrix.md
└── validation-tests.md
```

Evidence:

[`screenshots/07-detection/`](screenshots/07-detection/)

---

## 06 — Investigation

The investigation separates:

**Simulator-generated activity**

from

**Unrelated background security events**

This prevents unrelated alerts from being incorrectly attributed to the simulated incident.

Investigation material:

```text
investigation/
├── incident-timeline.md
├── ioc.md
└── triage.md
```

Evidence:

[`screenshots/08-investigation/`](screenshots/08-investigation/)

---

## 07 — Incident Response

A SOC-style response workflow is documented in:

[`incident-response/response-playbook.md`](incident-response/response-playbook.md)

The playbook covers:

- Initial triage
- Scope assessment
- Evidence preservation
- IOC review
- Containment considerations
- Recovery considerations
- Post-incident validation

---

## 08 — MITRE ATT&CK Assessment

Observed behaviors are reviewed against the MITRE ATT&CK framework.

The mapping is intentionally evidence-based:

```text
Observed Behavior
       │
       ▼
Behavioral Interpretation
       │
       ▼
Potential ATT&CK Mapping
       │
       ▼
Evidence Review
       │
       ▼
Validated / Not Validated
```

See:

[`mitre/attack-mapping.md`](mitre/attack-mapping.md)

---

# Detection Methodology

The project uses a **behavior-oriented detection model** rather than treating a single filename or extension as proof of ransomware.

The simulator generates three primary synthetic signals:

```text
┌───────────────────────────┐
│ 30 Synthetic Documents    │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ Rename → .locked          │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ Simulated Ransom Note     │
│ SIMULATED_RANSOM_NOTE.txt │
└───────────────────────────┘
```

These signals are analyzed alongside endpoint and Wazuh telemetry.

### Why correlation matters

A `.locked` extension alone does not prove ransomware.

Similarly, a file-integrity alert does not automatically establish malicious activity.

A stronger detection requires contextual correlation across:

- Process execution
- File creation/modification/rename activity
- Affected paths
- Timing
- Alert context
- Supporting indicators

---

# Validation Results

## Confirmed by the captured evidence

The available evidence confirms:

- Windows 11 Pro was used as the laboratory endpoint.
- Python 3.14.7 was available.
- Sysmon service and configuration evidence was captured.
- Wazuh Agent `001` was shown as active.
- The safe simulator completed without encryption or destructive behavior.
- Synthetic `.locked` files and the simulated ransom note were created.
- Wazuh telemetry captured file activity associated with the laboratory path.
- Wazuh rules `553` and `554` appear within captured telemetry.
- Alert-detail evidence shows rule `553` associated with a file-deletion event in the laboratory path.

## Not conclusively proven by the supplied evidence

The captured screenshots do **not** conclusively demonstrate:

- Successful triggering of custom rules `100100` / `100101`
- A ransomware-specific Wazuh rule firing
- Sysmon Event ID 1 specifically identifying the simulator
- Real encryption
- Destructive ransomware behavior
- A validated MITRE ATT&CK ransomware technique
- A complete raw-event export
- A complete simulator execution log

### Final assessment

> **The laboratory execution and telemetry collection are evidenced; ransomware-specific custom detection is not conclusively validated by the supplied screenshots.**

This limitation is deliberately documented because reliable SOC analysis requires conclusions to remain within the boundaries of the available evidence.

---

# Evidence Collection

The repository contains evidence from the complete testing lifecycle:

| Phase | Evidence |
|---|---|
| Environment | SS-01 – SS-03 |
| Sysmon | SS-04 – SS-06 |
| Wazuh | SS-07 – SS-09 |
| Baseline | SS-10 – SS-11 |
| Simulation | SS-12 – SS-13 |
| Telemetry | SS-14 – SS-15 |
| Detection | SS-16 – SS-18 |
| Investigation | SS-19 |
| Validation | SS-20 |

All screenshots are organized under:

```text
screenshots/
```

Supporting evidence summaries are maintained under:

```text
evidence/
```

See [`docs/evidence-collection.md`](docs/evidence-collection.md).

---

# Repository Structure

```text
ransomware-detection-lab/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── architecture/
│   ├── README.md
│   └── architecture.png
│
├── detection/
│   ├── detection-logic.md
│   ├── detection-matrix.md
│   └── validation-tests.md
│
├── docs/
│   ├── evidence-collection.md
│   ├── lessons-learned.md
│   ├── setup-guide.md
│   └── troubleshooting.md
│
├── evidence/
│   ├── iocs/
│   ├── simulator/
│   ├── sysmon/
│   ├── timeline/
│   ├── validation/
│   └── README.md
│
├── incident-response/
│   └── response-playbook.md
│
├── investigation/
│   ├── incident-timeline.md
│   ├── ioc.md
│   └── triage.md
│
├── mitre/
│   └── attack-mapping.md
│
├── reports/
│   └── incident-report.md
│
├── screenshots/
│   ├── 01-environment/
│   ├── 02-sysmon/
│   ├── 03-wazuh/
│   ├── 04-baseline/
│   ├── 05-simulation/
│   ├── 06-telemetry/
│   ├── 07-detection/
│   ├── 08-investigation/
│   └── 09-validation/
│
├── simulator/
│   ├── README.md
│   ├── config.json
│   ├── ransomware_simulator.py
│   └── requirements.txt
│
├── sysmon/
│   ├── README.md
│   └── sysmon-config.xml
│
└── wazuh/
    ├── README.md
    ├── decoders/
    └── rules/
```

---

# Documentation Map

| Directory | Purpose |
|---|---|
| `architecture/` | Architecture and data-flow documentation |
| `detection/` | Detection logic, matrix and validation |
| `docs/` | Setup, troubleshooting, evidence and lessons learned |
| `evidence/` | Sanitized investigation evidence |
| `incident-response/` | Incident-response playbook |
| `investigation/` | Triage, timeline and IOC analysis |
| `mitre/` | ATT&CK behavior assessment |
| `reports/` | Final incident report |
| `screenshots/` | SS-01 through SS-20 |
| `simulator/` | Safe ransomware-like behavior simulator |
| `sysmon/` | Sysmon configuration and documentation |
| `wazuh/` | Wazuh rules and decoder material |

---

# Setup

For complete installation and configuration instructions, see:

[`docs/setup-guide.md`](docs/setup-guide.md)

Troubleshooting guidance:

[`docs/troubleshooting.md`](docs/troubleshooting.md)

Simulator documentation:

[`simulator/README.md`](simulator/README.md)

Sysmon documentation:

[`sysmon/README.md`](sysmon/README.md)

Wazuh documentation:

[`wazuh/README.md`](wazuh/README.md)

---

# Lessons Learned

This laboratory reinforced several important Blue Team principles:

### Detection ≠ Alert

Generating an alert does not automatically prove that the intended detection logic worked.

### Baselines Matter

A clean baseline provides context for identifying changes introduced during testing.

### File Activity Requires Context

Creation, modification, deletion and rename events can all occur legitimately. Detection should consider surrounding behavior.

### Evidence Must Drive Conclusions

A professional investigation distinguishes between:

```text
Observed
   ↓
Supported
   ↓
Validated
```

rather than:

```text
Alert
   ↓
Attack
```

### Safe Simulation Enables Repeatable Testing

Controlled simulations allow detection engineering and investigation workflows to be tested without deploying real malware.

---

# Limitations

This project is a **controlled training laboratory**, not a production ransomware-detection platform.

Current limitations include:

- The simulator does not perform real encryption.
- Evidence is primarily screenshot-based.
- Some Wazuh alerts observed during testing were unrelated background activity.
- File-integrity activity alone cannot establish ransomware attribution.
- The captured screenshots do not conclusively validate the custom ransomware-specific rules.
- Raw event exports and complete execution logs are not included as validated evidence.

These limitations are explicitly documented to maintain evidence integrity.

---

# Future Improvements

Potential future iterations include:

- Structured raw-event exports
- Improved process-to-file correlation
- Additional Sysmon telemetry
- More advanced behavioral detection logic
- Automated detection validation
- Additional Wazuh decoders and rules
- False-positive testing
- Automated incident timelines
- Automated evidence collection
- Expanded ATT&CK mapping
- Controlled multi-stage attack simulations

---

# Portfolio Skills Demonstrated

This project demonstrates hands-on exposure to:

### SOC Operations
- Endpoint monitoring
- Alert analysis
- Security telemetry
- Evidence collection
- Incident triage

### Detection Engineering
- Behavioral detection concepts
- Wazuh rules
- Sysmon telemetry
- Detection validation
- False-positive awareness

### Incident Response
- Timeline construction
- IOC identification
- Evidence preservation
- Investigation
- Response planning

### Security Frameworks
- MITRE ATT&CK
- Evidence-based analysis
- Defensive security methodology

---

# Conclusion

This laboratory demonstrates how a SOC analyst can move from **controlled endpoint activity to telemetry, detection, investigation, incident response, and final validation**.

The project intentionally goes beyond simply displaying an alert.

It asks:

> **What happened?**

> **What evidence supports it?**

> **What does the evidence not prove?**

> **Was the intended detection actually validated?**

That evidence-driven approach is central to reliable SOC operations and detection engineering.

---

## License

This project is licensed under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

## Author

**Mahrukh**

BS Cyber Security  
SOC / Blue Team • Detection Engineering • Incident Response

---

> **Disclaimer:** This project was developed strictly for authorized cybersecurity education and isolated laboratory testing. No real ransomware or destructive malware is included.
