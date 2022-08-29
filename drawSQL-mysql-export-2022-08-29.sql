CREATE TABLE `super`(
    `name` CHAR(255) NOT NULL,
    `alter_ego` CHAR(255) NOT NULL,
    `primary_ability` CHAR(255) NOT NULL,
    `second_ability` CHAR(255) NOT NULL,
    `catch_phrase` CHAR(255) NOT NULL,
    `FK super_type` INT NOT NULL
);
ALTER TABLE
    `super` ADD PRIMARY KEY `super_name_primary`(`name`);
ALTER TABLE
    `super` ADD UNIQUE `super_fk super_type_unique`(`FK super_type`);
CREATE TABLE `Supertype`(`type` CHAR(255) NOT NULL);
ALTER TABLE
    `Supertype` ADD PRIMARY KEY `supertype_type_primary`(`type`);