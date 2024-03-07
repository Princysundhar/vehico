/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - vehi_co
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`vehi_co` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `vehi_co`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add login',7,'add_login'),(26,'Can change login',7,'change_login'),(27,'Can delete login',7,'delete_login'),(28,'Can view login',7,'view_login'),(29,'Can add service',8,'add_service'),(30,'Can change service',8,'change_service'),(31,'Can delete service',8,'delete_service'),(32,'Can view service',8,'view_service'),(33,'Can add user',9,'add_user'),(34,'Can change user',9,'change_user'),(35,'Can delete user',9,'delete_user'),(36,'Can view user',9,'view_user'),(37,'Can add serviceprovider',10,'add_serviceprovider'),(38,'Can change serviceprovider',10,'change_serviceprovider'),(39,'Can delete serviceprovider',10,'delete_serviceprovider'),(40,'Can view serviceprovider',10,'view_serviceprovider'),(41,'Can add rating',11,'add_rating'),(42,'Can change rating',11,'change_rating'),(43,'Can delete rating',11,'delete_rating'),(44,'Can view rating',11,'view_rating'),(45,'Can add ownservice',12,'add_ownservice'),(46,'Can change ownservice',12,'change_ownservice'),(47,'Can delete ownservice',12,'delete_ownservice'),(48,'Can view ownservice',12,'view_ownservice'),(49,'Can add feedback',13,'add_feedback'),(50,'Can change feedback',13,'change_feedback'),(51,'Can delete feedback',13,'delete_feedback'),(52,'Can view feedback',13,'view_feedback'),(53,'Can add complaint',14,'add_complaint'),(54,'Can change complaint',14,'change_complaint'),(55,'Can delete complaint',14,'delete_complaint'),(56,'Can view complaint',14,'view_complaint'),(57,'Can add booking',15,'add_booking'),(58,'Can change booking',15,'change_booking'),(59,'Can delete booking',15,'delete_booking'),(60,'Can view booking',15,'view_booking'),(61,'Can add bank',16,'add_bank'),(62,'Can change bank',16,'change_bank'),(63,'Can delete bank',16,'delete_bank'),(64,'Can view bank',16,'view_bank');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(16,'VECHI_CO_APP','bank'),(15,'VECHI_CO_APP','booking'),(14,'VECHI_CO_APP','complaint'),(13,'VECHI_CO_APP','feedback'),(7,'VECHI_CO_APP','login'),(12,'VECHI_CO_APP','ownservice'),(11,'VECHI_CO_APP','rating'),(8,'VECHI_CO_APP','service'),(10,'VECHI_CO_APP','serviceprovider'),(9,'VECHI_CO_APP','user');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'VECHI_CO_APP','0001_initial','2023-10-28 06:39:36.710305'),(2,'contenttypes','0001_initial','2023-10-28 06:39:37.210338'),(3,'auth','0001_initial','2023-10-28 06:39:37.304143'),(4,'admin','0001_initial','2023-10-28 06:39:37.632274'),(5,'admin','0002_logentry_remove_auto_add','2023-10-28 06:39:37.694779'),(6,'admin','0003_logentry_add_action_flag_choices','2023-10-28 06:39:37.710308'),(7,'contenttypes','0002_remove_content_type_name','2023-10-28 06:39:37.788527'),(8,'auth','0002_alter_permission_name_max_length','2023-10-28 06:39:37.804059'),(9,'auth','0003_alter_user_email_max_length','2023-10-28 06:39:37.851030'),(10,'auth','0004_alter_user_username_opts','2023-10-28 06:39:37.851030'),(11,'auth','0005_alter_user_last_login_null','2023-10-28 06:39:37.882278'),(12,'auth','0006_require_contenttypes_0002','2023-10-28 06:39:37.897902'),(13,'auth','0007_alter_validators_add_error_messages','2023-10-28 06:39:37.897902'),(14,'auth','0008_alter_user_username_max_length','2023-10-28 06:39:37.929057'),(15,'auth','0009_alter_user_last_name_max_length','2023-10-28 06:39:37.960376'),(16,'auth','0010_alter_group_name_max_length','2023-10-28 06:39:37.991562'),(17,'auth','0011_update_proxy_permissions','2023-10-28 06:39:38.007279'),(18,'sessions','0001_initial','2023-10-28 06:39:38.038523'),(19,'VECHI_CO_APP','0002_auto_20231028_1544','2023-10-28 10:14:17.004128'),(20,'VECHI_CO_APP','0003_auto_20231125_1220','2023-11-25 06:50:37.065305'),(21,'VECHI_CO_APP','0002_auto_20231227_1253','2023-12-27 07:23:57.617091'),(22,'VECHI_CO_APP','0003_auto_20240120_1550','2024-01-20 10:21:45.989299'),(23,'VECHI_CO_APP','0004_auto_20240120_1556','2024-01-20 10:26:58.144547'),(24,'VECHI_CO_APP','0005_booking_status','2024-02-10 08:41:42.789606');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('3j1etfy82v16kgk8q5y0r5fwuklzpml1','NjY5ZTc5MDBhNmNiYzM5YTEyNTc2YjZjMzY1NWNlOWYxODUzMzViZjp7ImxvZ2lkIjoxLCJsZyI6IiIsImxpZCI6MX0=','2024-01-13 07:47:31.563745'),('vbby42f842cch4yn5w57jhvrkj1xm3yf','Zjc4NmFkMjI4MTA5OTNiNDE4Y2ZiNmQ5NzY4MzQ1OWM4OGMzYzM1ZTp7ImxpZCI6MSwibGciOiJsaW4iLCJsb2dpZCI6MX0=','2024-01-13 07:45:47.675238');

