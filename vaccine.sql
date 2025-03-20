-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 21, 2025 at 04:25 PM
-- Server version: 11.6.2-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vaccine`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add contact', 7, 'add_contact'),
(26, 'Can change contact', 7, 'change_contact'),
(27, 'Can delete contact', 7, 'delete_contact'),
(28, 'Can view contact', 7, 'view_contact'),
(29, 'Can add faqs', 8, 'add_faqs'),
(30, 'Can change faqs', 8, 'change_faqs'),
(31, 'Can delete faqs', 8, 'delete_faqs'),
(32, 'Can view faqs', 8, 'view_faqs'),
(33, 'Can add vaccine', 9, 'add_vaccine'),
(34, 'Can change vaccine', 9, 'change_vaccine'),
(35, 'Can delete vaccine', 9, 'delete_vaccine'),
(36, 'Can view vaccine', 9, 'view_vaccine'),
(37, 'Can add faq', 10, 'add_faq'),
(38, 'Can change faq', 10, 'change_faq'),
(39, 'Can delete faq', 10, 'delete_faq'),
(40, 'Can view faq', 10, 'view_faq'),
(41, 'Can add profile', 11, 'add_profile'),
(42, 'Can change profile', 11, 'change_profile'),
(43, 'Can delete profile', 11, 'delete_profile'),
(44, 'Can view profile', 11, 'view_profile'),
(45, 'Can add appointment', 12, 'add_appointment'),
(46, 'Can change appointment', 12, 'change_appointment'),
(47, 'Can delete appointment', 12, 'delete_appointment'),
(48, 'Can view appointment', 12, 'view_appointment'),
(49, 'Can add vaccination record', 13, 'add_vaccinationrecord'),
(50, 'Can change vaccination record', 13, 'change_vaccinationrecord'),
(51, 'Can delete vaccination record', 13, 'delete_vaccinationrecord'),
(52, 'Can view vaccination record', 13, 'view_vaccinationrecord');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(6, 'pbkdf2_sha256$870000$PFD1OwtTwpjjIRCS6s7Nlk$xk5wmtlXj5/BOTm/ovHizhp3CIi5HtMBMi2ZVUb4x1I=', '2025-02-21 09:50:57.000000', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2024-02-11 04:54:48.000000'),
(8, 'pbkdf2_sha256$600000$PHpbEIs0vAPgtLIdr80bv1$GoHVsBRvleWW+yqnhUCnt2T1V9V/Ig4j+TL6zK8lhj4=', '2024-02-11 10:43:51.458283', 0, 'John', 'John', 'Carter', 'john@gmail.com', 0, 1, '2024-02-11 09:26:49.480945'),
(10, 'pbkdf2_sha256$600000$q25H0SydrjuaCdO6VKcPvd$NWPDJez0nAk07QMHefMG61XEQGYDKp6q32i8Atx+VR4=', '2024-02-11 10:51:47.000000', 0, 'cityhospital', 'City Hospital', '', 'cityhospital@gmail.com', 0, 1, '2024-02-11 09:55:12.000000'),
(11, 'pbkdf2_sha256$870000$mR83ZlT9X9UUnv4esOFiRo$f0v2jRC3i5qoe/RATLx953tRR9UTvHtKQrS85CZC+yc=', '2025-02-21 15:23:49.903688', 0, 'admin1', 'Shvet', 'patel', 'shvet@gmail.com', 0, 1, '2024-09-29 11:40:41.000000'),
(12, 'pbkdf2_sha256$720000$xq2rn07iQ60QflnqLcKt1F$DvYa9E7zSFNDpx+95tSCLcnLGuQZeG1c5EdYWuXiWFI=', '2024-09-29 11:58:16.511021', 0, 'hospital1', 'Nootan General Hospital', '', 'NootanHospital@gmail.com', 0, 1, '2024-09-29 11:54:19.939239'),
(16, 'pbkdf2_sha256$870000$AGkBtb61ofHPGnBMYbGw9S$6pMaL24P2kQFa1t19tZ+xQ9cYK3FlJ0qNE9fApscvac=', '2025-02-21 10:04:30.000000', 1, 'hospital2', 'VADNAGAR HOSPITAL', '', 'VADNAGAR@gmail.com', 1, 1, '2025-02-21 10:04:19.000000'),
(18, 'pbkdf2_sha256$870000$6Tvqf6R7Mbque4EXroJQw5$uRQ2kTGXalymcWzr22iwzxs3gGxy+h5Rw/5VBdbK3u4=', NULL, 0, 'ved001', 'ved', 'patel', 'ved@gmail.com', 0, 1, '2025-02-21 12:09:14.806255');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `childvc_appointment`
--

CREATE TABLE `childvc_appointment` (
  `aid` int(11) NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `hospital_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `vac_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `childvc_appointment`
--

INSERT INTO `childvc_appointment` (`aid`, `datetime`, `status`, `created_at`, `hospital_id`, `user_id`, `vac_id`) VALUES
(1, '2024-02-29 18:00:00.000000', 'Pending', '2024-02-11 10:27:13.968333', 10, 8, 3),
(2, '2024-09-30 11:31:00.000000', 'Approved', '2024-09-29 11:55:10.098265', 12, 11, 2),
(3, '2025-02-18 15:47:55.000000', 'Approved', '2025-02-18 15:48:18.329862', 10, 10, 2),
(5, '2025-02-25 23:29:00.000000', 'Approved', '2025-02-21 12:54:30.651288', 10, 11, 14);

-- --------------------------------------------------------

--
-- Table structure for table `childvc_contact`
--

CREATE TABLE `childvc_contact` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `msg` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `childvc_contact`
--

INSERT INTO `childvc_contact` (`id`, `name`, `email`, `phone`, `msg`) VALUES
(1, ',nc,mc,mn,mn', 'john@gmail.com', 728964529834, 'jkfnlksjndflskjdn'),
(2, 'bhavin', 'bhavinasodariya2911@gmail.com', 7990187017, 'jjjjj'),
(3, 'shvet', 'patelshvet5825@gmail.com', 9023751034, 'hyyy');

-- --------------------------------------------------------

--
-- Table structure for table `childvc_faq`
--

CREATE TABLE `childvc_faq` (
  `fid` int(11) NOT NULL,
  `question` longtext NOT NULL,
  `answer` longtext NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `u_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `childvc_faq`
