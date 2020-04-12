CREATE TABLE `user_tb` (
	`user_id` INT NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(100) NOT NULL,
	`first_name` VARCHAR(100),
	`last_name` VARCHAR(100),
	`password` VARCHAR(100) NOT NULL,
	`phone_number` VARCHAR(20) NOT NULL,
	`address` VARCHAR(250) NOT NULL,
	`dob` DATE DEFAULT NULL,
	`date_hired` DATE DEFAULT NULL,
	`manager_id` INT DEFAULT NULL,
	`salary` INT DEFAULT NULL,
	`specialty` VARCHAR(20) DEFAULT NULL,
	`license_number` VARCHAR(100) DEFAULT NULL,
	`license_expiration` DATE DEFAULT NULL,
	`pos_logon` VARCHAR(100) DEFAULT NULL,
	PRIMARY KEY (user_id),
	FOREIGN KEY (manager_id) REFERENCES user_tb(user_id)
);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Stacy_Nelson_19','Stacy','Nelson','MLTTHfp',1692128724,'144 Main Lane','1986-8-21','2015-9-20','1',15,NULL,NULL,NULL,'XCzWVTu');
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Jim_Davis_0','Jim','Davis','aezhHYz',3240018750,'593 Tree Road',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('David_Baker_1','David','Baker','KsHNsuP',5541247833,'352 Leaf Way',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Erica_Goldberg_2','Erica','Goldberg','zwQlUOp',9344748949,'506 Oak Way',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Lucy_Flores_3','Lucy','Flores','EsHAUVb',8625945561,'922 Yam Street',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Bob_Bell_4','Bob','Bell','jmkdJTW',8779416157,'779 Corn Street',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Kim_Hill_5','Kim','Hill','UjebVDK',1509088181,'156 Yam Street',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Karen_Smith_6','Karen','Smith','NvbDWlU',0608854710,'779 Tree Road',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('David_Baker_7','David','Baker','ycJzWKa',1426026293,'431 Yellow Street',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Lucy_Cook_8','Lucy','Cook','YgLTLsN',3169505608,'953 Yam Road',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('David_Davis_9','David','Davis','JkeZJPD',6100584888,'827 Main Lane',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Bob_Taylor_10','Bob','Taylor','bxJbtHF',3053371170,'726 Garden Way','1987-5-22','1980-10-15',1,12,'Sushi',NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('David_Flores_11','David','Flores','FLWRqRF',1456318318,'053 Main Way','1997-1-22','1996-8-8',1,20,'Sushi',NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Mary_Bell_12','Mary','Bell','OHcqWwL',5110527097,'417 Main Way','1981-5-1','2004-5-16',1,13,'Soups',NULL,NULL,NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Chad_Moore_13','Chad','Moore','eOsjMgV',9793081959,'062 Tree Road','2002-4-6','1988-6-23',1,10,NULL,42779,'1996-6-14',NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('John_Nelson_14','John','Nelson','pLcryuZ',0245494765,'281 Blue Road','2001-2-11','1992-8-12',1,11,NULL,31334,'1991-7-31',NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Walter_Bell_15','Walter','Bell','PgalOjI',2103196879,'847 Yellow Way','1996-9-23','2010-5-25',1,12,NULL,09113,'2012-4-9',NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Walter_Moore_16','Walter','Moore','gObntAk',1563352935,'425 Leaf Way','2007-11-11','1983-9-21',1,14,NULL,83913,'1983-7-3',NULL);
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('Bob_Bell_17','Bob','Bell','FzAkmEe',5367729088,'848 Oak Street','2012-8-27','1983-3-1',1,10,NULL,NULL,NULL,'MCEMTnE');
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('James_Goldberg_18','James','Goldberg','VGGMYHQ',8120747975,'349 Corn Road','1983-6-2','1989-7-3',1,12,NULL,NULL,NULL,'JmmXtjf');
INSERT INTO user_tb(username,first_name,last_name,password,phone_number,address,dob,date_hired,manager_id,salary,specialty,license_number,license_expiration,pos_logon) VALUES ('John_Moore_20','John','Moore','HSeMVTJ',3868518438,'678 Tree Way','2018-1-28','1995-10-22',1,18,NULL,NULL,NULL,'NoAQYyf');


CREATE TABLE `order_tb` (
	`order_id` INT NOT NULL,
	`customer_id` INT NOT NULL,
	`staff_id` INT NOT NULL,
	`order_date` DATE NOT NULL,
	PRIMARY KEY (`order_id`),
    FOREIGN KEY (customer_id) REFERENCES user_tb(user_id),
    FOREIGN KEY (staff_id) REFERENCES user_tb(user_id)
);

CREATE TABLE `item_tb` (
	`item_id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
	`cost` FLOAT NOT NULL,
	`type` VARCHAR(100) NOT NULL,
	`description` VARCHAR(2000),
	PRIMARY KEY (`item_id`)
);

INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (0,'Edamame',5.00,'app', 'Steamed Japanese Soy Bean, Sprinkled Lightly with Salt.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (1,'Takoyaki',7.50,'app', '(6 Pieces) Crispy Octopus Puffs Topped with Fish Bonito, Seaweed, MayoSweet Brown Sauce and Sesame Seeds.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (2,'Gyoza',6.50,'app', '(5 pieces) Pan Fried Japanese Chicken Dumpling.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (3,'Age-Dashi Tofu',6.50,'app', 'A creamy soft tofu, sliced thin and quick fried for crispiness, served in a hot broth with ginger and garnished with green onion.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (4,'Crab Rangoon',6.50,'app', '(6 Pieces) Soft Cream Cheese, Crab Stick, Celery, Water Chestnut and Carrots; Wrapped in Crispy Spring Roll Skin. Served with Sweet & Sour Sauce.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (5,'Mixed Greens Salad',6.00,'sal', 'Mixed Greens, Carrots, Cucumbers and Tomatoes. Served With Japanese Style Ginger Dressing Or Creamy Homemade Dressing.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (6,'Tuna Avocado Salad',9.00,'sal', 'Mixed greens Topped with Sliced fresh Tuna ');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (7,'Miso Soup',2.50,'sop', 'Soy bean Broth with Soft tofu, Scallions, and Seaweed.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (8,'Tom Kha Soup',5.95,'sop', '(Chicken Or Tofu) Coconut Broth with Mushroom, Tomato, Onion, Galangal, Lemongrass and Cilantro.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (9,'Tonkotsu Ramen',12.95,'sop', 'Japanese Egg Noodles, Pork Broth, Pork Chashu, Marinated Bamboo Shoots, Quail Eggs, Spinach, Japanese Prepared Vegetables, Bean Sprouts and Sesame Seeds. Topped with Green Onion, Fish Cake and Seaweed Sheet.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (10,'Shrimp Tempura',13.95,'ent', 'Deep Fried Shrimp and Vegetables Tempura with Tempura Sauce.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (11,'Chicken Katsu',13.95,'ent', 'Breaded Deep-Fried Chicken Served with Our Chef`s Signature Sauce.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (12,'Panang Curry',14.95,'ent', 'Choice of Salmon or Rib Eye Steak with Kefir Lime Leaf, Bell Pepper, Green Beans, Peas, Carrots and Asparagus in Coconut Milk and Panang Curry.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (13,'Salmon Roll',8.00,'ent', 'Fresh salmon.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (14,'Philly Maki',8.50,'ent', 'Smoked salmon, avocado, and cream cheese.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (15,'Spicy Tuna Maki',9.50,'ent', 'Chopped tuna, masago mayo and chili sauce.');
INSERT INTO item_tb(item_id,name,cost,type,description) VALUES (16,'Dragon Maki',15.00,'ent', 'Shrimp tempura, masago mayo, topped with fresh water eel, avocado, and unagi sauce.');
INSERT INTO item_tb(item_id,name,cost,type) VALUES (17,'Soft Drink',1.75,'drk');
INSERT INTO item_tb(item_id,name,cost,type) VALUES (18,'Thai Iced Tea',2.50,'drk');
INSERT INTO item_tb(item_id,name,cost,type) VALUES (19,'Green Tea',1.75,'drk');


CREATE TABLE `order_contents_tb` (
	`order_id` INT NOT NULL,
	`item_id` INT NOT NULL,
	`quantity` INT NOT NULL,
	PRIMARY KEY (item_id, order_id),
	FOREIGN KEY (order_id) REFERENCES order_tb(order_id),
    FOREIGN KEY (item_id) REFERENCES item_tb(item_id)
);