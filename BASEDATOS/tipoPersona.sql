CREATE TABLE tipoPersona(
idTipoPersona SERIAl PRIMARY KEY not null,
tipoPersona VARCHAR (50) not null
);
INSERT INTO tipopersona(tipopersona) VALUES ('MEDICO');
INSERT INTO tipopersona(tipopersona) VALUES ('PACIENTE');
INSERT INTO tipopersona(tipopersona) VALUES ('ACUDIENTE');


SELECT * FROM tipopersona;