-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2024 at 09:50 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hoteldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin123'),
(2, 'a', 'w');

-- --------------------------------------------------------

--
-- Table structure for table `cust_reservation`
--

CREATE TABLE `cust_reservation` (
  `id` int(10) NOT NULL,
  `c_id` varchar(12) NOT NULL,
  `p_id` varchar(12) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile` int(15) NOT NULL,
  `no_of_pax` int(11) NOT NULL,
  `reservation_date` date NOT NULL,
  `make_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cust_reservation`
--

INSERT INTO `cust_reservation` (`id`, `c_id`, `p_id`, `full_name`, `email`, `mobile`, `no_of_pax`, `reservation_date`, `make_date`) VALUES
(1, 'C003', 'P006', 'Senesh Dilshan', 'seneshnagod@gmail.com', 774589322, 25, '2024-05-19', '2024-05-01 04:38:13'),
(3, 'C001', 'P006', 'Amal Perera', 'amal@gmail.com', 774589322, 4, '2024-05-02', '2024-04-29 21:19:30'),
(4, 'C001', 'P007', 'sdfsdfsdf ', 'dsfdsf@gmail.com', 11542, 16, '2024-05-02', '2024-04-30 08:28:55');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(10) NOT NULL,
  `customer_id` varchar(12) NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(10) NOT NULL,
  `email` varchar(32) NOT NULL,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `customer_id`, `username`, `password`, `email`, `create_date`) VALUES
(1, 'C001', 'Amal', '123', 'amal@gmail.com', '2024-04-29 16:44:58'),
(2, 'C002', 'Nimal', 'nimal123', 'nimal@gmail.com', '2024-04-27 19:24:10'),
(3, 'C003', 'a', 'a', '', '2024-04-29 19:31:42');

-- --------------------------------------------------------

--
-- Table structure for table `number_of_pax`
--

CREATE TABLE `number_of_pax` (
  `id` int(11) NOT NULL,
  `max_no_of_pax` int(11) NOT NULL,
  `cost` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `number_of_pax`
--

INSERT INTO `number_of_pax` (`id`, `max_no_of_pax`, `cost`) VALUES
(1, 15, 3000),
(2, 25, 2500),
(3, 50, 1500),
(4, 51, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `packages`
--

CREATE TABLE `packages` (
  `id` int(10) NOT NULL,
  `p_id` varchar(12) NOT NULL,
  `p_name` varchar(30) NOT NULL,
  `cost_per_person` int(11) NOT NULL,
  `description` varchar(300) NOT NULL,
  `complementary` varchar(300) NOT NULL,
  `category` varchar(30) NOT NULL,
  `p_image` varchar(1000) NOT NULL,
  `p_create_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `packages`
--

INSERT INTO `packages` (`id`, `p_id`, `p_name`, `cost_per_person`, `description`, `complementary`, `category`, `p_image`, `p_create_date`) VALUES
(13, 'P007', 'Night party', 1, 'asdasdadasd', 'CAR PARKING', '', 'P007.jpg', '2024-05-01 07:13:09'),
(14, 'P0014', 'Weeding Party', 1, 'First and foremost, your wedding party website descriptions should be unique to each person. Don\'t just write their names and their wedding party roles. ', 'FREE WIFI, BUTLER SERVICE, INFINITY POOL', '', 'P0014.jpg', '2024-04-30 08:14:45'),
(15, 'P0015', 'Full day Weeding Party', 1, 'First and foremost, your wedding party website descriptions should be unique to each person. Don\'t just write their names and their wedding party roles. ', 'FREE WIFI, BUTLER SERVICE, INFINITY POOL', '', 'P0015.jpg', '2024-04-30 08:15:49'),
(16, 'P0016', 'Birthday Party', 1, 'Discover hints and tips on how to write your party invitations with invitation wording ideas for birthdays and other special occasions.', 'FREE WIFI, 24HR SECURITY , BUTLER SERVICE, CAR PARKING, INFINITY POOL, 24HR SERVICE', '', 'P0016.jpg', '2024-05-01 07:12:48');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `staff_id` varchar(12) NOT NULL,
  `s_name` varchar(32) NOT NULL,
  `s_photo` varchar(1000) NOT NULL,
  `s_gender` varchar(50) NOT NULL,
  `s_department` varchar(50) NOT NULL,
  `s_address` varchar(255) NOT NULL,
  `s_contact_no` varchar(15) NOT NULL,
  `s_email` varchar(32) NOT NULL,
  `s_salary` int(32) NOT NULL,
  `s_g_certificate` varchar(1000) NOT NULL,
  `s_p_certificate` varchar(1000) NOT NULL,
  `s_acc_create_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`id`, `staff_id`, `s_name`, `s_photo`, `s_gender`, `s_department`, `s_address`, `s_contact_no`, `s_email`, `s_salary`, `s_g_certificate`, `s_p_certificate`, `s_acc_create_date`) VALUES
(31, 'S0021', 'Dasun Shanaka', 'S0021.jpg', 'Male', 'Housekeeping', 'Badulla, Sri Lanka', '0716402929', 'dsfsdfds@sdfs.com', 30000, 'GC_S0021.jpg', 'PC_S0021.jpg', '2024-04-29 08:47:12'),
(32, 'S0032', 'Danushka', 'S0032.jpg', 'Male', 'Kitchen', 'Colombo, Sri Lanka', '0774589322', 'senesh@gmail.com', 50000, 'GC_S0032.png', 'PC_S0032.jpg', '2024-04-30 08:26:14'),
(33, 'S0033', 'Dilka Subash', 'S0033.png', 'Male', 'Banquets', 'Galle, Nagoda', '0774589322', 'senesdh@gmail.com', 60000, 'GC_S0033.jpg', 'PC_S0033.png', '2024-04-30 08:12:12'),
(34, 'S0034', 'senesh', 'S0034.jpg', 'Male', 'Banquets', 'galle', '0774523955', 'sddfsdf@gmail.com', 60000, 'GC_S0034.jpg', 'PC_S0034.png', '2024-04-30 08:27:33'),
(35, 'S0035', 'Uthara Devi', 'S0035.png', 'Female', 'Housekeeping', 'Galle, Sri Lanka', '0774589322', 'seneshdilshan@gmail.com', 30000, 'GC_S0035.jpg', 'PC_S0035.png', '2024-05-01 06:58:04'),
(36, 'S0036', 'john Green', 'S0036.png', 'Male', 'Kitchen', 'Colombo, Sri Lanka', '0771289357', 'sample@gm.com', 50000, 'GC_S0036.jpg', 'PC_S0036.png', '2024-05-01 07:02:21'),
(37, 'S0037', 'Keen Williyoumson', 'S0037.jpg', 'Male', 'Housekeeping', 'Nagoda,\nGalle,\nSri Lanka', '0771245985', 'ufynkf@gmail.com', 30000, 'GC_S0037.jpg', 'PC_S0037.png', '2024-05-01 07:07:40');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cust_reservation`
--
ALTER TABLE `cust_reservation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `c_id` (`c_id`,`p_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customer_id` (`customer_id`),
  ADD KEY `customer_id_2` (`customer_id`),
  ADD KEY `customer_id_3` (`customer_id`);

--
-- Indexes for table `number_of_pax`
--
ALTER TABLE `number_of_pax`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `packages`
--
ALTER TABLE `packages`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `p_id` (`p_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `cust_reservation`
--
ALTER TABLE `cust_reservation`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `number_of_pax`
--
ALTER TABLE `number_of_pax`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `packages`
--
ALTER TABLE `packages`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cust_reservation`
--
ALTER TABLE `cust_reservation`
  ADD CONSTRAINT `cust_reservation_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `login` (`customer_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