--

INSERT INTO `childvc_faq` (`fid`, `question`, `answer`, `datetime`, `u_id_id`) VALUES
(1, 'How do vaccines work?', 'Vaccines help your child’s immune system fight off infections efficiently. They do so by sparking the response of their immune system to specific diseases. So, if the bacteria or virus tries to invade their body in the future, the immune system will already know how to protect the body against it.', '2023-12-25 11:39:04.507164', NULL),
(2, 'What diseases do vaccines protect against?', 'Through vaccinations, you can immunize your baby against the following serious diseases: Chickenpox, Diphtheria, Influenza, Measles, Mumps, Polio, Rotavirus, Tetanus, Tuberculosis, Whooping cough and others', '2023-12-25 11:40:54.335987', NULL),
(3, 'Are vaccines safe?', 'Vaccines are generally very safe. It is far more likely for your child to be hurt by a disease that is vaccine-preventable, than by a vaccine. All vaccines have to go through a rigorous procedure of safety testing. This also includes conducting clinical trials before approving them for clinical use.', '2023-12-25 11:41:16.327151', NULL),
(4, 'Will breastfeeding protect my baby from infectious diseases?', 'There are some antibodies present in the breast milk that can be passed to the baby, especially in a couple of days after birth. However, after a few weeks, this passive immunity starts wearing off. After this, breastfeeding provides little to no protection from serious infectious diseases. Therefore, even if you are planning on breastfeeding long-term, you have to get your child vaccinated.', '2023-12-25 11:41:32.690185', NULL),
(5, 'Can my baby handle all of these vaccines?', 'Yes. Some parents are worried that so many vaccinations can overload the immune system of your child. However, it is important to note that your child is exposed to thousands of germs every single day. A sore throat or a common cold will put more stress on the immune system of the child than vaccines.', '2023-12-25 11:41:49.727251', NULL),
(6, 'What if my baby is taking antibiotics? Can they still get vaccinated?', 'Yes. Even if your child has a low-grade fever, a mild illness and is taking an antibiotic, he or she can still get vaccinated. If you are unsure, talk to your pediatrician about it.', '2023-12-25 11:42:05.388002', NULL),
(7, 'Can I delay the vaccine schedule?', 'Following the recommended vaccine schedule is one of the best ways of protecting your child against serious infectious diseases. Every time you delay a vaccination, you are putting your child at risk. If for some reason, delaying the vaccine schedule is inevitable, you can talk to your paediatrician regarding the adjustment.', '2023-12-25 11:42:19.488562', NULL),
(8, 'Do vaccines have side effects?', 'Vaccinations are mostly safe and usually, babies don’t usually have any side effects from the immunization. However, some children may have side effects to certain vaccines. They are usually minor and go away in a few days. Here are some of the common side effects a child might face: Low-grade fever for a few days after the vaccinations. The doctor might recommend paracetamol drops to relieve the symptoms.', '2023-12-25 11:43:04.720820', NULL),
(9, 'Which are vaccine is safe for 6 month older child?', 'All vaccines are safe for children and also these are authorized by GOVT. .', '2023-12-25 12:15:00.549610', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `childvc_profile`
--

CREATE TABLE `childvc_profile` (
  `profile_id` int(11) NOT NULL,
  `profile_image` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `role` varchar(20) NOT NULL,
  `bdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `childvc_profile`
--

INSERT INTO `childvc_profile` (`profile_id`, `profile_image`, `address`, `phone`, `user_id`, `role`, `bdate`) VALUES
(1, 'img3.png', '', NULL, 6, '1', NULL),
(3, '2_img_TUp6rqL.jpg', 'Surat', 827628347, 8, '1', NULL),
(5, 'img3.png', '', NULL, 10, '2', NULL),
(6, 'img3.png', '', 9023751034, 11, '1', '2003-09-11'),
(7, 'img3.png', '', NULL, 12, '2', NULL),
(12, 'img3.png', '', 9023751034, 16, '1', '2024-09-24'),
(16, '2_img_ft9coJp.jpg', 'vadnagar', 9023751034, 18, '1', '1911-01-03');

-- --------------------------------------------------------

--
-- Table structure for table `childvc_vaccinationrecord`
--

CREATE TABLE `childvc_vaccinationrecord` (
  `id` bigint(20) NOT NULL,
  `child_name` varchar(100) NOT NULL,
  `vaccine_name` varchar(100) NOT NULL,
  `status` varchar(20) NOT NULL,
  `parent_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `childvc_vaccine`
--

CREATE TABLE `childvc_vaccine` (
  `vid` int(11) NOT NULL,
  `vname` varchar(100) NOT NULL,
  `vdiscription` varchar(100) NOT NULL,
  `vprice` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `childvc_vaccine`
--

INSERT INTO `childvc_vaccine` (`vid`, `vname`, `vdiscription`, `vprice`) VALUES
(1, 'DTwP /DTaP1, Hib-1, IPV-1, Hep B2, PCV 1,Rota-1', '6 weeks', 150),
(2, 'DTwP /DTaP2, Hib-2, IPV-2, Hep B3, PCV 2, Rota-2', '10 weeks', 150),
(3, 'Influenza-1', '6 Months', 150),
(4, 'DTwP /DTaP3, Hib-3, IPV-3, Hep B4, PCV 3, Rota-3*', '14Weeks', 150),
(5, 'Influenza -2', '7 Months', 200),
(6, 'Typhoid Conjugate Vaccine', '6 - 9 Months', 220),
(7, 'MMR 1 (Mumps, measles, Rubella)', '9 Months', 255),
(8, 'Hepatitis A- 1', '12 Months', 500),
(9, 'PCV Booster', '12 - 15 Months', 580),
(10, 'MMR 2, Varicella', '15 Months', 400),
(11, 'DTwP /DTaP, Hib, IPV', '16 – 18 Months', 620),
(12, 'Hepatitis A- 2**, Varicella 2', '18 – 19 Months', 800),
(13, 'DTwP /DTaP, IPV, MMR 3', '4 – 6 years', 620),
(14, 'HPV (2 doses)', '9 – 15years (Girls)', 380),
(15, 'Tdap/ Td', '10 – 12 Years', 560),
(16, 'Annual Influenza Vaccine', '2nd, 3rd, 4th and 5th Year', 290);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(16, '2024-02-11 04:58:32.820434', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"Profile image\"]}}]', 11, 6),
(17, '2024-02-11 09:47:40.541307', '7', 'cityhospital', 3, '', 4, 6),
(18, '2024-02-11 09:51:42.397546', '9', 'cityhospital', 3, '', 4, 6),
(19, '2024-02-11 10:15:13.819485', '1', 'DTwP /DTaP1, Hib-1, IPV-1, Hep B2, PCV 1,Rota-1', 1, '[{\"added\": {}}]', 9, 6),
(20, '2024-02-11 10:15:30.961027', '2', 'DTwP /DTaP2, Hib-2, IPV-2, Hep B3, PCV 2, Rota-2', 1, '[{\"added\": {}}]', 9, 6),
(21, '2024-02-11 10:15:49.218148', '3', 'Influenza-1', 1, '[{\"added\": {}}]', 9, 6),
(22, '2024-02-11 10:27:53.791951', '1', 'John', 2, '[{\"changed\": {\"fields\": [\"User\"]}}]', 12, 6),
(23, '2024-09-29 11:56:33.084709', '2', 'admin1', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 12, 6),
(24, '2024-09-29 11:58:54.859309', '2', 'admin1', 2, '[]', 12, 6),
(25, '2025-02-18 15:47:43.130152', '2', 'admin1', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 12, 6),
(26, '2025-02-18 15:48:18.331202', '3', 'cityhospital', 1, '[{\"added\": {}}]', 12, 6),
(27, '2025-02-21 09:52:45.574861', '10', 'hospital2', 2, '[{\"changed\": {\"fields\": [\"Address\", \"Phone\", \"Role\"]}}]', 11, 6),
(28, '2025-02-21 09:53:12.798592', '4', 'VIDHI001', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 12, 6),
(29, '2025-02-21 10:02:45.215601', '4', 'VIDHI001', 3, '', 12, 6),
(30, '2025-02-21 10:03:44.457844', '14', 'VIDHI001', 3, '', 4, 6),
(31, '2025-02-21 10:03:49.247288', '15', 'hospital2', 3, '', 4, 6),
(32, '2025-02-21 10:06:04.544120', '2', 'admin1', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 12, 6),
(33, '2025-02-21 11:52:14.840348', '16', 'hospital2', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Staff status\", \"Superuser status\"]}}]', 4, 6),
(34, '2025-02-21 12:00:31.052598', '17', 'kuntal019', 3, '', 4, 6),
(35, '2025-02-21 12:07:36.210795', '2', 'admin1', 2, '[]', 12, 6),
(36, '2025-02-21 12:17:53.236700', '6', 'admin', 2, '[]', 4, 6),
(37, '2025-02-21 12:18:04.257110', '11', 'admin1', 2, '[]', 4, 6),
(38, '2025-02-21 12:18:12.022100', '10', 'cityhospital', 2, '[]', 4, 6),
(39, '2025-02-21 12:18:55.214450', '2', 'bhavin', 2, '[]', 7, 6),
(40, '2025-02-21 12:19:20.279112', '3', 'shvet', 1, '[{\"added\": {}}]', 7, 6),
(41, '2025-02-21 12:20:08.930469', '16', 'ved001', 2, '[{\"changed\": {\"fields\": [\"Bdate\", \"Profile image\", \"Address\", \"Phone\"]}}]', 11, 6),
(42, '2025-02-21 12:20:21.357371', '12', 'hospital2', 2, '[{\"changed\": {\"fields\": [\"Bdate\", \"Phone\"]}}]', 11, 6),
(43, '2025-02-21 12:35:15.926297', '6', 'admin1', 2, '[{\"changed\": {\"fields\": [\"Bdate\", \"Phone\"]}}]', 11, 6),
(44, '2025-02-21 12:41:53.616156', '2', 'DTwP /DTaP2, Hib-2, IPV-2, Hep B3, PCV 2, Rota-2', 2, '[]', 9, 6),
(45, '2025-02-21 12:42:25.972249', '4', 'DTwP /DTaP3, Hib-3, IPV-3, Hep B4, PCV 3, Rota-3*', 1, '[{\"added\": {}}]', 9, 6),
(46, '2025-02-21 12:42:45.897722', '5', 'Influenza -2', 1, '[{\"added\": {}}]', 9, 6),
(47, '2025-02-21 12:43:09.012442', '6', 'Typhoid Conjugate Vaccine', 1, '[{\"added\": {}}]', 9, 6),
(48, '2025-02-21 12:43:34.092092', '7', 'MMR 1 (Mumps, measles, Rubella)', 1, '[{\"added\": {}}]', 9, 6),
(49, '2025-02-21 12:44:04.345979', '8', 'Hepatitis A- 1', 1, '[{\"added\": {}}]', 9, 6),
(50, '2025-02-21 12:44:37.326249', '9', 'PCV Booster', 1, '[{\"added\": {}}]', 9, 6),
(51, '2025-02-21 12:44:57.937330', '10', 'MMR 2, Varicella', 1, '[{\"added\": {}}]', 9, 6),
(52, '2025-02-21 12:45:14.916744', '11', 'DTwP /DTaP, Hib, IPV', 1, '[{\"added\": {}}]', 9, 6),
(53, '2025-02-21 12:45:28.563645', '12', 'Hepatitis A- 2**, Varicella 2', 1, '[{\"added\": {}}]', 9, 6),
(54, '2025-02-21 12:45:50.307141', '13', 'DTwP /DTaP, IPV, MMR 3', 1, '[{\"added\": {}}]', 9, 6),
(55, '2025-02-21 12:46:16.802717', '14', 'HPV (2 doses)', 1, '[{\"added\": {}}]', 9, 6),
(56, '2025-02-21 12:46:33.573114', '15', 'Tdap/ Td', 1, '[{\"added\": {}}]', 9, 6),
(57, '2025-02-21 12:46:50.564117', '16', 'Annual Influenza Vaccine', 1, '[{\"added\": {}}]', 9, 6),
(58, '2025-02-21 15:24:34.780394', '5', 'admin1', 2, '[{\"changed\": {\"fields\": [\"Hospital\", \"Status\"]}}]', 12, 6);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(12, 'childvc', 'appointment'),
(7, 'childvc', 'contact'),
(10, 'childvc', 'faq'),
(8, 'childvc', 'faqs'),
(11, 'childvc', 'profile'),
(13, 'childvc', 'vaccinationrecord'),
(9, 'childvc', 'vaccine'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-12-25 11:13:54.466719'),
(2, 'auth', '0001_initial', '2023-12-25 11:13:55.362001'),
(3, 'admin', '0001_initial', '2023-12-25 11:13:55.530369'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-12-25 11:13:55.546357'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-12-25 11:13:55.562325'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-12-25 11:13:55.660754'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-12-25 11:13:55.758000'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-12-25 11:13:55.794895'),
(9, 'auth', '0004_alter_user_username_opts', '2023-12-25 11:13:55.816945'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-12-25 11:13:55.907404'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-12-25 11:13:55.915383'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-12-25 11:13:55.938364'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-12-25 11:13:55.991721'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-12-25 11:13:56.027470'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-12-25 11:13:56.066955'),
(16, 'auth', '0011_update_proxy_permissions', '2023-12-25 11:13:56.093805'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-12-25 11:13:56.128754'),
(18, 'childvc', '0001_initial', '2023-12-25 11:13:56.160639'),
(19, 'childvc', '0002_alter_contact_email', '2023-12-25 11:13:56.173598'),
(20, 'childvc', '0003_alter_contact_phone', '2023-12-25 11:13:56.237478'),
(21, 'childvc', '0004_vaccine_faqs', '2023-12-25 11:13:56.385447'),
(22, 'childvc', '0005_remove_faqs_vid_alter_faqs_datetime', '2023-12-25 11:13:57.899610'),
(23, 'childvc', '0006_faqs_vid', '2023-12-25 11:20:50.846016'),
(24, 'sessions', '0001_initial', '2023-12-25 11:20:50.912843'),
(25, 'childvc', '0007_faq_delete_faqs', '2023-12-25 11:34:52.518996'),
(26, 'childvc', '0008_alter_faq_answer_alter_faq_question', '2023-12-25 11:38:25.692598'),
(27, 'childvc', '0009_faq_u_id', '2023-12-25 12:09:45.537236'),
(28, 'childvc', '0010_hospital_appointment', '2024-02-11 04:48:25.645916'),
(29, 'childvc', '0011_profile_delete_appointment_delete_hospital', '2024-02-11 04:48:25.785125'),
(30, 'happ', '0001_initial', '2024-02-11 04:48:25.814789'),
(31, 'happ', '0002_delete_contact', '2024-02-11 04:48:25.831393'),
(32, 'childvc', '0012_alter_profile_address_alter_profile_phone', '2024-02-11 04:52:00.046759'),
(33, 'childvc', '0013_alter_profile_phone', '2024-02-11 04:53:54.910450'),
(34, 'childvc', '0014_appointment', '2024-02-11 09:25:07.501003'),
(35, 'childvc', '0015_profile_role', '2024-02-11 09:46:40.799314'),
(36, 'childvc', '0016_appointment_vac', '2024-02-11 09:58:54.596168'),
(37, 'childvc', '0017_vaccine_vprice_alter_appointment_datetime', '2024-09-29 11:38:49.266283'),
(38, 'childvc', '0018_vaccinationrecord', '2025-02-21 09:46:51.648659'),
(39, 'childvc', '0019_profile_bdate_alter_profile_user', '2025-02-21 09:46:54.111643');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0vokdggp27epflwu5lmc1cyo2e5wcrhe', '.eJxVjDsOwjAQBe_iGln-xD9Kes5grb1rHEC2FCcV4u4QKQW0b2bei0XY1hq3QUuckZ2ZZaffLUF-UNsB3qHdOs-9rcuc-K7wgw5-7UjPy-H-HVQY9VtrOWFImgK64sgIoAmEouIhQwlJWmE8KUJvQTujQBEFL7UXTgrKSbH3B_wKODQ:1rZ6QV:sDfmJmC0JVuD48K8oO0HqaYTHdEBfmliDkYnl2Qq39U', '2024-02-25 09:47:07.289049'),
('2tma8cmrd7w2cszxratihojmx30txyom', '.eJxVjDsOwjAUBO_iGlkvxp-Ykj5nsLx2Hg4gR4qTCnF3iJQC2p2ZfYkQt7WErY1LmLK4CCVOvxtieox1B_ke622Waa7rMkHuijxok8Ocx-f1cP8OSmzlW5seLlsmRd4zzkQ-Je6iNujYKgcN1yuCMRqsmYyy5PrkGBkMQIn3B9taOCg:1rHj7O:HF9tOU5bZ2agxv_nuGePlNGr-Q4TdDxVhN6VvzfXifo', '2024-01-08 11:27:34.038090'),
('nad2g9iqe4hp65zfrkqlpgkvdszhfrsq', '.eJxVjDsOwjAYg--SGUV5tInKyM4Zov8VUkCp1LRTxd1ppQ5gefJne1MJ1qWktcmcRlZXZXt1-Q0R6CX1IPyE-pg0TXWZR9RHRZ-06fvE8r6d3b-DAq3sa_Rd9MQxB_bCzlncFYgpGrPbR8NxQONBcm_BQEZiH4FCJ24Q7NTnCyTIOQM:1tlPes:lOr2hAS3_yJrriMT8NvJuvIGWl6NMtuGhdogpKxqnT0', '2025-03-07 09:49:22.481980'),
('os00w456jj96oddlkupyxysfuqfppbxm', '.eJxVjDsOwjAQBe_iGllr4ngTSvqcIfJ-jAPIlvKpEHeHSCmgfTPzXmaM25rHbdF5nMRcjPPm9DtS5IeWncg9llu1XMs6T2R3xR50sUMVfV4P9-8gxyV_a_ZdEnDaBi-RQujYIUTokantGEShwaCKhNooOAZK0vRnZNcmcpjM-wMWnziP:1tlPfh:ZQvjxFtrwR3pxM3omMS87ySNpmGDFGATkEa_5I7OIYc', '2025-03-07 09:50:13.999117'),
('p5ofd2gwd5c3xtyx7wnyecc1bmdmoeis', '.eJxVjEEOwiAQRe_C2hCglAGX7j1DM8wMtmpoUtqV8e7apAvd_vfef6kBt3UctibLMLE6K2vV6XfMSA-pO-E71tusaa7rMmW9K_qgTV9nluflcP8ORmzjt0ZfiAvZXpwvHQQfgJPkmCkXA2B6gtJxMNYHAYwpicMYjeHgUvIdqfcHIf04HA:1tl3e9:9FEHokrYM1j2vlGJg8yzQWTCoOp8NpT0eBAntGFYzp0', '2025-03-06 10:19:09.076725'),
('pjrspwwj2pnwg7zdmga38410ra0nali0', '.eJxVjEEOwiAQRe_C2hCglAGX7j1DM8wMtmpoUtqV8e7apAvd_vfef6kBt3UctibLMLE6K2vV6XfMSA-pO-E71tusaa7rMmW9K_qgTV9nluflcP8ORmzjt0ZfiAvZXpwvHQQfgJPkmCkXA2B6gtJxMNYHAYwpicMYjeHgUvIdqfcHIf04HA:1tlUsY:x7qcOxa9MCFuB0Bx_M__Eg2QlDn29xoWTEnKpybDKQQ', '2025-03-07 15:23:50.086781'),
('qfon0sx8nduuggmnen2aupv9ehuwt7ri', '.eJxVjEEOgjAQRe_StWk6UGnHpXvO0AydGYsaSCisjHdXEha6_e-9_zKJtrWkrcqSRjYXA86cfseB8kOmnfCdptts8zytyzjYXbEHrbafWZ7Xw_07KFTLt_akGrIKRGgYGkRFJ1kdOeGzRt85LyzAHGDggBEI0WPbYvaNdE7N-wMlXDh3:1rZ7R5:i5PmD7R_OG-fgpM-Kj3m4a9TFFoUP2jj4nfRWHkXDEE', '2024-02-25 10:51:47.495434'),
('rnt6lwu4a0saklb9gt7s1ly9xlg1fjzs', '.eJxVjEEOwiAQRe_C2pBKKTgu3fcMhGFmpGogKe3KeHdD0oVu_3vvv1WI-5bD3ngNC6mrcur0u2FMTy4d0COWe9Wplm1dUHdFH7TpuRK_bof7d5Bjy712Ft3IdjJA3rpJRIxnZ852lIQRSThZAGcEcOAR0QtcgAYCI4lI1OcL-ek5Gg:1tlPgP:NhSU6X8WbTKPFDJO4SgSC0XLg0dieZYm6zR5qUgR2jM', '2025-03-07 09:50:57.063900'),
('wqn7da3kf5sy1c6idps5nzmvkkqjs4s4', '.eJxVjDsOwjAUBO_iGlkvxp-Ykj5nsLx2Hg4gR4qTCnF3iJQC2p2ZfYkQt7WErY1LmLK4CCVOvxtieox1B_ke622Waa7rMkHuijxok8Ocx-f1cP8OSmzlW5seLlsmRd4zzkQ-Je6iNujYKgcN1yuCMRqsmYyy5PrkGBkMQIn3B9taOCg:1rHj7N:vNvViSxnzJJwbr60FQm2NYSKIikVkCsdMSgWT4B8VP0', '2024-01-08 11:27:33.109573'),
('yubnyhamojltlshf301gr8btxb8hr8jo', '.eJxVjEEOwiAQRe_C2pAOFCgu3XsGMgyDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3EWoMTpd4xID647SXestyap1XWZo9wVedAury3x83K4fwcFe_nWnnPOmCwjJAdZZ1Dagxmsn0YwmtB443y0Rnt2BMNkSSnExCNlC2TE-wMQqTgR:1susZ6:UzqUaku0Xuj_J5eziuP328iXHvyFjWG4GhwzEIpzmp8', '2024-10-13 11:58:16.679610');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `name`, `status`) VALUES
(1, 'Vishal1 Gupta', 1),
(2, 'Vishal2 Gupta', 1),
(3, 'Vishal3 Gupta', 1),
(4, 'Vishal4 Gupta', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `childvc_appointment`
--
ALTER TABLE `childvc_appointment`
  ADD PRIMARY KEY (`aid`),
  ADD KEY `childvc_appointment_hospital_id_82fd80ef_fk_auth_user_id` (`hospital_id`),
  ADD KEY `childvc_appointment_user_id_edc691bb_fk_auth_user_id` (`user_id`),
  ADD KEY `childvc_appointment_vac_id_84e56652_fk_childvc_vaccine_vid` (`vac_id`);

--
-- Indexes for table `childvc_contact`
--
ALTER TABLE `childvc_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `childvc_faq`
--
ALTER TABLE `childvc_faq`
  ADD PRIMARY KEY (`fid`),
  ADD KEY `childvc_faq_u_id_id_53badd63_fk_auth_user_id` (`u_id_id`);

--
-- Indexes for table `childvc_profile`
--
ALTER TABLE `childvc_profile`
  ADD PRIMARY KEY (`profile_id`),
  ADD UNIQUE KEY `childvc_profile_user_id_e6018891_uniq` (`user_id`);

--
-- Indexes for table `childvc_vaccinationrecord`
--
ALTER TABLE `childvc_vaccinationrecord`
  ADD PRIMARY KEY (`id`),
  ADD KEY `childvc_vaccinationrecord_parent_id_3f7eb11f_fk_auth_user_id` (`parent_id`);

--
-- Indexes for table `childvc_vaccine`
--
ALTER TABLE `childvc_vaccine`
  ADD PRIMARY KEY (`vid`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `childvc_appointment`
--
ALTER TABLE `childvc_appointment`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `childvc_contact`
--
ALTER TABLE `childvc_contact`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `childvc_faq`
--
ALTER TABLE `childvc_faq`
  MODIFY `fid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `childvc_profile`
--
ALTER TABLE `childvc_profile`
  MODIFY `profile_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `childvc_vaccinationrecord`
--
ALTER TABLE `childvc_vaccinationrecord`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `childvc_vaccine`
--
ALTER TABLE `childvc_vaccine`
  MODIFY `vid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `childvc_appointment`
--
ALTER TABLE `childvc_appointment`
  ADD CONSTRAINT `childvc_appointment_hospital_id_82fd80ef_fk_auth_user_id` FOREIGN KEY (`hospital_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `childvc_appointment_user_id_edc691bb_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `childvc_appointment_vac_id_84e56652_fk_childvc_vaccine_vid` FOREIGN KEY (`vac_id`) REFERENCES `childvc_vaccine` (`vid`);

--
-- Constraints for table `childvc_faq`
--
ALTER TABLE `childvc_faq`
  ADD CONSTRAINT `childvc_faq_u_id_id_53badd63_fk_auth_user_id` FOREIGN KEY (`u_id_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `childvc_profile`
--
ALTER TABLE `childvc_profile`
  ADD CONSTRAINT `childvc_profile_user_id_e6018891_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `childvc_vaccinationrecord`
--
ALTER TABLE `childvc_vaccinationrecord`
  ADD CONSTRAINT `childvc_vaccinationrecord_parent_id_3f7eb11f_fk_auth_user_id` FOREIGN KEY (`parent_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
