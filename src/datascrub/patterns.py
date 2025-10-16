import re

EMAIL_RE = re.compile(r"(?i)\b([A-Z0-9._%+-]+)@([A-Z0-9.-]+\.[A-Z]{2,})\b")
PHONE_RE = re.compile(r"\b(\+?1[-.\s]?)?(\(?\d{3}\)?)[-.\s]?\d{3}[-.\s]?\d{4}\b")
SSN_RE = re.compile(r"\b(\d{3})[- ]?(\d{2})[- ]?(\d{4})\b")

def mask_email(text: str) -> str:
    def _m(m):
        name, domain = m.group(1), m.group(2)
        masked = name[0] + "*" * max(len(name)-1, 0)
        return f"{masked}@{domain}"
    return EMAIL_RE.sub(_m, text)

def mask_phone(text: str) -> str:
    def _m(m):
        return "(***)-***-****"
    return PHONE_RE.sub(_m, text)

def mask_ssn(text: str) -> str:
    def _m(m):
        return "***-**-****"
    return SSN_RE.sub(_m, text)

def mask_all(text: str) -> str:
    text = mask_email(text)
    text = mask_phone(text)
    text = mask_ssn(text)
    return text
