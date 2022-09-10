create table hospitalizacion(
	idHospitalizacion SERIAl PRIMARY KEY not null,
	sugerenciaMedicas VARCHAR(500) not null, 
	idSignosVitales INT NOT null,
	cedula INTEGER,
	FOREIGN KEY(idSignosVitales) REFERENCES signoVitales (idSignoVitales),
	FOREIGN KEY(cedula) REFERENCES persona (cedula)
);