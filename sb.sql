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