import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse


def send_test_email(smtp_server, smtp_port, smtp_user, smtp_password, to_address):
    subject = "SMTP Test"
    body = "Dies ist eine Test-E-Mail, um die SMTP-Verbindung zu überprüfen."

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = to_address
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.set_debuglevel(1)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_address, msg.as_string())
        server.quit()
        print(f"[INFO] Test-E-Mail erfolgreich an {to_address} gesendet.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"[ERROR] Authentifizierungsfehler: {e}")
    except smtplib.SMTPConnectError as e:
        print(f"[ERROR] Verbindungsfehler: {e}")
    except Exception as e:
        print(f"[ERROR] Allgemeiner Fehler beim Senden der E-Mail: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Testet die SMTP-Verbindung durch das Senden einer Test-E-Mail."
    )
    parser.add_argument("--smtp_server", required=True, help="SMTP-Server-Adresse")
    parser.add_argument(
        "--smtp_port", type=int, default=587, help="SMTP-Server-Port (Standard: 587)"
    )
    parser.add_argument("--smtp_user", required=True, help="SMTP-Benutzername")
    parser.add_argument("--smtp_password", required=True, help="SMTP-Passwort")
    parser.add_argument(
        "--to_address", required=True, help="E-Mail-Adresse des Empfängers"
    )

    args = parser.parse_args()
    send_test_email(
        args.smtp_server,
        args.smtp_port,
        args.smtp_user,
        args.smtp_password,
        args.to_address,
    )


if __name__ == "__main__":
    main()
