CREATE TABLE `zochitika_db`.`zochitika`
 (`title` VARCHAR(255) NOT NULL ,
  `organiser` VARCHAR(255) NULL DEFAULT NULL ,
  `date` DATE NULL DEFAULT NULL ,
  `description` TEXT NULL DEFAULT NULL ,
  `location` VARCHAR(255) NULL DEFAULT NULL ,
  `type` VARCHAR(255) NOT NULL ,
  `entry_fee` VARCHAR(255) NULL DEFAULT NULL ,
  `address` VARCHAR(255) NULL DEFAULT NULL ,
  `coordinates` VARCHAR(255) NOT NULL ,
  `id` BIGINT NOT NULL AUTO_INCREMENT , PRIMARY KEY (`id`)) ENGINE = InnoDB;

INSERT INTO `zochitika`
 (`title`, `organiser`, `date`, `description`, `location`, `type`, `entry_fee`, `address`, `coordinates`, `id`)
 VALUES
 ('Nasty C', 'illusionz_mw', '2023-12-29', 'Starring Nasty C', 'illuzions Golden Peacock Complex', 'shows', NULL, NULL, '', NULL);
ALTER TABLE `zochitika`
 ADD `end_date` DATE NULL DEFAULT NULL AFTER `date`,
 ADD `time` TIME NULL DEFAULT NULL AFTER `end_date`,
 ADD `end_time` TIME NULL DEFAULT NULL AFTER `time`;

INSERT INTO `zochitika` (`title`, `organiser`, `date`, `end_date`, `time`, `end_time`, `description`, `location`, `type`, `entry_fee`, `address`, `coordinates`, `id`) VALUES ('Soirée de Luxe', 'The Sunday Soiree', '2023-12-16', '2023-12-17', '12:00:00', '12:30:00', 'As the year draws to a close, join us for an extraordinary end-of-year soirée event. Soirée de Luxe doubles as the perfect homecoming celebration.', 'Lassie House Zomba Street, Area 10, House No. 10/85, Lilongwe', 'Event', '20,000', 'Zomba Street, Area 10, House No. 10/85 Lilongwe', '-13.938678652825335, 33.804071176631645', NULL)
INSERT INTO `zochitika` (`title`, `organiser`, `date`, `end_date`, `time`, `end_time`, `description`, `location`, `type`, `entry_fee`, `address`, `coordinates`, `id`)
 VALUES
 ('Karonga Moko Fest', 'Akometsi Entertainment', '2023-12-22', '2023-12-22', '14:00:00', NULL, NULL, 'Club Destination 24/7 Karonga', 'show', '5000', 'Club Destination 24/7 Karonga', '', NULL),
 ('Mind issues Album listening party', 'Plvgeyez', '2023-12-23', '2023-12-23', '12:00:00', NULL, NULL, 'Angelo Goveya, Blantyre', 'listening party', '3,000', NULL, '', NULL),
 ('We Outside Christmas Eve', 'New Village House', '2023-12-24', '2023-12-24', '18:00:00', NULL, NULL, 'New Village House', 'show', '4,000', NULL, 'New Village House,Manase,Blantyre', NULL)
INSERT INTO `zochitika` (`title`, `organiser`, `date`, `end_date`, `time`, `end_time`, `description`, `location`, `type`, `entry_fee`, `address`, `coordinates`, `id`) VALUES ('The Hive Experience', 'Royal Images and Umodzi Park', '2023-12-29', '2023-12-30', '20:30:00', '04:00:00', NULL, 'BICC Auditorium,Lilongwe', 'Show', '20,000', 'BICC Auditorium', '', NULL)