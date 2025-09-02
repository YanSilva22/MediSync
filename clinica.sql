Create database clinica;
use clinica;

create table medicos (
	id int auto_increment primary key,
    nome varchar(50),
    email varchar(50),
    tel varchar(11),
    crm varchar(8),
    d_nasc date,
    cpf varchar(11)
    );
    
create table pacientes (
	id int auto_increment primary key,
    nome varchar(50),
    data_nascimento date,
    telefone varchar(11),
	email varchar(50),
	cpf varchar(11)
	);
     
create table consultas (
	id int auto_increment primary key,
    medico_id int,
    paciente_id int,
    data date,
    horario time,
    descricao varchar(150),
    val_cons decimal(5,2),
    foreign key (medico_id) references medicos(ID),
    foreign key (paciente_id) references pacientes(ID)
    );

select * from consultas;
select * from medicos;
select * from pacientes;
