"""NOCTE – genereert de 3 MailerLite-e-mails (HTML) uit één template.

Copy komt uit 03_assets/ai/NOCTE_copy_v01.md. Merge tags zijn MailerLite-tags:
{$name} = voornaam, {$unsubscribe} = uitschrijflink, {$url} = webversie.
Gebruik: python3 NOCTE_mail_generator_v01.py  -> schrijft NOCTE_mail_0X_*.html
"""
from pathlib import Path

IMG = "https://raw.githubusercontent.com/syldevos2004-cell/creativeautomation-nocte/claude/project-thread-l0aa7r/mailerlite/img/"
SITE = "https://syldevos2004-cell.github.io/creativeautomation-nocte/"

C = dict(nacht="#160C22", violet="#3B1D52", pink="#EE92C2", mauve="#9D6A89",
         olive="#998648", creme="#F7F0EC")

MAILS = [
    dict(file="NOCTE_mail_01_welkom", img="NOCTE_mail_01_welkom.jpg",
         subject="Welkom in de nacht, {$name} 🖤", preheader="Je Night Pass is klaar.",
         label="Night Pass · welkom", h1="WELKOM IN", h1_thin="de nacht.",
         body=["Hey {$name},",
               "Je staat op de lijst. Vanaf nu ben je een van de eersten die NOCTE mag dragen: een zoete, intense geur voor wie pas om middernacht begint.",
               "Je Night Pass geeft je drie dingen:"],
         perks=["Een gratis sample", "Een plek op de gastenlijst van de launch party", "Early access bij de lancering"],
         after="Claim je sample nu, voor ze op zijn.",
         cta="Claim mijn sample", href=SITE + "#nightpass", sign="Tot vanavond,"),
    dict(file="NOCTE_mail_02_nightpass", img="NOCTE_mail_02_nightpass.jpg",
         subject="Je sample is onderweg. Dit is pas het begin.", preheader="Zo draag je NOCTE de hele nacht.",
         label="Night Pass · scenario A", h1="DIT IS PAS", h1_thin="het begin.",
         body=["{$name}, je sample is geclaimd. Nu het belangrijkste: hoe je hem draagt.",
               "Spray op je pols, in je nek en één keer in je haar. Daar blijft de geur het langst hangen en daar komen ze het dichtst bij.",
               "En hou je agenda vrij: als Night Pass-houder sta je op de gastenlijst van de launch party. De datum krijg je als eerste."],
         perks=[], after="",
         cta="Bekijk de vier geuren", href=SITE, sign="Draag de nacht,"),
    dict(file="NOCTE_mail_03_reminder", img="NOCTE_mail_03_reminder.jpg",
         subject="{$name}, je sample wacht nog op je", preheader="Nog maar een paar Night Passes over.",
         label="Night Pass · scenario B", h1="JE SAMPLE", h1_thin="wacht nog.",
         body=["Je schreef je in, maar je sample staat nog klaar. Zonde, want deze nacht is voor jou gemaakt.",
               "Eén klik en we sturen hem op. Daarbij krijg je ook je plek op de gastenlijst van de launch party."],
         perks=[], after="",
         cta="Ja, stuur mijn sample", href=SITE + "#nightpass", sign="We houden een plek vrij,"),
]

FONT = "'Bricolage Grotesque', Helvetica, Arial, sans-serif"


def render(m):
    p = "".join(f'<p style="margin:0 0 16px;font:300 17px/1.6 {FONT};color:{C["creme"]};">{t}</p>' for t in m["body"])
    perks = ""
    if m["perks"]:
        rows = "".join(
            f'<tr><td style="padding:10px 0;border-top:1px solid {C["violet"]};font:600 13px/1.4 {FONT};'
            f'letter-spacing:2px;text-transform:uppercase;color:{C["pink"]};">0{i+1}&nbsp;&nbsp;'
            f'<span style="color:{C["creme"]};">{t}</span></td></tr>' for i, t in enumerate(m["perks"]))
        perks = f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin:0 0 20px;">{rows}</table>'
    after = f'<p style="margin:0 0 28px;font:300 17px/1.6 {FONT};color:{C["creme"]};">{m["after"]}</p>' if m["after"] else '<div style="height:12px"></div>'
    return f"""<!doctype html>
<html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{m['subject']}</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&display=swap" rel="stylesheet">
</head>
<body style="margin:0;padding:0;background:{C['nacht']};">
<div style="display:none;max-height:0;overflow:hidden;">{m['preheader']}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{C['nacht']};">
<tr><td align="center" style="padding:24px 12px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:100%;max-width:600px;background:{C['nacht']};">
  <tr><td style="padding:8px 32px 20px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
      <td style="font:600 15px/1 {FONT};letter-spacing:7px;color:{C['olive']};">NOCTE</td>
      <td align="right" style="font:300 12px/1 {FONT};color:{C['mauve']};"><a href="{{$url}}" style="color:{C['mauve']};">Webversie</a></td>
    </tr></table>
  </td></tr>
  <tr><td><img src="{IMG}{m['img']}" width="600" alt="NOCTE-fles op de dansvloer" style="display:block;width:100%;max-width:600px;height:auto;border:0;"></td></tr>
  <tr><td style="height:4px;background:{C['pink']};line-height:4px;font-size:0;">&nbsp;</td></tr>
  <tr><td style="padding:40px 32px 8px;">
    <p style="margin:0 0 18px;font:600 11px/1 {FONT};letter-spacing:4px;text-transform:uppercase;color:{C['olive']};">{m['label']}</p>
    <h1 style="margin:0 0 28px;font:800 48px/0.95 {FONT};letter-spacing:-0.5px;color:{C['creme']};">{m['h1']}<br><span style="font-weight:200;color:{C['pink']};">{m['h1_thin']}</span></h1>
    {p}{perks}{after}
    <table role="presentation" cellpadding="0" cellspacing="0"><tr><td style="border-radius:99px;background:{C['pink']};">
      <a href="{m['href']}" style="display:inline-block;padding:18px 32px;font:600 13px/1 {FONT};letter-spacing:3px;text-transform:uppercase;color:{C['nacht']};text-decoration:none;">{m['cta']}</a>
    </td></tr></table>
    <p style="margin:36px 0 0;font:300 17px/1.5 {FONT};color:{C['creme']};">{m['sign']}<br><strong style="font-weight:800;letter-spacing:4px;">NOCTE</strong></p>
  </td></tr>
  <tr><td style="padding:40px 32px 24px;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td style="border-top:1px solid {C['violet']};padding-top:20px;font:300 12px/1.6 {FONT};color:{C['mauve']};">
      Je krijgt deze mail omdat je je aanmeldde voor de NOCTE Night Pass en toestemming gaf om e-mails te ontvangen.
      We gebruiken je naam en e-mailadres alleen voor NOCTE-mails. <a href="{{$unsubscribe}}" style="color:{C['pink']};">Uitschrijven</a> kan altijd met één klik.<br><br>
      NOCTE · Draag de nacht. · Fictief merk, schoolproject Artevelde Hogeschool.
    </td></tr></table>
  </td></tr>
</table>
</td></tr></table>
</body></html>
"""


if __name__ == "__main__":
    out = Path(__file__).parent
    for m in MAILS:
        (out / f"{m['file']}.html").write_text(render(m), encoding="utf-8")
        print("ok", m["file"], "|", m["subject"])
