CREATE TABLE partidos (
    id int NOT NULL AUTO_INCREMENT,
    jugadorLocal int NOT NULL,
    equipoLocal int NOT NULL,
    golesLocal int NOT NULL,
    jugadorVisitante int NOT NULL,
    equipoVisitante int NOT NULL,
    golesVisitante int NOT NULL,
    ganador int NOT NULL,
    PRIMARY KEY (id)
);