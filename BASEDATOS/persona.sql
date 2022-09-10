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
	contraseña VARCHAR(16) not null,
	FOREIGN KEY(idTipoPersonas) REFERENCES tipoPersona(idTipoPersona)
);

INSERT INTO persona  (cedula, primernombre, segundonombre, primerapellido, segundoapellido, telefono, pais, departamento, municipio,
barrio, idtipopersonas, contraseña) values (1098622901, 'cesar', 'augusto', 'sanabria',
'casanova', '3102857230', 'Colombia', 'Santander','Floridablanca', 'Rosales', 1, 'cesar1986') ;

INSERT INTO persona  (cedula, primernombre, segundonombre, primerapellido, segundoapellido, telefono, pais, departamento, municipio,
barrio, idtipopersonas, contraseña) values (63310789, 'glady', '', 'casanova',
'cuadros', '3118543049', 'Colombia', 'Santander','Bucaramanga', 'Giron', 1, 'Gladys1964') ;
