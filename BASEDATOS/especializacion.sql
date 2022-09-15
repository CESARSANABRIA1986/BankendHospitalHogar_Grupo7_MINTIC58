CREATE TABLE especializacion(
idEspecializacion INTEGER PRIMARY KEY not null,
nombreEspecializacion VARCHAR (100)
);


alter table persona
add constraint FKtest
Foreign key (idEspecialidad)
references especializacion(idEspecializacion)


insert into especializacion values (1, 'Neurología');
insert into especializacion values (2, 'Pediatría');
insert into especializacion values (3, 'Medicina Interna');
insert into especializacion values (4, 'Anestesia');
insert into especializacion values (5, 'Ginecología');
insert into especializacion values (6, 'Urología');
insert into especializacion values (7, 'Cardiologia');
insert into especializacion values (8, 'Oftalmología');
insert into especializacion values (9, 'Ortopedia');
insert into especializacion values (10, 'Psiquiatría');