/*Table structure for table `vechi_co_app_bank` */

DROP TABLE IF EXISTS `vechi_co_app_bank`;

CREATE TABLE `vechi_co_app_bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ifsc` varchar(200) NOT NULL,
  `accountnumber` varchar(200) NOT NULL,
  `balance` varchar(200) NOT NULL,
  `HOLDER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `VECHI_CO_APP_bank_HOLDER_id_51eff237_fk_VECHI_CO_APP_login_id` (`HOLDER_id`),
  CONSTRAINT `VECHI_CO_APP_bank_HOLDER_id_51eff237_fk_VECHI_CO_APP_login_id` FOREIGN KEY (`HOLDER_id`) REFERENCES `vechi_co_app_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `vechi_co_app_bank` */

/*Table structure for table `vechi_co_app_booking` */

DROP TABLE IF EXISTS `vechi_co_app_booking`;

CREATE TABLE `vechi_co_app_booking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lattitude` varchar(200) NOT NULL,
  `longitude` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `paymentstatus` varchar(200) NOT NULL,
  `SERVICE_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  `completionstatus` varchar(200) NOT NULL,
  `note` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `VECHI_CO_APP_booking_SERVICE_id_4cd53bce_fk_VECHI_CO_` (`SERVICE_id`),
  KEY `VECHI_CO_APP_booking_USER_id_bcd8abc9_fk_VECHI_CO_APP_user_id` (`USER_id`),
  CONSTRAINT `VECHI_CO_APP_booking_SERVICE_id_4cd53bce_fk_VECHI_CO_` FOREIGN KEY (`SERVICE_id`) REFERENCES `vechi_co_app_service` (`id`),
  CONSTRAINT `VECHI_CO_APP_booking_USER_id_bcd8abc9_fk_VECHI_CO_APP_user_id` FOREIGN KEY (`USER_id`) REFERENCES `vechi_co_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `vechi_co_app_booking` */

insert  into `vechi_co_app_booking`(`id`,`lattitude`,`longitude`,`date`,`paymentstatus`,`SERVICE_id`,`USER_id`,`completionstatus`,`note`,`status`) values (1,'26256','36565','2023/12/26','pending',1,1,'11','approved','1');

/*Table structure for table `vechi_co_app_complaint` */

DROP TABLE IF EXISTS `vechi_co_app_complaint`;

