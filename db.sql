/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - online_website
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`online_website` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `online_website`;

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `reciever_id` int(11) DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`sender_id`,`reciever_id`,`message`,`date`) values (1,3,15,'hlooo','2022-01-22 15:31:23'),(2,15,3,'hai','2022-01-22 15:31:26'),(3,3,15,'huhi','2022-01-22 15:44:17'),(4,3,11,'hai','2022-01-29 10:58:34'),(5,3,11,'hello','2022-01-29 10:58:39'),(6,3,11,'aswani','2022-01-29 10:58:50'),(7,15,3,'ok','2022-01-29 10:58:50'),(8,3,11,'ok','2022-01-29 11:03:12'),(9,3,11,'helo','2022-01-29 11:05:50'),(10,3,11,'hello','2022-01-29 11:09:09'),(11,3,11,'he','2022-01-29 11:10:55'),(12,3,11,'hello','2022-01-29 11:11:00'),(13,3,11,'hai','2022-01-29 11:12:05'),(14,3,11,'lknk','2022-01-29 13:31:37'),(15,3,11,'dxfchgjhkjk','2022-01-29 13:31:55'),(16,3,11,'hiiii','2022-01-29 13:34:52'),(17,11,3,'helloo','2022-01-29 13:34:52'),(18,3,11,'dfghjk','2022-01-29 13:42:39'),(19,3,11,'hellloooooo','2022-01-29 13:43:27'),(20,11,3,'hifcgvbh','2022-01-29 13:43:27'),(21,7,3,'hoi','2022-01-29 13:55:31'),(22,3,11,'hiiii','2022-01-29 13:58:35'),(23,11,3,'hoooo','2022-01-29 14:00:02'),(24,8,3,'hello','2022-01-29 16:22:00'),(25,3,11,'fe','2022-02-05 10:48:19'),(26,3,20,'adfsh','2022-02-10 15:03:26'),(27,3,20,'dgsdfh','2022-02-10 15:04:42'),(28,7,3,'aSCxfbcv','2022-02-10 15:18:04'),(29,10,20,'asdfhnm','2022-02-10 16:26:20'),(30,10,20,'asdfghm','2022-02-10 16:27:57'),(31,18,20,'helloo','2022-02-10 16:33:31'),(32,20,18,'wdasfh','2022-02-10 16:53:36'),(33,20,18,'hiiiii','2022-02-10 16:53:42'),(34,18,20,'hiiii','2022-02-10 16:54:40');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `complaint` varchar(500) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`login_id`,`complaint`,`reply`,`date`) values (1,1,'		\r\n	hkfd','gukkgg','2022-01-22 10:43:06'),(2,17,'		\r\n	hkjkzKk','we will take ','2022-01-22 14:18:56'),(3,17,'		\r\n	hkjkzKk','pending','2022-01-22 14:19:22'),(4,17,'		\r\n	hhhh','pk','2022-01-22 14:20:43'),(5,17,'		\r\n	hhhh','pending','2022-01-22 14:21:03'),(6,17,'		not \r\n	','ok','2022-01-22 14:21:27'),(7,17,'		not \r\n	','fine','2022-01-22 14:21:46'),(8,17,'		hello\r\n\r\n	','fine ok','2022-01-22 14:23:21'),(9,8,'		hishi\r\n	','pending','2022-01-29 15:56:41'),(10,8,'		hishi\r\n	','pending','2022-01-29 15:57:08'),(11,8,'		hishi\r\n	','pending','2022-01-29 15:57:43'),(12,8,'		hishi\r\n	','pending','2022-01-29 15:57:57'),(13,8,'		hishi\r\n	','pending','2022-01-29 15:58:03'),(14,8,'		hishi\r\n	','pending','2022-01-29 15:58:57'),(15,8,'		hishi\r\n	','pending','2022-01-29 15:59:58'),(16,8,'		hishi\r\n	','pending','2022-01-29 16:00:53'),(17,8,'		hishi\r\n	','pending','2022-01-29 16:01:25'),(18,8,'		hishi\r\n	','pending','2022-01-29 16:01:57'),(19,8,'		hishi\r\n	','pending','2022-01-29 16:02:20'),(20,8,'		\r\n	vvvv','pending','2022-01-29 16:15:40'),(21,3,'		\r\n	czfd','pending','2022-02-05 11:26:55'),(22,3,'			ASGDGH\r\n		','pending','2022-02-10 15:02:11'),(23,3,'			SZDFGN\r\n		','pending','2022-02-10 15:02:25'),(24,7,'asfdk,','pending','2022-02-10 15:20:57'),(25,7,'sdfhm','pending','2022-02-10 15:23:46'),(26,10,'asdfk','pending','2022-02-10 16:30:52'),(27,10,'asdfk','pending','2022-02-10 16:31:04');

