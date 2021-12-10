USE geodata;


DROP TABLE IF EXISTS `coordinates`;
CREATE TABLE `coordinates` (
    `id` int NOT NULL AUTO_INCREMENT,
    `lat` FLOAT(32, 29) NOT NULL,
    `lon` FLOAT(32, 29) NOT NULL,
    `version` int NOT NULL
);


