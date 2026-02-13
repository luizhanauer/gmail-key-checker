import smtplib
from email.message import EmailMessage
from datetime import datetime

GREEN = "\033[1;32m"
RESET = "\033[0m"

def run_checker():
    print(f"{GREEN}>>> GMAIL SMTP CHECKER LOCAL <<<{RESET}\n")

    # Coleta de dados (Placeholder manual para teste rápido)
    seu_email = input("E-mail Gmail: ").strip()
    senha_app = input("Senha de App (16 dígitos): ").strip().replace(" ", "")
    destinatario = input("Enviar para: ").strip()

    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Montagem da mensagem
    msg = EmailMessage()
    msg['Subject'] = f"Teste Local SMTP - {agora}"
    msg['From'] = seu_email
    msg['To'] = destinatario
    msg.set_content(f"Enviado do terminal Ubuntu às {agora}")

    try:
        print(f"\n[{agora}] 🔄 Conectando ao smtp.gmail.com...")
        
        # Conexão segura porta 465
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(seu_email, senha_app)
            smtp.send_message(msg)
            
        print(f"{GREEN}[{agora}] ✅ SUCESSO: E-mail enviado para {destinatario}{RESET}")

    except Exception as e:
        print(f"\n❌ ERRO NA CONEXÃO:")
        print(f"Detalhes: {e}")

if __name__ == "__main__":
    run_checker()