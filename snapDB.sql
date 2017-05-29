# ************************************************************
# 
# SnapchatClone Database
# Autor: Fernando Ortiz Rico Celio
#
# ************************************************************

CREATE DATABASE `snapchat`;

USE `snapchat`;

DROP TABLE IF EXISTS `SNAP`;

CREATE TABLE `SNAP` (
  `snapID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `snapName` varchar(150) NOT NULL DEFAULT '',
  `snapSender` int(5) unsigned zerofill DEFAULT NULL,
  `snapReceiver` int(5) unsigned zerofill DEFAULT NULL,
  `snapStatus` tinyint(1) unsigned NOT NULL,
  `snapFile` longtext,
  PRIMARY KEY (`snapID`),
  KEY `FK_snapChannel` (`snapSender`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `USER`;

CREATE TABLE `USER` (
  `userID` int(5) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `userNickname` varchar(50) NOT NULL DEFAULT '',
  `userName` varchar(50) NOT NULL DEFAULT '',
  `userPassword` varchar(100) NOT NULL DEFAULT '',
  `userIPAddress` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;