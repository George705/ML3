# datascrub-cli

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Build](https://github.com/George705/ML3/actions/workflows/ci.yml/badge.svg)](https://github.com/George705/ML3/actions)
[![Python](https://img.shields.io/badge/python-3.9%2B-brightgreen)]()
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)]()

A lightweight open-source tool that scans CSV files for common personal data (emails, phone numbers, US SSNs) and masks them automatically.  
Useful for students, educators, and researchers sharing datasets safely.

---

## 🚀 Features
- Detects and masks:
  - Email addresses → `john@example.com` → `j***@example.com`
  - US phone numbers → `(***)-***-****`
  - US Social Security Numbers → `***-**-****`
- Command-line and Python API interface
- Works entirely offline
- Open source and non-commercial
- Minimal dependencies, cross-platform

---

## 🧩 Installation
Clone the repo and install locally:

```bash
git clone https://github.com/George705/ML3.git
cd ML3
pip install -e .
```

---

## 🧪 Usage

### CLI
```bash
datascrub scan sample.csv --out sanitized.csv
```

Dry-run mode (preview without writing):
```bash
datascrub scan sample.csv --dry-run
```

### Python API
```python
from datascrub.patterns import mask_all

text = "Contact: jane@example.com or 415-555-1212"
print(mask_all(text))
# -> Contact: j***@example.com or (***)-***-****
```

---

## 🧰 Development
Set up a local environment for contributing:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ".[dev]"
pytest -q
```

---

## 🤝 Contributing
Contributions are welcome!  
Please see [CONTRIBUTING.md](CONTRIBUTING.md) and follow the simple pull request steps.  
Before submitting a PR:
- Keep commits focused and descriptive  
- Add or update tests if needed  
- Update the README or docs for user-facing changes  

---

## 🔒 Security
If you discover a vulnerability, **do not open a public issue**.  
Contact the maintainers listed in [MAINTAINERS.md](MAINTAINERS.md).  
We recommend using 1Password or Bitwarden to manage project credentials securely.

---

## 🪪 License
This project is licensed under the [MIT License](LICENSE).

---

## 👥 Maintainers
| Name | Role | Contact |
|------|------|----------|
| George + Team| Project maintainer | [@George705](https://github.com/George705) |

---

## 📜 Acknowledgements
Created to support open-source education and safe data sharing.

---

## 🌍 Project Links
- Repository: [https://github.com/George705/ML3](https://github.com/George705/ML3)
- License: [MIT](LICENSE)
- Continuous Integration: [GitHub Actions](https://github.com/George705/ML3/actions)
