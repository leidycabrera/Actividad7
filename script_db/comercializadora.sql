-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-08-2024 a las 02:35:20
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `comercializadora`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fases_paquete`
--

CREATE TABLE `fases_paquete` (
  `idfases_paquete` int(11) NOT NULL,
  `nombre_fase` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `fases_paquete`
--

INSERT INTO `fases_paquete` (`idfases_paquete`, `nombre_fase`) VALUES
(1, 'Empacando'),
(2, 'Empacado'),
(3, 'Enviado'),
(4, 'En reparto'),
(5, 'Entregado'),
(6, 'Devuelto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paquete`
--

CREATE TABLE `paquete` (
  `idpaquete` int(11) NOT NULL,
  `nombre_paquete` varchar(400) NOT NULL,
  `estado` varchar(1) DEFAULT NULL,
  `fecha_entrega` date DEFAULT NULL,
  `hora_entrega` time DEFAULT NULL,
  `idfases_paquete` int(11) NOT NULL,
  `idpersona` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `paquete`
--

INSERT INTO `paquete` (`idpaquete`, `nombre_paquete`, `estado`, `fecha_entrega`, `hora_entrega`, `idfases_paquete`, `idpersona`) VALUES
(1, 'Herramienta', 'A', '2024-09-07', '14:30:52', 3, 5),
(2, 'Monitor Samsung', 'A', '2024-09-05', '16:33:13', 2, 7),
(3, 'Audifonos', 'A', '2024-08-31', '09:33:40', 4, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

CREATE TABLE `persona` (
  `idpersona` int(11) NOT NULL,
  `nombre_persona` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `docidentidad` varchar(45) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(300) NOT NULL,
  `idtipo_persona` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `persona`
--

INSERT INTO `persona` (`idpersona`, `nombre_persona`, `apellido`, `docidentidad`, `telefono`, `direccion`, `correo`, `username`, `password`, `idtipo_persona`) VALUES
(1, 'Dahianna', 'Cabrera', '1051555252', '320287672', 'Nobsa Boy', 'leidy.cabrera-a@uniminuto.edu.co', 'dcabrera', 'scrypt:32768:8:1$DFrORpE7UJe07izV$05a9e37648c1221c21975fb4ff61ac42e531ca342bf2bfab6269edbb9e54bf9da22a41eddfc4bf7a47f2e76c11d79d9ed92f41b54297d46ff6cd671fa3a7303d', 1),
(2, 'Paula', 'Lopez', '1051555251', '3222333422', 'Nobsa Boy', 'paula.lopez-a@uniminuto.edu.co', 'plopez', 'scrypt:32768:8:1$DFrORpE7UJe07izV$05a9e37648c1221c21975fb4ff61ac42e531ca342bf2bfab6269edbb9e54bf9da22a41eddfc4bf7a47f2e76c11d79d9ed92f41b54297d46ff6cd671fa3a7303d', 5),
(3, 'Nidia', 'Sierra', '1051555253', '334322233', 'Nobsa Boy', 'nidia.sierra-a@uniminuto.edu.co', 'nsierra', 'scrypt:32768:8:1$DFrORpE7UJe07izV$05a9e37648c1221c21975fb4ff61ac42e531ca342bf2bfab6269edbb9e54bf9da22a41eddfc4bf7a47f2e76c11d79d9ed92f41b54297d46ff6cd671fa3a7303d', 2),
(5, 'Lucia', 'Andrade', '2122376', '3423456745', 'Sogamoso Boy', 'liz@gmail.com', 'landrade', 'scrypt:32768:8:1$DFrORpE7UJe07izV$05a9e37648c1221c21975fb4ff61ac42e531ca342bf2bfab6269edbb9e54bf9da22a41eddfc4bf7a47f2e76c11d79d9ed92f41b54297d46ff6cd671fa3a7303d', 8),
(6, 'Cristian', 'Robles', '454535634', '454343335', 'Sogamoso Boy', 'cristian@gmail.com', 'crobles', 'scrypt:32768:8:1$DFrORpE7UJe07izV$05a9e37648c1221c21975fb4ff61ac42e531ca342bf2bfab6269edbb9e54bf9da22a41eddfc4bf7a47f2e76c11d79d9ed92f41b54297d46ff6cd671fa3a7303d', 5),
(7, 'Lizandro', 'Rojas', '2122376', '3423456745', 'Sogamoso Boy', 'liz@gmail.com', 'lrojas', 'scrypt:32768:8:1$DFrORpE7UJe07izV$05a9e37648c1221c21975fb4ff61ac42e531ca342bf2bfab6269edbb9e54bf9da22a41eddfc4bf7a47f2e76c11d79d9ed92f41b54297d46ff6cd671fa3a7303d', 8),
(8, 'Cristian', 'Robles', '454535634', '454343335', 'Sogamoso Boy', 'cristian@gmail.com', 'crobles', 'scrypt:32768:8:1$DFrORpE7UJe07izV$05a9e37648c1221c21975fb4ff61ac42e531ca342bf2bfab6269edbb9e54bf9da22a41eddfc4bf7a47f2e76c11d79d9ed92f41b54297d46ff6cd671fa3a7303d', 5),
(9, 'Laura', 'Niño', '122123434', '3208287672', 'Sogamoso Boy', 'laura312@gmail.com', 'lniño', 'scrypt:32768:8:1$DFrORpE7UJe07izV$05a9e37648c1221c21975fb4ff61ac42e531ca342bf2bfab6269edbb9e54bf9da22a41eddfc4bf7a47f2e76c11d79d9ed92f41b54297d46ff6cd671fa3a7303d', 3),
(10, 'Maria', 'Gutierrez', '3442342343', '5345433', 'Sogamoso Boy', 'maria934@gmail.com', 'mgutierrez', 'scrypt:32768:8:1$DFrORpE7UJe07izV$05a9e37648c1221c21975fb4ff61ac42e531ca342bf2bfab6269edbb9e54bf9da22a41eddfc4bf7a47f2e76c11d79d9ed92f41b54297d46ff6cd671fa3a7303d', 8),
(13, 'Andrea', 'Jaimes', '4343453534', '32122344543', 'Sogamoso Boy', 'andrea323@gmail.com', 'ajaimes', 'scrypt:32768:8:1$DFrORpE7UJe07izV$05a9e37648c1221c21975fb4ff61ac42e531ca342bf2bfab6269edbb9e54bf9da22a41eddfc4bf7a47f2e76c11d79d9ed92f41b54297d46ff6cd671fa3a7303d', 4),
(19, 'David', 'Monroy', '12223765', '3256738763', 'Sogamoso', 'david@gmail.com', 'DMonroy', 'scrypt:32768:8:1$cJEEyc7iQShY3eZQ$6804596cfc0ec72cee6cc76843c28665fcfec4c2d9dd4b85392a58d7d48d7b3e3264282cdd26638eb7982e5c9958cd9dc2d5ba0d7a165d1259b109304b2121c6', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_persona`
--

CREATE TABLE `tipo_persona` (
  `idtipo_persona` int(11) NOT NULL,
  `nombre_tipo` varchar(45) DEFAULT NULL,
  `estado` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipo_persona`
--

INSERT INTO `tipo_persona` (`idtipo_persona`, `nombre_tipo`, `estado`) VALUES
(1, 'Administrador', 'A'),
(2, 'Gerente', 'A'),
(3, 'Empacador', 'A'),
(4, 'Transportador', 'A'),
(5, 'Recepcionista', 'A'),
(6, 'Distribuidor', 'A'),
(8, 'Cliente', 'A');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `fases_paquete`
--
ALTER TABLE `fases_paquete`
  ADD PRIMARY KEY (`idfases_paquete`);

--
-- Indices de la tabla `paquete`
--
ALTER TABLE `paquete`
  ADD PRIMARY KEY (`idpaquete`),
  ADD KEY `fk_paquete_fases_paquete1` (`idfases_paquete`),
  ADD KEY `fk_paquete_persona1` (`idpersona`);

--
-- Indices de la tabla `persona`
--
ALTER TABLE `persona`
  ADD PRIMARY KEY (`idpersona`),
  ADD KEY `fk_persona_tipo_persona1` (`idtipo_persona`);

--
-- Indices de la tabla `tipo_persona`
--
ALTER TABLE `tipo_persona`
  ADD PRIMARY KEY (`idtipo_persona`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `fases_paquete`
--
ALTER TABLE `fases_paquete`
  MODIFY `idfases_paquete` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `paquete`
--
ALTER TABLE `paquete`
  MODIFY `idpaquete` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `persona`
--
ALTER TABLE `persona`
  MODIFY `idpersona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `tipo_persona`
--
ALTER TABLE `tipo_persona`
  MODIFY `idtipo_persona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `paquete`
--
ALTER TABLE `paquete`
  ADD CONSTRAINT `fk_paquete_fases_paquete1` FOREIGN KEY (`idfases_paquete`) REFERENCES `fases_paquete` (`idfases_paquete`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_paquete_persona1` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `persona`
--
ALTER TABLE `persona`
  ADD CONSTRAINT `fk_persona_tipo_persona1` FOREIGN KEY (`idtipo_persona`) REFERENCES `tipo_persona` (`idtipo_persona`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
