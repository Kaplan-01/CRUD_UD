CREATE DATABASE escuela;

USE escuela;

CREATE TABLE alumnos(
    id_alumno int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    matricula int(10) NOT NULL,
    nombre varchar(50) NOT NULL,
    primer_apellido varchar(50) NOT NULL,
    segundo_apellido varchar(50) NOT NULL,
    edad int(10) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    sexo varchar(20) NOT NULL,
    estado varchar(20) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET=latin1;

INSERT INTO alumnos(matricula, nombre, primer_apellido, segundo_apellido, edad, fecha_nacimiento, sexo, estado)
VALUES 
(1718110389,'Melanie', 'Kaplan', 'Maldonado', 19, '2000-03-70', 'Femenino', 'Soltero'),
(1718110399,'Nicholas', 'Bladel', 'Hoult', 30, '1990-01-11', 'Masculino', 'Casado');

CREATE USER 'melanie'@'localhost' IDENTIFIED BY 'Agenda.2020';
GRANT ALL PRIVILEGES ON escuela.* TO 'melanie'@'localhost';
FLUSH PRIVILEGES;
