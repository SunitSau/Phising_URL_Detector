# Phishing & Malicious URL Scanner

A lightweight, rule-based Python heuristic scanner designed to evaluate URLs for potential phishing, credential theft, and suspicious structural patterns.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SunitSau/Phising_URL_Detector/blob/main/Phising_URL_Detector.ipynb)

---

## Overview

Phishing websites often employ specific domain tricks to evade suspicion, mislead users, or obscure the actual host server. This tool analyzes input URLs across multiple structural parameters, assigns a risk score based on detected red flags, and classifies the target into one of three threat categories:

* **Safe:** No immediate heuristic red flags detected.
* **Suspicious:** Exhibits mild anomalies; proceed with caution.
* **High Risk:** Shows multiple strong indicators of phishing or malicious intent.

---

## Detection Heuristics

The scanner evaluates the following indicators:

* **Protocol Security:** Flags unencrypted `http://` connections.
* **Direct IP Usage:** Detects raw IPv4 addresses used instead of standard domain names.
* **Host Obfuscation:** Identifies `@` symbols commonly used to trick browsers into routing to malicious sub-hosts.
* **Lookalike Domains:** Flags hyphenation (`-`) inside the core domain, a common tactic for spoofing established brand names.
* **Deceptive Keywords:** Scans for high-urgency bait terms often found in credential-harvesting paths (e.g., `verify`, `secure`, `bank`, `claim`, `update`).

---
