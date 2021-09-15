-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 15, 2021 at 01:03 AM
-- Server version: 5.6.35
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `holts`
--

-- --------------------------------------------------------

--
-- Table structure for table `CUSTOMER`
--

CREATE TABLE `CUSTOMER` (
  `CUSTOMER_NUM` int(11) NOT NULL,
  `CUSTOMER_NAME` varchar(30) DEFAULT NULL,
  `CUSTOMER_ADDRESS1` varchar(30) DEFAULT NULL,
  `CUSTOMER_ADDRESS2` varchar(25) DEFAULT NULL,
  `CUSTOMER_CITY` varchar(20) DEFAULT NULL,
  `CUSTOMER_STATE` varchar(2) DEFAULT NULL,
  `CUSTOMER_ZIP` int(5) DEFAULT NULL,
  `MTDSALES` decimal(8,2) DEFAULT NULL,
  `YTDSALES` decimal(8,2) DEFAULT NULL,
  `CURRENT_BALANCE` decimal(15,2) DEFAULT NULL,
  `CREDIT_LIMIT` decimal(15,2) DEFAULT NULL,
  `SHIPPING_NAME` varchar(30) DEFAULT NULL,
  `SHIPPING_ADDRESS1` varchar(30) DEFAULT NULL,
  `SHIPPING_ADDRESS2` varchar(25) DEFAULT NULL,
  `SHIPPING_CITY` varchar(20) DEFAULT NULL,
  `SHIPPING_STATE` varchar(2) DEFAULT NULL,
  `SHIPPING_ZIP` int(5) DEFAULT NULL,
  `INVOICE_TOTAL` decimal(8,2) DEFAULT NULL,
  `PAYMENT_TOTAL` decimal(10,2) DEFAULT NULL,
  `CURRENT_AMOUNT` decimal(10,2) DEFAULT NULL,
  `PREVIOUS_BALANCE` decimal(10,2) DEFAULT NULL,
  `TERRITORY_NUM` int(11) DEFAULT NULL,
  `SALES_REP_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `CUSTOMER`
--

INSERT INTO `CUSTOMER` (`CUSTOMER_NUM`, `CUSTOMER_NAME`, `CUSTOMER_ADDRESS1`, `CUSTOMER_ADDRESS2`, `CUSTOMER_CITY`, `CUSTOMER_STATE`, `CUSTOMER_ZIP`, `MTDSALES`, `YTDSALES`, `CURRENT_BALANCE`, `CREDIT_LIMIT`, `SHIPPING_NAME`, `SHIPPING_ADDRESS1`, `SHIPPING_ADDRESS2`, `SHIPPING_CITY`, `SHIPPING_STATE`, `SHIPPING_ZIP`, `INVOICE_TOTAL`, `PAYMENT_TOTAL`, `CURRENT_AMOUNT`, `PREVIOUS_BALANCE`, `TERRITORY_NUM`, `SALES_REP_ID`) VALUES
(1, 'Tayyab Woodley', '75 Old Greystone St.', 'Suite 2', 'Brookfield', 'WI', 53045, '4766.34', '61445.76', '3412.45', '1000000.00', 'Yasmine Macias', '9625 Rockland Dr.', 'Suite R', 'Londonderry', 'NH', 3053, '20769.17', '20769.17', '3412.45', '3412.45', 10, 4),
(2, 'Nel Holden', '668 Lilac Dr.', 'Fl 3', 'North Haven', 'CT', 6473, '2564.65', '5256.45', '526.76', '1000000.00', 'Amaan Carlson', '21 West Newport Court', 'Suite 3', 'Randallstown', 'MD', 21133, '1844.97', '1844.97', '526.76', '526.76', 10, 8),
(3, 'Xena McCall', '17 Ketch Harbour Rd.', 'Apt 5', 'Westport', 'CT', 6880, '425.56', '2956.45', '1646.54', '1000000.00', 'Ajwa Cowan', '892 Princess St.', 'Apt 4C', 'King of Prussia', 'PA', 19406, '0.00', '0.00', '1646.54', '1646.54', 7, 10),
(4, 'Fearne Whitworth', '8 Warren St.', 'Apt 5', 'Loveland', 'OH', 45140, '425.45', '2496.46', '287.45', '1000000.00', 'Aled Blevins', '8204 SW. Princess Ave.', 'Suite 3', 'Algonquin', 'IL', 60102, '0.00', '0.00', '287.45', '287.45', 2, 3),
(5, 'Bernice Osborn', '2 Birchwood St.', 'Apt 20', 'North Ridgeville', 'OH', 44039, '1275.56', '5245.63', '974.74', '1000000.00', 'Morgan Marquez', '7883 53rd Dr.', 'Apt 7', 'Klamath Falls', 'OR', 97603, '1906.40', '1906.40', '974.74', '974.74', 6, 9),
(6, 'Muhamed Domingue', '9291 Bald Hill Rd.', 'Suite 1', 'Westlake', 'OH', 44145, '134.34', '645.23', '346.45', '1000000.00', 'Aayan Akhtar', '480 Plymouth Dr.', 'Fl 3', 'Roy', 'UT', 84067, '0.00', '0.00', '346.45', '346.45', 4, 1),
(7, 'Nabila Weiss', '736 Peachtree Ave.', 'Fl 2', 'Coventry', 'RI', 2816, '1837.45', '28454.46', '3684.34', '1000000.00', 'Emanuel Simmonds', '19 Ridgeview Dr.', 'Suite 4', 'Maineville', 'OH', 45039, '6764.11', '6764.11', '3684.34', '3684.34', 8, 6),
(8, 'Chanelle Morris', '9631 Cambridge St.', 'Suite 3', 'Marshfield', 'WI', 54449, '23.45', '423.76', '267.45', '1000000.00', 'Amari Bird', '627 Mechanic St.', 'Apt 2', 'West Bloomfield', 'MI', 48322, '0.00', '0.00', '267.45', '267.45', 9, 7),
(9, 'Walter Michael', '198 Redwood Rd.', 'Apt 5', 'Minneapolis', 'MN', 55406, '7457.83', '34452.97', '12042.03', '1000000.00', 'Conall Lawson', '8341 Ann St.', 'Apt 6', 'Allison Park', 'PA', 15101, '9902.34', '1818.76', '12042.03', '3958.45', 5, 5),
(10, 'Danyal Ashley', '36 Main St.', 'Apt 8', 'Wappingers Falls', 'NY', 12590, '2456.45', '5646.45', '2398.72', '1000000.00', 'Gregg Mooney', '8379 Wrangler Lane', 'Apt 12', 'Amsterdam', 'NY', 12010, '1723.38', '0.00', '2398.72', '675.34', 7, 10);

-- --------------------------------------------------------

--
-- Table structure for table `INVOICE`
--

CREATE TABLE `INVOICE` (
  `INVOICE_NUM` int(11) NOT NULL,
  `INVOICE_DATE` date DEFAULT NULL,
  `INVOICE_TOTAL` decimal(10,2) DEFAULT NULL,
  `INVOICE_SHIPPING` decimal(10,2) DEFAULT NULL,
  `INVOICE_TAX` decimal(2,0) DEFAULT NULL,
  `CUSTOMER_NUM` int(11) DEFAULT NULL,
  `ORDER_NUM` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `INVOICE`
--

INSERT INTO `INVOICE` (`INVOICE_NUM`, `INVOICE_DATE`, `INVOICE_TOTAL`, `INVOICE_SHIPPING`, `INVOICE_TAX`, `CUSTOMER_NUM`, `ORDER_NUM`) VALUES
(17, '2019-11-14', '6764.11', '35.00', '28', 7, 4),
(18, '2019-12-01', '328.83', '25.00', '24', 9, 10),
(19, '2019-12-15', '1906.40', '25.00', '27', 5, 3),
(20, '2020-01-06', '9655.99', '17.00', '15', 1, 9),
(21, '2020-01-25', '5757.22', '27.50', '22', 1, 5),
(22, '2020-01-25', '1489.93', '32.00', '27', 9, 8),
(23, '2020-05-20', '8083.58', '23.75', '16', 9, 6),
(24, '2020-05-20', '5355.96', '17.00', '13', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `ORDERS`
--

CREATE TABLE `ORDERS` (
  `ORDER_NUM` int(11) NOT NULL,
  `ORDER_DATE` date DEFAULT NULL,
  `ORDER_COMMENTS` varchar(50) DEFAULT NULL,
  `CUSTOMER_PO_NUM` varchar(20) DEFAULT NULL,
  `ORDER_STATUS` varchar(20) DEFAULT NULL,
  `CUSTOMER_NUM` int(11) DEFAULT NULL,
  `SPECIAL_CHARGE_NUM` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ORDERS`
--

INSERT INTO `ORDERS` (`ORDER_NUM`, `ORDER_DATE`, `ORDER_COMMENTS`, `CUSTOMER_PO_NUM`, `ORDER_STATUS`, `CUSTOMER_NUM`, `SPECIAL_CHARGE_NUM`) VALUES
(11, '2020-04-14', ' ', 'PO45345', 'CLOSED', 1, 4),
(12, '2020-06-26', 'Color: Blue', 'PO869506', 'OPEN', 2, 7),
(13, '2019-12-10', ' ', ' ', 'CLOSED', 5, 6),
(14, '2019-10-23', ' ', ' ', 'CLOSED', 7, 7),
(15, '2020-01-04', 'Size: Large', 'PO13906', 'CLOSED', 1, 9),
(16, '2020-03-29', ' ', 'PO8495', 'CLOSED', 9, 5),
(17, '2019-12-10', 'Size: Medium', ' ', 'OPEN', 10, 4),
(18, '2020-01-04', 'Size: Large', ' ', 'CLOSED', 9, 7),
(19, '2019-12-10', 'Color: Black', ' ', 'CLOSED', 1, 5),
(20, '2019-10-23', ' ', 'PO2576', 'CLOSED', 9, 2);

-- --------------------------------------------------------

--
-- Table structure for table `ORDER_DETAILS`
--

CREATE TABLE `ORDER_DETAILS` (
  `ORDER_DETAIL_NUM` int(11) NOT NULL,
  `NUMBER_ORDERED` int(10) DEFAULT NULL,
  `QUOTED_PRICE` decimal(10,2) DEFAULT NULL,
  `PART_NUM` int(11) DEFAULT NULL,
  `ORDER_NUM` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ORDER_DETAILS`
--

INSERT INTO `ORDER_DETAILS` (`ORDER_DETAIL_NUM`, `NUMBER_ORDERED`, `QUOTED_PRICE`, `PART_NUM`, `ORDER_NUM`) VALUES
(41, 5, '219.76', 5, 9),
(42, 4, '764.23', 4, 6),
(43, 8, '209.38', 8, 7),
(44, 5, '85.45', 1, 9),
(45, 10, '85.45', 1, 1),
(46, 8, '219.76', 5, 2),
(47, 7, '387.35', 10, 6),
(48, 1, '209.38', 8, 10),
(49, 8, '476.87', 9, 4),
(50, 15, '123.65', 2, 3),
(51, 3, '229.38', 8, 9),
(52, 18, '123.65', 2, 6),
(53, 10, '219.76', 5, 1),
(54, 4, '387.35', 10, 9),
(55, 9, '634.23', 3, 5),
(56, 2, '123.65', 2, 1),
(57, 6, '329.45', 6, 1),
(58, 3, '476.87', 9, 8),
(59, 15, '190.76', 5, 4),
(60, 18, '359.45', 6, 9);

-- --------------------------------------------------------

--
-- Table structure for table `PART`
--

CREATE TABLE `PART` (
  `PART_NUM` int(11) NOT NULL,
  `PART_DESCRIPTION` varchar(50) DEFAULT NULL,
  `UNIT_PRICE` decimal(8,2) DEFAULT NULL,
  `MTDSALES` decimal(10,2) DEFAULT NULL,
  `YTDSALES` decimal(10,2) DEFAULT NULL,
  `UNITS_ONHAND` int(10) DEFAULT NULL,
  `UNITS_ALLOCATED` int(10) DEFAULT NULL,
  `REORDER_POINT` int(10) DEFAULT NULL,
  `NOTES` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PART`
--

INSERT INTO `PART` (`PART_NUM`, `PART_DESCRIPTION`, `UNIT_PRICE`, `MTDSALES`, `YTDSALES`, `UNITS_ONHAND`, `UNITS_ALLOCATED`, `REORDER_POINT`, `NOTES`) VALUES
(1, 'T-Shirt', '85.45', '2221.70', '14114.10', 53, 15, 125, '*'),
(2, 'Sweatpant', '123.65', '8284.55', '105226.15', 576, 35, 200, ' '),
(3, 'Jacket', '634.23', '32979.96', '413517.96', 546, 9, 200, ' '),
(4, 'Coat', '764.23', '32097.66', '261366.66', 91, 4, 150, '*'),
(5, 'Jeans', '219.76', '18020.32', '90101.60', 286, 38, 125, ' '),
(6, 'Backpack', '329.45', '20755.35', '172302.35', 494, 24, 75, ' '),
(7, 'Wallet', '154.98', '13948.20', '112050.54', 41, 0, 150, '*'),
(8, 'Dress', '209.38', '17169.16', '135050.10', 374, 12, 125, ' '),
(9, 'Hoodie', '476.87', '17644.19', '200749.64', 265, 11, 150, ' '),
(10, 'Sneaker', '387.35', '14719.30', '113493.55', 218, 11, 150, ' ');

-- --------------------------------------------------------

--
-- Table structure for table `PAYMENT`
--

CREATE TABLE `PAYMENT` (
  `PAYMENT_NUM` int(11) NOT NULL,
  `PAYMENT_DATE` date DEFAULT NULL,
  `PAYMENT_AMOUNT` decimal(15,2) DEFAULT NULL,
  `CUSTOMER_NUM` int(11) DEFAULT NULL,
  `INVOICE_NUM` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PAYMENT`
--

INSERT INTO `PAYMENT` (`PAYMENT_NUM`, `PAYMENT_DATE`, `PAYMENT_AMOUNT`, `CUSTOMER_NUM`, `INVOICE_NUM`) VALUES
(1, '2019-12-15', '328.83', 9, 2),
(2, '2020-01-25', '6764.11', 7, 1),
(3, '2020-02-04', '1906.40', 5, 3),
(4, '2020-02-04', '1489.93', 9, 7),
(5, '2020-02-20', '5757.22', 9, 6),
(6, '2020-06-17', '8083.58', 1, 8),
(7, '2020-06-23', '9655.99', 1, 5),
(8, '2020-07-28', '5355.96', 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `SALES_REP`
--

CREATE TABLE `SALES_REP` (
  `SALES_REP_ID` int(11) NOT NULL,
  `SALES_REP_NAME` varchar(30) DEFAULT NULL,
  `SALES_REP_ADDRESS` varchar(35) DEFAULT NULL,
  `SALES_REP_CITY` varchar(20) DEFAULT NULL,
  `SALES_REP_STATE` varchar(2) DEFAULT NULL,
  `SALES_REP_ZIP` varchar(5) DEFAULT NULL,
  `MTDSALES` decimal(10,2) DEFAULT NULL,
  `YTDSALES` decimal(10,2) DEFAULT NULL,
  `MTD_COMMISSION` decimal(8,2) DEFAULT NULL,
  `YTD_COMMISSION` decimal(8,2) DEFAULT NULL,
  `COMMISSION_RATE` decimal(8,5) DEFAULT NULL,
  `TERRITORY_NUM` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `SALES_REP`
--

INSERT INTO `SALES_REP` (`SALES_REP_ID`, `SALES_REP_NAME`, `SALES_REP_ADDRESS`, `SALES_REP_CITY`, `SALES_REP_STATE`, `SALES_REP_ZIP`, `MTDSALES`, `YTDSALES`, `MTD_COMMISSION`, `YTD_COMMISSION`, `COMMISSION_RATE`, `TERRITORY_NUM`) VALUES
(1, 'Gene Appleton', '310 Wayne Str.', 'Malvern', 'PA', '19355', '345.34', '7535.34', '18.30', '399.37', '0.05000', 4),
(2, 'Elleanor Melton', '63 Cooper Dr.', 'Lewiston', 'ME', '04240', '8474.35', '35984.45', '661.00', '2806.79', '0.08000', 6),
(3, 'Keiran Lott', '9353 Annadale Dr.', 'Harvey', 'IL', '06426', '1245.39', '4124.56', '150.69', '499.07', '0.12000', 2),
(4, 'Francesca Morse', '267 S. Third Ave.', 'Southfield', 'MI', '48076', '65.23', '786.23', '0.78', '9.43', '0.01000', 10),
(5, 'Chandler McCormick', '8385 Hillcrest St.', 'Miami', 'FL', '33125', '6567.34', '96434.34', '584.49', '8582.66', '0.09000', 5),
(6, 'Clarice Bean', '89 Kirkland Dr.', 'Grayslake', 'IL', '60030', '742.45', '4653.45', '48.26', '302.47', '0.07000', 8),
(7, 'Balraj Haynes', '58 Thorne St.', 'Corpus Christi', 'TX', '78418', '657.45', '24567.45', '32.22', '1203.81', '0.05000', 9),
(8, 'Dawson Fellows', '8078 Bellevue Dr.', 'Lansing', 'MI', '48910', '1234.56', '44554.34', '67.90', '2450.49', '0.06000', 10),
(9, 'Uma Blevins', '55 DE. Ridge St.', 'Mokena', 'IL', '60448', '967.56', '34456.43', '32.90', '1171.52', '0.03000', 6),
(10, 'Fannie Riddle', '47 Plymouth Ave.', 'Brighton', 'MA', '02135', '8474.35', '35984.45', '661.00', '2806.79', '0.08000', 7);

-- --------------------------------------------------------

--
-- Table structure for table `SPECIAL_CHARGES`
--

CREATE TABLE `SPECIAL_CHARGES` (
  `SPECIAL_CHARGE_NUM` int(11) NOT NULL,
  `SPECIAL_CHARGE_DESCRIPTION` varchar(40) DEFAULT NULL,
  `SPECIAL_CHARGE_AMOUNT` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `SPECIAL_CHARGES`
--

INSERT INTO `SPECIAL_CHARGES` (`SPECIAL_CHARGE_NUM`, `SPECIAL_CHARGE_DESCRIPTION`, `SPECIAL_CHARGE_AMOUNT`) VALUES
(1, 'Heavy', '75.00'),
(2, 'Fragile', '70.00'),
(3, 'Handling', '25.00'),
(4, 'Special', '50.00'),
(5, 'Large', '50.00'),
(6, 'Glass', '20.00'),
(7, 'Flammable', '25.00'),
(8, 'Dangerous', '50.00'),
(9, 'High Value', '75.00'),
(10, 'Low Qty', '20.00');

-- --------------------------------------------------------

--
-- Table structure for table `TERRITORY`
--

CREATE TABLE `TERRITORY` (
  `TERRITORY_NUM` int(11) NOT NULL,
  `TERRITORY_NAME` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `TERRITORY`
--

INSERT INTO `TERRITORY` (`TERRITORY_NUM`, `TERRITORY_NAME`) VALUES
(1, 'East1'),
(2, 'East2'),
(3, 'East3'),
(4, 'South1'),
(5, 'South2'),
(6, 'West1'),
(7, 'West2'),
(8, 'West3'),
(9, 'North1'),
(10, 'North2');

-- --------------------------------------------------------

--
-- Table structure for table `VENDOR`
--

CREATE TABLE `VENDOR` (
  `VENDOR_NUM` int(11) NOT NULL,
  `VENDOR_NAME` varchar(30) DEFAULT NULL,
  `VENDOR_ADDRESS` varchar(30) DEFAULT NULL,
  `VENDOR_CITY` varchar(20) DEFAULT NULL,
  `VENDOR_STATE` varchar(2) DEFAULT NULL,
  `VENDOR_ZIP` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `VENDOR`
--

INSERT INTO `VENDOR` (`VENDOR_NUM`, `VENDOR_NAME`, `VENDOR_ADDRESS`, `VENDOR_CITY`, `VENDOR_STATE`, `VENDOR_ZIP`) VALUES
(1, 'Killian Wolfe', '761 Harvey St.', 'Farmingdale', 'NY', '11735'),
(2, 'Muhamed Cassidy', '8030 W. Paris Hill Ave.', 'Pudacah', 'KY', '42001'),
(3, 'Rehan Doyle', '322 Plymouth St.', 'La Crosse', 'WI', '54601'),
(4, 'Willie Gillespie', '7187 Cambridge St.', 'Lowell', 'MA', '01851'),
(5, 'Karla Bateman', '33 Jockey Hollow Circle', 'Fremont', 'OH', '43420'),
(6, 'Sabiha Coles', '14 Cedar Dr.', 'Honolulu', 'HI', '96815'),
(7, 'Ammarah Handley', '8382 Lyme Dr.', 'Hagerstown', 'MD', '21740'),
(8, 'Karishma Joseph', '8590 N. Roehampton Rd.', 'Kernersville', 'NC', '27284'),
(9, 'Shona Villa', '999 Gulf Ave.', 'Rego Park', 'NY', '11374'),
(10, 'Reyansh Mosley', '9956 N. Grand St.', 'Monsey', 'NY', '10952');

-- --------------------------------------------------------

--
-- Table structure for table `VENDOR_PART`
--

CREATE TABLE `VENDOR_PART` (
  `VENDOR_PART_NUM` int(11) NOT NULL,
  `VENDOR_PART_PRICE` decimal(10,2) DEFAULT NULL,
  `MIN_ORDER_QUANTITY` int(10) DEFAULT NULL,
  `PART_LEAD_TIME` char(10) DEFAULT NULL,
  `PART_NUM` int(11) DEFAULT NULL,
  `VENDOR_NUM` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `VENDOR_PART`
--

INSERT INTO `VENDOR_PART` (`VENDOR_PART_NUM`, `VENDOR_PART_PRICE`, `MIN_ORDER_QUANTITY`, `PART_LEAD_TIME`, `PART_NUM`, `VENDOR_NUM`) VALUES
(1, '150.00', 20, '5', 4, 6),
(2, '475.00', 25, '7', 6, 3),
(3, '65.00', 20, '10', 9, 3),
(4, '45.00', 30, '7', 3, 6),
(5, '145.00', 25, '8', 5, 8),
(6, '225.00', 30, '5', 1, 10),
(7, '135.00', 25, '12', 2, 8),
(8, '175.00', 20, '3', 5, 7),
(9, '150.00', 25, '5', 4, 5),
(10, '75.00', 30, '8', 10, 3),
(11, '550.00', 25, '9', 8, 4),
(12, '235.00', 25, '5', 7, 1),
(13, '75.00', 25, '10', 4, 2),
(14, '335.00', 20, '2', 10, 8),
(15, '50.00', 35, '5', 4, 9),
(16, '75.00', 35, '7', 7, 4),
(17, '360.00', 30, '3', 9, 5),
(18, '230.00', 25, '8', 6, 2),
(19, '340.00', 25, '2', 9, 9),
(20, '145.00', 30, '6', 8, 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `CUSTOMER`
--
ALTER TABLE `CUSTOMER`
  ADD PRIMARY KEY (`CUSTOMER_NUM`),
  ADD KEY `TERRITORY_NUM` (`TERRITORY_NUM`),
  ADD KEY `EMPLOYEE_ID` (`SALES_REP_ID`);

--
-- Indexes for table `INVOICE`
--
ALTER TABLE `INVOICE`
  ADD PRIMARY KEY (`INVOICE_NUM`),
  ADD KEY `CUSTOMER_NUM` (`CUSTOMER_NUM`),
  ADD KEY `ORDER_NUM` (`ORDER_NUM`);

--
-- Indexes for table `ORDERS`
--
ALTER TABLE `ORDERS`
  ADD PRIMARY KEY (`ORDER_NUM`),
  ADD KEY `CUSTOMER_NUM` (`CUSTOMER_NUM`),
  ADD KEY `SPECIAL_CHARGE_NUM` (`SPECIAL_CHARGE_NUM`);

--
-- Indexes for table `ORDER_DETAILS`
--
ALTER TABLE `ORDER_DETAILS`
  ADD PRIMARY KEY (`ORDER_DETAIL_NUM`),
  ADD KEY `PART_NUM` (`PART_NUM`),
  ADD KEY `ORDER_NUM` (`ORDER_NUM`);

--
-- Indexes for table `PART`
--
ALTER TABLE `PART`
  ADD PRIMARY KEY (`PART_NUM`);

--
-- Indexes for table `PAYMENT`
--
ALTER TABLE `PAYMENT`
  ADD PRIMARY KEY (`PAYMENT_NUM`),
  ADD KEY `CUSTOMER_NUM` (`CUSTOMER_NUM`),
  ADD KEY `INVOICE_NUM` (`INVOICE_NUM`);

--
-- Indexes for table `SALES_REP`
--
ALTER TABLE `SALES_REP`
  ADD PRIMARY KEY (`SALES_REP_ID`),
  ADD KEY `TERRITORY_NUM` (`TERRITORY_NUM`);

--
-- Indexes for table `SPECIAL_CHARGES`
--
ALTER TABLE `SPECIAL_CHARGES`
  ADD PRIMARY KEY (`SPECIAL_CHARGE_NUM`);

--
-- Indexes for table `TERRITORY`
--
ALTER TABLE `TERRITORY`
  ADD PRIMARY KEY (`TERRITORY_NUM`);

--
-- Indexes for table `VENDOR`
--
ALTER TABLE `VENDOR`
  ADD PRIMARY KEY (`VENDOR_NUM`);

--
-- Indexes for table `VENDOR_PART`
--
ALTER TABLE `VENDOR_PART`
  ADD PRIMARY KEY (`VENDOR_PART_NUM`),
  ADD KEY `PART_NUM` (`PART_NUM`),
  ADD KEY `VENDOR_NUM` (`VENDOR_NUM`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `CUSTOMER`
--
ALTER TABLE `CUSTOMER`
  MODIFY `CUSTOMER_NUM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `INVOICE`
--
ALTER TABLE `INVOICE`
  MODIFY `INVOICE_NUM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `ORDERS`
--
ALTER TABLE `ORDERS`
  MODIFY `ORDER_NUM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `ORDER_DETAILS`
--
ALTER TABLE `ORDER_DETAILS`
  MODIFY `ORDER_DETAIL_NUM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `PART`
--
ALTER TABLE `PART`
  MODIFY `PART_NUM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `PAYMENT`
--
ALTER TABLE `PAYMENT`
  MODIFY `PAYMENT_NUM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `SALES_REP`
--
ALTER TABLE `SALES_REP`
  MODIFY `SALES_REP_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `SPECIAL_CHARGES`
--
ALTER TABLE `SPECIAL_CHARGES`
  MODIFY `SPECIAL_CHARGE_NUM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `TERRITORY`
--
ALTER TABLE `TERRITORY`
  MODIFY `TERRITORY_NUM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `VENDOR`
--
ALTER TABLE `VENDOR`
  MODIFY `VENDOR_NUM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `VENDOR_PART`
--
ALTER TABLE `VENDOR_PART`
  MODIFY `VENDOR_PART_NUM` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `CUSTOMER`
--
ALTER TABLE `CUSTOMER`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`TERRITORY_NUM`) REFERENCES `TERRITORY` (`TERRITORY_NUM`),
  ADD CONSTRAINT `customer_ibfk_2` FOREIGN KEY (`SALES_REP_ID`) REFERENCES `SALES_REP` (`SALES_REP_ID`);

--
-- Constraints for table `INVOICE`
--
ALTER TABLE `INVOICE`
  ADD CONSTRAINT `invoice_ibfk_1` FOREIGN KEY (`CUSTOMER_NUM`) REFERENCES `CUSTOMER` (`CUSTOMER_NUM`),
  ADD CONSTRAINT `invoice_ibfk_2` FOREIGN KEY (`ORDER_NUM`) REFERENCES `ORDERS` (`ORDER_NUM`);

--
-- Constraints for table `ORDERS`
--
ALTER TABLE `ORDERS`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`CUSTOMER_NUM`) REFERENCES `CUSTOMER` (`CUSTOMER_NUM`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`SPECIAL_CHARGE_NUM`) REFERENCES `SPECIAL_CHARGES` (`SPECIAL_CHARGE_NUM`);

--
-- Constraints for table `ORDER_DETAILS`
--
ALTER TABLE `ORDER_DETAILS`
  ADD CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`PART_NUM`) REFERENCES `PART` (`PART_NUM`),
  ADD CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`ORDER_NUM`) REFERENCES `ORDERS` (`ORDER_NUM`);

--
-- Constraints for table `PAYMENT`
--
ALTER TABLE `PAYMENT`
  ADD CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`CUSTOMER_NUM`) REFERENCES `CUSTOMER` (`CUSTOMER_NUM`),
  ADD CONSTRAINT `payment_ibfk_2` FOREIGN KEY (`INVOICE_NUM`) REFERENCES `INVOICE` (`INVOICE_NUM`);

--
-- Constraints for table `SALES_REP`
--
ALTER TABLE `SALES_REP`
  ADD CONSTRAINT `sales_rep_ibfk_1` FOREIGN KEY (`TERRITORY_NUM`) REFERENCES `TERRITORY` (`TERRITORY_NUM`);

--
-- Constraints for table `VENDOR_PART`
--
ALTER TABLE `VENDOR_PART`
  ADD CONSTRAINT `vendor_part_ibfk_1` FOREIGN KEY (`PART_NUM`) REFERENCES `PART` (`PART_NUM`),
  ADD CONSTRAINT `vendor_part_ibfk_2` FOREIGN KEY (`VENDOR_NUM`) REFERENCES `VENDOR` (`VENDOR_NUM`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
