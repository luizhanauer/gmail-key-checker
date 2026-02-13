# 🟢 Gmail Key Checker

Laboratório Google Colab e script local para envio de e-mails via scripts usando **Senhas de App** do Gmail.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/luizhanauer/4f9b7c62a5ef6a64ce1e8bba93a28194/gmail_key_checker.ipynb)

Este projeto foi desenvolvido para facilitar a configuração e o teste de **Senhas de App** do Gmail.

---

## 🚀 Como conseguir uma chave (key) de **"Senhas de App"** do Gmail?

Para usar o Gmail em seus scripts, você não deve usar sua senha principal, mas sim uma **Senha de App**. 

Siga o fluxo abaixo para criar uma:

### 1. Preparação (Segurança)
Em [https://myaccount.google.com/security](https://myaccount.google.com/security) você deve habilitar a  **Verificação em Duas Etapas** na sua Conta Google.
![<security>](/img/security.png)

### 2. Gerar Chave (Key)
Em [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) por segurança você terá de fazer o login novamente em sua conta.

Posteriormente faça os passos a seguir, para gerar a sua chave:

#### Passo 1 - Nomear a sua chave

![<step-1>](/img/step-1.png)

#### Passo 2 - Gerar a chave e copiar

![<step-2>](/img/step-2.png)

#### Passo 3 - Validar a criação da chave

![<step-3>](/img/step-3.png)

### 3. Validação
Use o **Playground no Google Colab** para validar sua chave instantaneamente antes de implementá-la no seu código oficial.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/luizhanauer/4f9b7c62a5ef6a64ce1e8bba93a28194/gmail_key_checker.ipynb)

![<colab>](/img/colab.png)

Se desejar testar localmente você pode clonar o repositório [gmail-key-checker](https://github.com/luizhanauer/gmail-key-checker) e executar o script **checker.py**

Clonar o repositório:
```bash
git clone https://github.com/luizhanauer/gmail-key-checker.git
```
Acessar o diretório clonado:
```bash
cd gmail-key-checker
```
Executar o script:
```bash
uv run checker.py
```

Resultado esperado:
```bash
unk@desktop:~/gmail-key-checker$ uv run checker.py
>>> GMAIL KEY CHECKER - LOCAL <<<

E-mail Gmail: luizhanauer@gmail.com
Senha de App (16 dígitos): xxxx xxxx xxxx xxxx
Enviar para: luizhanauer@gmail.com

[13/02/2026 12:21:07] 🔄 Conectando ao smtp.gmail.com...
[13/02/2026 12:21:07] ✅ SUCESSO: E-mail enviado para luizhanauer@gmail.com
```

No e-mail:

![<email>](/img/email.png)