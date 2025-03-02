#!/bin/bash

# Ensure Semgrep is installed
if ! command -v semgrep &> /dev/null
then
    echo "⚠️ Semgrep is not installed! Installing..."
    pip install semgrep
fi

# Run Semgrep scan
semgrep scan --config=config/semgrep-rules.yml --json > semgrep_results.json

# Print results
cat semgrep_results.json
