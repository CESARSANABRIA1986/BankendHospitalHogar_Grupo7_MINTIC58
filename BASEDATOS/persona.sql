create table persona(
	cedula INTEGER PRIMARY KEY not null,
	primerNombre VARCHAR(20) not null, 
	segundoNombre varchar(20),
	primerApellido VARCHAR(20) not null, 
	segundoApellido VARCHAR(20), 
	telefono VARCHAR(15),
	pais VARCHAR(20),
	departamento varchar(20),
	municipio VARCHAR(30),
	barrio VARCHAR(30),
	idTipoPersonas INTEGER, 
	idHospitalizaciones INTEGER,
	FOREIGN KEY(idTipoPersonas) REFERENCES tipoPersona(idTipoPersona),
	FOREIGN KEY(idHospitalizaciones) REFERENCES hospitalizacion (idHospitalizacion)
);
