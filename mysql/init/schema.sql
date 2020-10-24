SET NAMES utf8mb4;
CREATE DATABASE IF NOT EXISTS `test-db`;

USE `test-db`;

CREATE TABLE `documents` (
  `doc_id` int PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text,
  `publisher_id` int,
  `release_year` year,
  `isbn` char(10),
  `language` ENUM ('english', 'vietnamese', 'other') NOT NULL,
  `path_to_file` varchar(255) NOT NULL,
  `category` ENUM ('book', 'arctile', 'slide', 'test') NOT NULL
);

CREATE TABLE `document_author` (
  `document_id` int NOT NULL,
  `author_id` int NOT NULL,
  `last_update` timestamp
);

CREATE TABLE `authors` (
  `author_id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text
);

CREATE TABLE `publishers` (
  `p_id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL
);

CREATE TABLE `users` (
  `user_id` int PRIMARY KEY AUTO_INCREMENT,
  `uname` varchar(255) UNIQUE NOT NULL,
  `email` varchar(255) UNIQUE NOT NULL,
  `md5_pass` varchar(255) NOT NULL
);

CREATE TABLE `bookmarks` (
  `bookmark_id` int PRIMARY KEY AUTO_INCREMENT,
  `document_id` int NOT NULL,
  `user_id` int NOT NULL
);

CREATE TABLE `uploaded` (
  `uploaded_id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `document_id` int NOT NULL,
  `upload_time` timestamp
);

CREATE TABLE `rates` (
  `rate_id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `document_id` int NOT NULL,
  `rate_value` tinyint NOT NULL
);

CREATE TABLE `subjects` (
  `subject_id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255)
);

CREATE TABLE `majors` (
  `major_id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255)
);

CREATE TABLE `major_subject` (
  `major_id` int NOT NULL,
  `subject_id` int NOT NULL
);

CREATE TABLE `subject_document` (
  `subject_id` int NOT NULL,
  `document_id` int NOT NULL
);

CREATE TABLE `subject_resource` (
  `subject_id` int NOT NULL,
  `resource` varchar(255) NOT NULL
);

ALTER TABLE `documents` ADD FOREIGN KEY (`publisher_id`) REFERENCES `publishers` (`p_id`);

ALTER TABLE `document_author` ADD FOREIGN KEY (`document_id`) REFERENCES `documents` (`doc_id`);

ALTER TABLE `document_author` ADD FOREIGN KEY (`author_id`) REFERENCES `authors` (`author_id`);

ALTER TABLE `bookmarks` ADD FOREIGN KEY (`document_id`) REFERENCES `documents` (`doc_id`);

ALTER TABLE `bookmarks` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

ALTER TABLE `uploaded` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

ALTER TABLE `uploaded` ADD FOREIGN KEY (`document_id`) REFERENCES `documents` (`doc_id`);

ALTER TABLE `rates` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

ALTER TABLE `rates` ADD FOREIGN KEY (`document_id`) REFERENCES `documents` (`doc_id`);

ALTER TABLE `major_subject` ADD FOREIGN KEY (`major_id`) REFERENCES `majors` (`major_id`);

ALTER TABLE `major_subject` ADD FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`subject_id`);

ALTER TABLE `subject_document` ADD FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`subject_id`);

ALTER TABLE `subject_document` ADD FOREIGN KEY (`document_id`) REFERENCES `documents` (`doc_id`);

ALTER TABLE `subject_resource` ADD FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`subject_id`);

ALTER TABLE `document_author` ADD UNIQUE `unique_pair` (`document_id`, `author_id`);

ALTER TABLE `bookmarks` ADD UNIQUE `unique_pair` (`document_id`, `user_id`);

ALTER TABLE `uploaded` ADD UNIQUE `unique_pair` (`user_id`, `document_id`);

ALTER TABLE `rates` ADD UNIQUE `unique_pair` (`user_id`, `document_id`);

ALTER TABLE `major_subject` ADD UNIQUE `unique_pair` (`major_id`, `subject_id`);

ALTER TABLE `subject_document` ADD UNIQUE `unique_pair` (`subject_id`, `document_id`);

ALTER TABLE `subject_resource` ADD UNIQUE `unique_pair` (`subject_id`, `resource`);