CREATE TABLE `vechi_co_app_complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `SERVICEPROVIDER_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  `reply` varchar(200) NOT NULL,
  `replydate` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `VECHI_CO_APP_complai_SERVICEPROVIDER_id_195b6751_fk_VECHI_CO_` (`SERVICEPROVIDER_id`),
  KEY `VECHI_CO_APP_complaint_USER_id_81c3ff75_fk_VECHI_CO_APP_user_id` (`USER_id`),
  CONSTRAINT `VECHI_CO_APP_complaint_USER_id_81c3ff75_fk_VECHI_CO_APP_user_id` FOREIGN KEY (`USER_id`) REFERENCES `vechi_co_app_user` (`id`),
  CONSTRAINT `VECHI_CO_APP_complai_SERVICEPROVIDER_id_195b6751_fk_VECHI_CO_` FOREIGN KEY (`SERVICEPROVIDER_id`) REFERENCES `vechi_co_app_serviceprovider` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `vechi_co_app_complaint` */

insert  into `vechi_co_app_complaint`(`id`,`complaint`,`date`,`SERVICEPROVIDER_id`,`USER_id`,`reply`,`replydate`) values (5,'dd','dcddd',3,1,'bdfnhgfn','20231209-115551');

/*Table structure for table `vechi_co_app_feedback` */

DROP TABLE IF EXISTS `vechi_co_app_feedback`;

CREATE TABLE `vechi_co_app_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedbacks` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `VECHI_CO_APP_feedback_USER_id_8dcd9741_fk_VECHI_CO_APP_user_id` (`USER_id`),
  CONSTRAINT `VECHI_CO_APP_feedback_USER_id_8dcd9741_fk_VECHI_CO_APP_user_id` FOREIGN KEY (`USER_id`) REFERENCES `vechi_co_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `vechi_co_app_feedback` */

insert  into `vechi_co_app_feedback`(`id`,`feedbacks`,`date`,`USER_id`) values (2,'oookokok','20/01/2024-16:04:34',1),(3,'xtz','27/01/2024-12:38:03',1),(4,'very good','27/01/2024-12:38:45',1),(5,'tggfgj','27/01/2024-14:39:53',1),(6,'ggg','10/02/2024-12:41:23',1);

/*Table structure for table `vechi_co_app_login` */

DROP TABLE IF EXISTS `vechi_co_app_login`;

CREATE TABLE `vechi_co_app_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usertype` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `vechi_co_app_login` */

insert  into `vechi_co_app_login`(`id`,`username`,`password`,`usertype`) values (1,'a','1','admin'),(3,'nandana','1234','service_provider'),(4,'ajoy','Vechi@123','service_provider'),(5,'1123erty@gmail.com','1234567789','service_provider'),(6,'','',''),(7,'bb','cc','user'),(8,'anu@gmail.com','123','service_provider'),(9,'anu@gmail.com','123','service_provider'),(10,'ajy@gmail.com','122','service_provider'),(11,'ee@gmsi','123','pending'),(12,'ajoy12@gmau.com','ajoy123','user'),(13,'ajoy12@gmau.com','ajoy123','user'),(14,'ajoy12@gmau.com','ajoy123','user'),(15,'ajoy12@gmau.com','ajoy123','user'),(16,'Ajoy123@gmail.com','123456789','user'),(17,'vzhsh','qq','user'),(18,'aaaa','123456789','user');

/*Table structure for table `vechi_co_app_ownservice` */

DROP TABLE IF EXISTS `vechi_co_app_ownservice`;

CREATE TABLE `vechi_co_app_ownservice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `SERVICE_id` int(11) NOT NULL,
  `SERVICEPROVIDER_id` int(11) NOT NULL,
  `amount` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `VECHI_CO_APP_ownserv_SERVICE_id_5d3e10c7_fk_VECHI_CO_` (`SERVICE_id`),
  KEY `VECHI_CO_APP_ownserv_SERVICEPROVIDER_id_31388361_fk_VECHI_CO_` (`SERVICEPROVIDER_id`),
  CONSTRAINT `VECHI_CO_APP_ownserv_SERVICEPROVIDER_id_31388361_fk_VECHI_CO_` FOREIGN KEY (`SERVICEPROVIDER_id`) REFERENCES `vechi_co_app_serviceprovider` (`id`),
  CONSTRAINT `VECHI_CO_APP_ownserv_SERVICE_id_5d3e10c7_fk_VECHI_CO_` FOREIGN KEY (`SERVICE_id`) REFERENCES `vechi_co_app_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `vechi_co_app_ownservice` */

insert  into `vechi_co_app_ownservice`(`id`,`SERVICE_id`,`SERVICEPROVIDER_id`,`amount`) values (8,18,4,'1');

/*Table structure for table `vechi_co_app_rating` */

DROP TABLE IF EXISTS `vechi_co_app_rating`;

CREATE TABLE `vechi_co_app_rating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rating` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `SERVICE_id` int(11) NOT NULL,
  `USER_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `VECHI_CO_APP_rating_SERVICE_id_1fc502af_fk_VECHI_CO_` (`SERVICE_id`),
  KEY `VECHI_CO_APP_rating_USER_id_2d5949f5_fk_VECHI_CO_APP_user_id` (`USER_id`),
  CONSTRAINT `VECHI_CO_APP_rating_SERVICE_id_1fc502af_fk_VECHI_CO_` FOREIGN KEY (`SERVICE_id`) REFERENCES `vechi_co_app_service` (`id`),
  CONSTRAINT `VECHI_CO_APP_rating_USER_id_2d5949f5_fk_VECHI_CO_APP_user_id` FOREIGN KEY (`USER_id`) REFERENCES `vechi_co_app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `vechi_co_app_rating` */

insert  into `vechi_co_app_rating`(`id`,`rating`,`date`,`SERVICE_id`,`USER_id`) values (1,'5','28',1,1);

/*Table structure for table `vechi_co_app_service` */

DROP TABLE IF EXISTS `vechi_co_app_service`;

CREATE TABLE `vechi_co_app_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `vechi_co_app_service` */

