-- Tabela de avicultores
CREATE TABLE IF NOT EXISTS tb_avicultores(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    nascimento DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    caf VARCHAR(10) NOT NULL
);

-- Tabela de aviários
CREATE TABLE IF NOT EXISTS tb_aviario(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    capacidade INTEGER NOT NULL
);

-- Tabela de avícolas
CREATE TABLE IF NOT EXISTS tb_avicolas(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    cnpj TEXT NOT NULL UNIQUE,
    endereco TEXT
);

-- Tabela de galpões
CREATE TABLE IF NOT EXISTS tb_galpoes(
    id SERIAL PRIMARY KEY,
    identificador TEXT NOT NULL,
    area_m2 REAL
);