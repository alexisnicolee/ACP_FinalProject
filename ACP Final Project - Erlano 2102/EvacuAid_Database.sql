-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2024 at 02:28 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `evacuaid_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `address`
--

CREATE TABLE `address` (
  `address_id` int(11) NOT NULL,
  `family_id` int(11) DEFAULT NULL,
  `original_address` varchar(255) DEFAULT NULL,
  `region` varchar(100) DEFAULT NULL,
  `postal_code` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `address`
--

INSERT INTO `address` (`address_id`, `family_id`, `original_address`, `region`, `postal_code`) VALUES
(88, 1, 'Sta. Maria', 'IV - A', '4201'),
(89, 2, 'Sta. Maria', 'IV - A', '4201'),
(90, 3, 'Sta. Maria', 'IV - A', '4201'),
(91, 4, 'San Andres', 'IV - A', '4201'),
(92, 5, 'San Pedro', 'IV - A', '4201'),
(93, 6, '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `contact_id` int(11) NOT NULL,
  `family_id` int(11) DEFAULT NULL,
  `primary_contact` varchar(15) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`contact_id`, `family_id`, `primary_contact`, `email`) VALUES
(88, 1, '09272373028', 'a3coley@gmail.com'),
(89, 2, '0927 237 3024', 'alexisnicole@gmail.com'),
(90, 3, '0927 237 3024', 'alexisnicole@gmail.com'),
(91, 4, '0995 378 6089', 'a6colie@gmail.com'),
(92, 5, '0945 387 6532', 'coleym@gmail.com'),
(93, 6, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `families`
--

CREATE TABLE `families` (
  `family_id` int(11) NOT NULL,
  `family_name` varchar(255) NOT NULL,
  `total_family` int(11) NOT NULL,
  `primary_contact` varchar(15) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `original_address` varchar(255) DEFAULT NULL,
  `shelter_location` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `families`
--

INSERT INTO `families` (`family_id`, `family_name`, `total_family`, `primary_contact`, `email`, `original_address`, `shelter_location`) VALUES
(1, 'Erlano ', 4, '09272373028', 'a3coley@gmail.com', 'Sta. Maria', 'Shelter A - Poblacion 2'),
(2, 'Erlano Family', 4, '0927 237 3024', 'alexisnicole@gmail.com', 'Sta. Maria', 'Poblacion 4'),
(3, 'Erlano Family', 4, '0927 237 3024', 'alexisnicole@gmail.com', 'Sta. Maria', 'Poblacion 4'),
(4, 'Martinez', 6, '0995 378 6089', 'a6colie@gmail.com', 'San Andres', 'Poblacio 4'),
(5, 'Martinez', 4, '0945 387 6532', 'coleym@gmail.com', 'San Pedro', 'Sta. Maria'),
(6, '', 0, '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `shelter`
--

CREATE TABLE `shelter` (
  `shelter_id` int(11) NOT NULL,
  `shelter_location` varchar(255) NOT NULL,
  `family_id` int(11) DEFAULT NULL,
  `capacity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shelter`
--

INSERT INTO `shelter` (`shelter_id`, `shelter_location`, `family_id`, `capacity`) VALUES
(84, 'Shelter A - Poblacion 2', 1, 5),
(85, 'Poblacion 4', 2, 5),
(86, 'Poblacion 4', 3, 5),
(87, 'Poblacio 4', 4, 7),
(88, 'Sta. Maria', 5, 4),
(89, '', 6, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `address`
--
ALTER TABLE `address`
  ADD PRIMARY KEY (`address_id`),
  ADD KEY `family_id` (`family_id`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`contact_id`),
  ADD KEY `family_id` (`family_id`);

--
-- Indexes for table `families`
--
ALTER TABLE `families`
  ADD PRIMARY KEY (`family_id`);

--
-- Indexes for table `shelter`
--
ALTER TABLE `shelter`
  ADD PRIMARY KEY (`shelter_id`),
  ADD KEY `family_id` (`family_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `address`
--
ALTER TABLE `address`
  MODIFY `address_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `contact_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT for table `families`
--
ALTER TABLE `families`
  MODIFY `family_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `shelter`
--
ALTER TABLE `shelter`
  MODIFY `shelter_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=90;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `address`
--
ALTER TABLE `address`
  ADD CONSTRAINT `address_ibfk_1` FOREIGN KEY (`family_id`) REFERENCES `families` (`family_id`);

--
-- Constraints for table `contacts`
--
ALTER TABLE `contacts`
  ADD CONSTRAINT `contacts_ibfk_1` FOREIGN KEY (`family_id`) REFERENCES `families` (`family_id`);

--
-- Constraints for table `shelter`
--
ALTER TABLE `shelter`
  ADD CONSTRAINT `shelter_ibfk_1` FOREIGN KEY (`family_id`) REFERENCES `families` (`family_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
