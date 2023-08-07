CREATE TABLE jugadores (
    id int NOT NULL AUTO_INCREMENT,
    nombre varchar(50) NOT NULL,
    estrellas int NOT NULL,
    copasAmerica int NOT NULL,
    copasEuro int NOT NULL,
    copasMundial int NOT NULL,
    foto varchar(225) NOT NULL,
    PRIMARY KEY (id)
);