/*Table structure for table `institution` */

DROP TABLE IF EXISTS `institution`;

CREATE TABLE `institution` (
  `institution_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `institution_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`institution_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `institution` */

insert  into `institution`(`institution_id`,`login_id`,`institution_name`,`place`,`phone`,`email`,`pincode`) values (1,3,'sngce','kochi','953877564654646','sngce@gmail.com','683556'),(2,17,'rajagiri','kochi','79879797','rajagiri@gmail.com','683554'),(3,19,'ilahia','muvattupuzha','797977978','ilahia@gmail.com','63578');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'abeel123','12345','user'),(3,'sngce123','12345','institution'),(4,'rahul123','12345','pending'),(5,'abeel148','12345','pending'),(10,'ram123','12345','user'),(7,'akash123','12345','speaker'),(8,'admin','admin','admin'),(11,'raju123','12345','speaker'),(12,'akhil123','12345','speaker'),(15,'raghu123','1345','speaker'),(14,'aswani123','12345','speaker'),(17,'rajagiri123','12345','institution'),(18,'aswathi','12345','user'),(19,'ilahia','12345','institution'),(20,'roopesh123','12345','speaker');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `institution_id` int(11) DEFAULT NULL,
  `speaker_id` int(11) DEFAULT NULL,
  `class_for` varchar(50) DEFAULT NULL,
  `class_date` varchar(50) DEFAULT NULL,
  `class_time` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `request` */

/*Table structure for table `speaker` */

DROP TABLE IF EXISTS `speaker`;

CREATE TABLE `speaker` (
  `speaker_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `subject` varchar(50) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`speaker_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `speaker` */

insert  into `speaker`(`speaker_id`,`login_id`,`first_name`,`last_name`,`place`,`phone`,`email`,`description`,`subject`,`image`,`designation`) values (4,11,'raju','ram','kochi','54646','sngca01@sngce.ac.in','jhjkh','Computer Science','static/99cff963-fcaf-4e4a-9499-b1a4f9854904Untitled design (55)_0.png','jhj'),(2,7,'aksh','ilsh','kochi','95398779878','akash@gmail.com','testing','motivationaal','static/64b1d7f5-fd17-42a4-a891-40dddcd63913Untitled design (55)_0.png','sample'),(5,12,'akhil','raj','kochi','7979797977','akhil@gmail.com','I am tech savvy','Computer Science','static/99cff963-fcaf-4e4a-9499-b1a4f9854904Untitled design (55)_0.png','developer'),(8,15,'raghu','nandan ','','987899555','raghu@gmail.com','','Automobile','static/99cff963-fcaf-4e4a-9499-b1a4f9854904Untitled design (55)_0.png',''),(7,14,'aswani','ram','malapuram','4999494','aswani@gmail.com','Mca student Passionate about programming','Computer Science','static/99cff963-fcaf-4e4a-9499-b1a4f9854904Untitled design (55)_0.png','student'),(10,20,'roopesh','varma','kollam','7989979','roopesh@gmail.com','Tech intersted guy who ','Automobile','static/99cff963-fcaf-4e4a-9499-b1a4f9854904Untitled design (55)_0.png','developer');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`first_name`,`last_name`,`place`,`phone`,`email`) values (1,1,'abeel','ashraf','kochi','9539877907','abeelashraf7@gmail.com'),(2,10,'ram','manoghar','kochi','6466464','ram@gmail.com'),(3,18,'aswathi','santhsh','wayanad','64664646','aswathi123@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
