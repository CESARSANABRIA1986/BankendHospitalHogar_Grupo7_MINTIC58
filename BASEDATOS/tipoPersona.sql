CREATE TABLE tipoPersona(
idTipoPersona INTEGER PRIMARY KEY not null,
tipoPersona VARCHAR (50) not null
);
INSERT INTO tipopersona (idtipopersona, tipopersona) values (1, 'Medico') ;
INSERT INTO tipopersona (idtipopersona, tipopersona) values (2, 'Paciente');
INSERT INTO tipopersona (idtipopersona, tipopersona) values (3, 'Acudiente');
select * from tipopersona;