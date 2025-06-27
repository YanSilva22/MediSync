# 🩺 MediSync — Sistema de Gestão de Consultório Médico

**MediSync** é um sistema desktop desenvolvido em **Python** com **Tkinter** para auxiliar na gestão de um consultório médico.  
Ele permite **cadastrar médicos, pacientes, agendar consultas** e gerenciar tudo através de um banco de dados **MySQL**.


## 📌 **Descrição**

Este projeto foi desenvolvido como trabalho prático da disciplina de **Banco de Dados** no curso de **Engenharia de Computação (FHO)**.  
Ele demonstra na prática o uso de um **banco de dados relacional** com uma **interface gráfica amigável**, permitindo realizar operações CRUD completas.



## 🎯 **Funcionalidades**

✅ Cadastro de médicos  
✅ Cadastro de pacientes  
✅ Agendamento de consultas  
✅ Edição e exclusão de registros  
✅ Integração com banco de dados MySQL



## 🖼️ **Tela de Login SQL**

![Tela de Login](./icons/vizualização.png)

**Descrição:**  
A primeira tela que aparece ao abrir o MediSync é a **tela de login no SQL**.  
Nela você deve informar:

- **HOST:** Endereço do servidor MySQL (ex: `localhost`)
- **USER:** Nome de usuário do MySQL (ex: `root`)
- **SENHA:** Senha do seu banco de dados

Após preencher, clique no **ícone de disquete** para validar o login.  
Isso conecta o sistema ao banco de dados e libera as demais funcionalidades.



## ⚙️ **Tecnologias Utilizadas**

- **Python 3**
- **Tkinter** (Interface Gráfica)
- **MySQL** (Banco de dados)
- **MySQL Connector Python**
- **MySQL Workbench** (Modelagem MER)

---

## 📁 **Estrutura de Pastas**

```plaintext
MEDISYNC/
├── __pycache__/         Arquivos compilados do Python
├── build/               Diretório de build do projeto
├── esboços/             Esboços e rascunhos de código
├── icons/               Ícones da interface gráfica
├── app.py               Código principal da aplicação
├── app.spec             Configuração de build (PyInstaller)
├── clinica.sql          Script de criação do banco de dados
├── README.md            Documentação principal do projeto
└── SQLfunctions.py      Funções de conexão e operações SQL
```