insert  into `vechi_co_app_service`(`id`,`service_name`) values (1,'fuel delevery'),(5,'vechicle service'),(18,'TOWING'),(20,'test');

/*Table structure for table `vechi_co_app_serviceprovider` */

DROP TABLE IF EXISTS `vechi_co_app_serviceprovider`;

CREATE TABLE `vechi_co_app_serviceprovider` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(200) NOT NULL,
  `contactnumber` bigint(20) NOT NULL,
  `lattitude` varchar(200) NOT NULL,
  `place` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  `longitude` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `VECHI_CO_APP_service_LOGIN_id_e7db528f_fk_VECHI_CO_` (`LOGIN_id`),
  CONSTRAINT `VECHI_CO_APP_service_LOGIN_id_e7db528f_fk_VECHI_CO_` FOREIGN KEY (`LOGIN_id`) REFERENCES `vechi_co_app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `vechi_co_app_serviceprovider` */

insert  into `vechi_co_app_serviceprovider`(`id`,`service_name`,`contactnumber`,`lattitude`,`place`,`email`,`LOGIN_id`,`longitude`) values (3,'ss',0,'ss','ss','ss',3,'1'),(4,'t',223,'11.868514423076922','w','w',4,'75.36321148076924'),(5,'nn',345,'ghf','cv','anu@gmail.com',9,'1'),(6,'r',234,'2345','aasd','ajy@gmail.com',10,'1'),(7,'name',89899,'11.868505755957644','place','ee@gmsi',11,'75.36320749499336');

/*Table structure for table `vechi_co_app_user` */

DROP TABLE IF EXISTS `vechi_co_app_user`;

CREATE TABLE `vechi_co_app_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `contact` bigint(20) NOT NULL,
  `Email` varchar(200) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `VECHI_CO_APP_user_LOGIN_id_c26a703f_fk_VECHI_CO_APP_login_id` (`LOGIN_id`),
  CONSTRAINT `VECHI_CO_APP_user_LOGIN_id_c26a703f_fk_VECHI_CO_APP_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `vechi_co_app_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `vechi_co_app_user` */

insert  into `vechi_co_app_user`(`id`,`username`,`contact`,`Email`,`LOGIN_id`) values (1,'nirmal',12345678,'chhh',7),(2,'ajoy',8888888888,'ajoy12@gmau.com',12),(3,'ajoy',8888888888,'ajoy12@gmau.com',13),(4,'ajoy',8888888888,'ajoy12@gmau.com',14),(5,'ajoy',8888888888,'ajoy12@gmau.com',15),(6,'Ajoy',8888888888,'Ajoy123@gmail.com',16),(7,'hshhz',667689,'vzhsh',17),(8,'Nandana Valsaraj',99999999,'aaaa',18);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
