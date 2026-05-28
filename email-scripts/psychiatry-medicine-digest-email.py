#!/usr/bin/env python3
"""Send the daily psychiatry medicine digest via Gmail SMTP."""

from __future__ import annotations

import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


SENDER = "caslinjiao@gmail.com"
RECIPIENT = "caslinjiao@gmail.com"
SECRET_FILE = Path.home() / ".nursing-digest-gmail.secret"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def load_password() -> str:
    return SECRET_FILE.read_text(encoding="utf-8").strip().replace(" ", "")


def build_email(digest_path: Path, date: str) -> MIMEMultipart:
    body = digest_path.read_text(encoding="utf-8")
    lines = body.splitlines()
    preview_lines = [l for l in lines[:30] if l.strip()][:12]
    preview = "\n".join(preview_lines)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Psychiatrie-Medizin-Digest {date}"
    msg["From"] = SENDER
    msg["To"] = RECIPIENT

    plain = f"{preview}\n\n---\n\nVollständiger Digest:\n\n{body}"
    msg.attach(MIMEText(plain, "plain", "utf-8"))
    return msg


def send(digest_path: Path, date: str) -> None:
    password = load_password()
    msg = build_email(digest_path, date)
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER, password)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
    print(f"E-Mail gesendet: {SENDER} → {RECIPIENT}")


def main() -> int:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <digest_file> <date>", file=sys.stderr)
        return 1
    digest_path = Path(sys.argv[1])
    date = sys.argv[2]
    if not digest_path.exists():
        print(f"Digest-Datei nicht gefunden: {digest_path}", file=sys.stderr)
        return 1
    if not SECRET_FILE.exists():
        print(f"Kein App-Passwort unter {SECRET_FILE}", file=sys.stderr)
        return 1
    try:
        send(digest_path, date)
        return 0
    except Exception as exc:
        print(f"E-Mail fehlgeschlagen: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
