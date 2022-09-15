CREATE TABLE especializacion(
idEspecializacion INTEGER PRIMARY KEY not null,
nombreEspecializacion VARCHAR (100)
);


alter table persona
add constraint FKtest
Foreign key (idEspecialidad)
references especializacion(idEspecializacion)