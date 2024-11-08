from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def split_emails(email_str):
    regex_email = r"[^@]+@[^@]+\.[^@]+"
    email_list = [email.strip() for email in email_str.split(',')]
    valid_emails = [email for email in email_list if re.match(regex_email, email)]
    return valid_emails

@app.route('/enviar_email', methods=['POST'])
def enviar_email():
    remetente_nome = request.form['remetente_nome']
    remetente = request.form['remetente']
    senha = request.form['senha']
    destinatarios_str = request.form['destinatario_email']
    destinatarios = split_emails(destinatarios_str)
    titulo = request.form['titulo']
    corpo = request.form['corpo'].replace("\n", "<br>")

    if not destinatarios:
        return jsonify({"success": False, "message": "Endereço de e-mail inválido(s)."})

    smtpObj = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtpObj.ehlo()

    try:
        smtpObj.login(remetente, senha)

        html_content = render_template('email_template.html', titulo=titulo, corpo=corpo, remetente_nome=remetente_nome)
        mensagem = MIMEText(html_content, "html", "utf-8")
        mensagem["Subject"] = Header(titulo, "utf-8")
        mensagem["From"] = formataddr((str(Header(remetente_nome, "utf-8")), remetente))
        mensagem["To"] = ", ".join(destinatarios)

        smtpObj.sendmail(remetente, destinatarios, mensagem.as_string())
        smtpObj.quit()

        return jsonify({"success": True, "message": f"Email enviado com sucesso para: {', '.join(destinatarios)}"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
