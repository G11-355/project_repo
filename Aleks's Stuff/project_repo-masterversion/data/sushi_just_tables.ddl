CREATE TABLE `user_tb` (
	`username` VARCHAR(100),
	`first_name` VARCHAR(100),
	`last_name` VARCHAR(100),
	`password` VARCHAR(100) NOT NULL,
	`phone_number` VARCHAR(10) NOT NULL,
	`address` VARCHAR(250) NOT NULL,
	`dob` DATE DEFAULT NULL,
	`date_hired` DATE DEFAULT NULL,
	`manager_id` VARCHAR(100) DEFAULT NULL,
	`salary` INT DEFAULT NULL,
	`specialty` INT DEFAULT NULL,
	`license_number` VARCHAR(100) DEFAULT NULL,
	`license_expiration` DATE DEFAULT NULL,
	`pos_logon` VARCHAR(100) DEFAULT NULL,
	PRIMARY KEY (`username`),
	FOREIGN KEY (manager_id) REFERENCES user_tb(username)
);

CREATE TABLE `order_tb` (
	`order_id` INT NOT NULL AUTO_INCREMENT,
	`customer_username` VARCHAR(100) NOT NULL,
	`staff_username` VARCHAR(100) NOT NULL,
	`order_date` DATE NOT NULL,
	PRIMARY KEY (`order_id`),
    FOREIGN KEY (customer_username) REFERENCES user_tb(username),
    FOREIGN KEY (staff_username) REFERENCES user_tb(username)
);

CREATE TABLE `item_tb` (
	`item_id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
	`cost` FLOAT NOT NULL,
	`type` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`item_id`)
);

CREATE TABLE `order_contents_tb` (
	`order_id` INT NOT NULL,
	`item_id` INT NOT NULL,
	`quantity` INT NOT NULL,
	PRIMARY KEY (item_id),
	FOREIGN KEY (order_id) REFERENCES order_tb(order_id),
    FOREIGN KEY (item_id) REFERENCES item_tb(item_id)
);

