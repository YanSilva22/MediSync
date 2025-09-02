import mysql.connector

class DBConnection:
    
    #__init__ para que sempre a classe for chamada execulte o comando de conexão 
    def __init__(self, currentHost, us, passw):
        #salvar dados do ususario 
        self.currentHost = currentHost
        self.user = us
        self.password = passw 
          
    def connectionMade(self):
        #variaveis de conexão 
        self.connection = self.conectar_bd()
        self.cursor = self.connection.cursor()
                
    # Conectar ao banco de dados
    def conectar_bd(self):
        try:
            return mysql.connector.connect(
                host= self.currentHost,
                user= self.user,
                password= self.password,
                database="clinica",
            )
            
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None

    # Função para adicionar um novo paciente
    def adicionar_paciente(self, entry_nome, entry_data_nascimento, entry_tel, entry_email, entry_cpf):
        nome = entry_nome
        data_nascimento = entry_data_nascimento
        telefone = entry_tel
        email = entry_email
        cpf = entry_cpf
        
        self.connectionMade()

        print("Adicionando paciente:", nome, data_nascimento, telefone, email, cpf)  # Debug info

        if self.connection is None:
            return False, "Deu ruim"

        try:
            self.cursor.execute("INSERT INTO pacientes (nome, data_nascimento, telefone, email, cpf) VALUES (%s, %s, %s, %s, %s)",
                        (nome, data_nascimento, telefone, email, cpf))
            self.connection.commit()
            return True, "Paciente adicionado com sucesso!"
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar paciente: {err}")  # Imprime o erro
            return False, f"Erro ao adicionar paciente: {err}"
        finally:
            self.connection.close()

    # Função para adicionar um novo médico       
    def adicionar_medico(self, entry_nome, entry_email, entry_tel, entry_crm, entry_data_nascimento, entry_cpf):
        nome = entry_nome
        email = entry_email
        telefone = entry_tel
        crm = entry_crm
        data_nascimento = entry_data_nascimento
        cpf = entry_cpf

        self.connectionMade()
        
        print("Adicionando medico:", nome, email, telefone, crm, data_nascimento, cpf)  # Debug info

        if self.connection is None:
            return False, "Deu ruim"

        try:
            self.cursor.execute("INSERT INTO medicos (nome, email, tel, crm, d_nasc, cpf) VALUES (%s, %s, %s, %s, %s, %s)",
                        (nome, email, telefone, crm, data_nascimento, cpf))
            self.connection.commit()
            return True, "Medico adicionado com sucesso!"
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar medico: {err}")  # Imprime o erro
            return False, f"Erro ao adicionar medico: {err}"
        finally:
            self.connection.close()

    # Função para agendar uma nova consulta
    def agendar_consulta(self, entry_paciente_id, entry_medico_id, entry_data, entry_horario, entry_descricao, entry_val):
        paciente_id = entry_paciente_id
        medico_id = entry_medico_id
        data = entry_data
        horario = entry_horario
        descricao = entry_descricao
        valor = entry_val
        
        self.connectionMade()

        print("Tentando adicionando nova consulta")  # Debug info

        if self.connection is None:
            return False

        try:
            self.cursor.execute("SELECT COUNT(horario) FROM consultas WHERE (horario = %s AND data = %s AND medico_id = %s)", 
                        (horario, data, medico_id))
            timeCheck = self.cursor.fetchone()[0]
            if (timeCheck > 0):
                return False, "Este horario já esta agendado!"
            else:
                self.cursor.execute("INSERT INTO consultas (paciente_id, medico_id, data, horario, descricao, val_cons) VALUES (%s, %s, %s, %s, %s, %s)",
                            (paciente_id, medico_id, data, horario, descricao, valor))
                self.connection.commit()
                return True, "Consulta agendada com sucesso!"
        except mysql.connector.Error as err:
            print(f"Erro ao agendar consulta: {err}")  # Imprime o erro
            return None, f"Erro ao agendar consulta: {err}"
        finally:
            self.connection.close()

    # Função para visualizar a lista de pacientes
    def visualizar_pacientes(self):
        self.connectionMade()
        
        if self.connection is None:
            return False

        try:
            self.cursor.execute("SELECT id, nome, email, telefone, cpf, data_nascimento FROM pacientes")
            pacientes = self.cursor.fetchall()
            return pacientes
        except mysql.connector.Error as err:
            print(f"Erro ao buscar pacientes: {err}")
            return False,  f"Erro ao buscar pacientes: {err}"
        finally:
            self.connection.close()

    # Função para visualizar a lista de medicos
    def visualizar_medicos(self):
        self.connectionMade()
        
        if self.connection is None:
            return False

        try:
            self.cursor.execute("SELECT id, nome, email, tel, crm, d_nasc, cpf FROM medicos")
            medicos = self.cursor.fetchall()
            return medicos
        except mysql.connector.Error as err:
            print(f"Erro ao buscar ,edicos: {err}")
            return None, f"Erro ao buscar medicos: {err}"
        finally:
            self.connection.close()
            
    # Função para visualizar a agenda de consultas
    def visualizar_agenda(self):
        self.connectionMade()
        
        if self.connection is None:
            return False

        try:
            self.cursor.execute(""" 
                SELECT consultas.id, medicos.nome AS medico, pacientes.nome AS paciente, consultas.val_cons, consultas.descricao, consultas.data, consultas.horario, consultas.val_cons
                FROM consultas 
                JOIN pacientes ON consultas.paciente_id = pacientes.id 
                JOIN medicos ON consultas.medico_id = medicos.id
                ORDER BY consultas.data ASC, consultas.horario ASC;
            """)
            consultas = self.cursor.fetchall()
            return consultas
        except mysql.connector.Error as err:
            print(f"Erro ao buscar agenda: {err}")
            return None, f"Erro ao buscar agenda: {err}"
        finally:
            self.connection.close()

    #Função de remoção de linhas na tabela pacientes
    def removedor_pacientes(self, aux, checkOpc):
        self.connectionMade()
        
        if self.connection is None:
            return False
        
        try:
            if (checkOpc):
                self.cursor.execute("DELETE FROM pacientes WHERE id = %s", (aux,))
                self.connection.commit()
                print(f"Dados deletados! ID = {aux}")
                return True, "Dados deletados com exito!"
            else:
                print("Deleção cancelada pelo usuario")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar paciente: {err}")
            return False, f"Erro ao deletar paciente: {err}"
        finally:
            self.connection.close()

    #Função de remoção de linhas na tabela medicos
    def removedor_medicos(self, aux, checkOpc):
        self.connectionMade()
        
        if self.connection is None:
            return False
        
        try:
            if (checkOpc):
                self.cursor.execute("DELETE FROM medicos WHERE id = %s", (aux,))
                self.connection.commit()
                print(f"Dados deletados! ID = {aux}")
                return True, "Dados deletados com exito!"
            else:
                print("Deleção cancelada pelo usuario")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar medico: {err}")
            return False, f"Erro ao deletar o funcionario: {err}"
        finally:
            self.connection.close()
            
    #Função de remoção de linhas na tabela consultas
    def removedor_consultas(self, aux, checkOpc):
        self.connectionMade()
        
        if self.connection is None:
            return False
        
        try:
            if (checkOpc):
                self.cursor.execute("DELETE FROM consultas WHERE id = %s", (aux,))
                self.connection.commit()
                print(f"Dados deletados! ID = {aux}")
                return True, "Dados deletados com exito!"
            else:
                print("Deleção cancelada pelo usuario")
        except mysql.connector.Error as err:
            print(f"Erro ao deletar consulta: {err}")
            return False, f"Erro ao deletar consulta: {err}"
        finally:
            self.connection.close()
    

