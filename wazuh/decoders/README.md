# Wazuh Decoder Notes

No custom decoder is required or evidenced by the supplied screenshots.

The correct workflow is to inspect the actual decoded Sysmon/Wazuh event structure first. Add a narrowly scoped decoder only when a required field is genuinely absent from the default decoding path, then validate it in the isolated lab.

The final evidence does not claim a custom decoder was deployed.
