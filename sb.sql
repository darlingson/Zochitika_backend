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