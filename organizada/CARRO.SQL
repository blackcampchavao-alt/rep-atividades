CREATE TABLE cliente(
  cpf CHAR(11) PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  telefone VARCHAR(20)
);

CREATE TABLE carro(
placa CHAR(7) PRIMARY KEY,
cor VARCHAR(20),
modelo VARCHAR(50) NOT NULL,
cpf CHAR(11),
CONSTRAINT cpf FOREIGN KEY (cpf)
REFERENCES cliente(cpf)
);

CREATE TABLE acidente(
id SERIAL PRIMARY KEY,
data DATE NOT NULL,
local VARHCAR(250), NOT null
);

CREATE TABLE carro_acidente(
placa_carro CHAR(7),
id_acidente INT,
CONSTRAINT placa_acidente FOREING KEY (placa_carro)
REFERENCES carro(placa),
CONSTRAINT id_acidente FOREING KEY (id_carro)
REFERENCES acidente(id)
ON DELETE RESTRICT,
PRIMARY KEY (id_acidente), placa_carro
);

ALTER TABLE carro_acidente ADD PRIMARY KEY (id_acidente)




tudo junto erro na 25

CREATE TABLE cliente(
  cpf CHAR(11) PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  telefone VARCHAR(20)
);

CREATE TABLE carro(
placa CHAR(7) PRIMARY KEY,
cor VARCHAR(20),
modelo VARCHAR(50) NOT NULL,
cpf CHAR(11),
CONSTRAINT cpf FOREIGN KEY (cpf)
REFERENCES cliente(cpf)
);

CREATE TABLE acidente(
id SERIAL PRIMARY KEY,
data DATE NOT NULL,
local varchar(250) NOT null
);

CREATE TABLE carro_acidente (
    placa_carro CHAR(7),
    id_acidente INT,

    CONSTRAINT placa_acidente 
        FOREIGN KEY (placa_carro)
        REFERENCES carro(placa),

    CONSTRAINT fk_id_acidente 
        FOREIGN KEY (id_acidente)
        REFERENCES acidente(id)
        ON DELETE RESTRICT,

    PRIMARY KEY (placa_carro, id_acidente)
);