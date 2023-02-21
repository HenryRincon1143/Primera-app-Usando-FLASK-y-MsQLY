-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3308
-- Tiempo de generación: 21-02-2023 a las 22:41:53
-- Versión del servidor: 8.0.27
-- Versión de PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hjas_data`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargos`
--

DROP TABLE IF EXISTS `cargos`;
CREATE TABLE IF NOT EXISTS `cargos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cargo` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `cargos`
--

INSERT INTO `cargos` (`id`, `cargo`) VALUES
(1, 'super_admin'),
(2, 'admin'),
(3, 'cliente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajadores`
--

DROP TABLE IF EXISTS `trabajadores`;
CREATE TABLE IF NOT EXISTS `trabajadores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `op` varchar(30) NOT NULL,
  `documento` varchar(30) NOT NULL,
  `celular` varchar(30) NOT NULL,
  `correo` varchar(30) NOT NULL,
  `usuario` varchar(40) NOT NULL,
  `clave` varchar(40) NOT NULL,
  `id_cargos` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_cargos` (`id_cargos`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `trabajadores`
--

INSERT INTO `trabajadores` (`id`, `nombres`, `apellidos`, `op`, `documento`, `celular`, `correo`, `usuario`, `clave`, `id_cargos`) VALUES
(1, 'juan', 'villar', 'admin', '1125698658', '123', 'juan123@gmail.com', 'juan1', '123', 2),
(2, 'julio', 'castaño', 'Cedula Extranjera', '111', '111', 'julio_cast@gmail.com', 'julio1', '123', 1),
(3, 'Henry', 'Rincon', 'Cedula nacional', '123456', '30135692', 'hjri@soy.sena.edu.co', 'hj1', '123', 3);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `trabajadores`
--
ALTER TABLE `trabajadores`
  ADD CONSTRAINT `trabajadores_ibfk_1` FOREIGN KEY (`id_cargos`) REFERENCES `cargos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
