CREATE TABLE signoVitales(
	idSignoVitales SERIAl PRIMARY KEY not null,
	oximetria INTEGER not null,
	frecuenciaRespiratoria INTEGER not NULL,
	frecuenciafrecuenciaCardiaca INTEGER not NULL,
	temperatura INTEGER not NULL,
	presionArterial INTEGER not NULL,
	glicemia INTEGER not NULL,
	fechaHoraSignosVitales date
);