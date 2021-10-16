-- 1

CREATE DATABASE Minions ;


-- 2

-- CREATE TABLE Minions (
--   Id INTEGER PRIMARY KEY,
--   Name VARCHAR(255) NOT NULL,
--   Age INTEGER NOT NULL
-- );

CREATE TABLE Towns (
  Id INTEGER PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL
);


-- 3

-- Not supported:
-- ALTER TABLE Minions
-- ADD TownId INTEGER NOT NULL;

-- ALTER TABLE Minions
-- ADD FOREIGN KEY (TownId) REFERENCES Towns(Id);

CREATE TABLE Minions (
  Id INTEGER PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Age INTEGER NOT NULL,
  TownId INTEGER,
  FOREIGN KEY (TownId) REFERENCES Towns(Id)
);

INSERT INTO Towns (Name)
VALUES ('Lemuel');

INSERT INTO Minions (Name, Age, TownId)
VALUES ('Lonnie', 20, 1);


-- 4

CREATE DATABASE Movies ;

CREATE TABLE Directors (
  Id INTEGER PRIMARY KEY AUTO_INCREMENT,
  DirectorName TINYEXT NOT NULL,
  Notes MEDIUMTEXT
);

CREATE TABLE Genres (
  Id INTEGER PRIMARY KEY AUTO_INCREMENT,
  GenreName TINYEXT NOT NULL UNIQUE,
  Notes MEDIUMTEXT
);

CREATE TABLE Categories (
  Id INTEGER PRIMARY KEY AUTO_INCREMENT,
  CategoryName TINYEXT NOT NULL UNIQUE,
  Notes MEDIUMTEXT
);

CREATE TABLE Movies (
  Id INTEGER PRIMARY KEY AUTO_INCREMENT,
  Title TINYTEXT NOT NULL,
  DirectorId INTEGER,
  CopyrightYear YEAR CHECK (CopyrightYear>=1900),
  Length TIME,
  GenreId INTEGER,
  CategoryId INTEGER,
  Rating FLOAT CHECK (0<=Rating<=10),
  Notes LONGTEXT,
  FOREIGN KEY (DirectorId) REFERENCES Directors(Id),
  FOREIGN KEY (GenreId) REFERENCES Genres(Id),
  FOREIGN KEY (CategoryId) REFERENCES Categories(Id)
);

-- Directors

INSERT INTO Directors (DirectorName, Notes)
VALUES ('Leonard Rogahn', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Directors (DirectorName, Notes)
VALUES ('Sharon Ryan', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Directors (DirectorName, Notes)
VALUES ('Rosalie Waelchi', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Directors (DirectorName, Notes)
VALUES ('Rose Pfeffer', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Directors (DirectorName)
VALUES ('Nelson Hilpert II');

-- Genres

INSERT INTO Genres (GenreName, Notes)
VALUES ('Action', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Genres (GenreName, Notes)
VALUES ('Comedy', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Genres (GenreName, Notes)
VALUES ('Drama', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Genres (GenreName, Notes)
VALUES ('Horror', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Genres (GenreName)
VALUES ('Kids', 'Ut delectus qui natus sed. Voluptatem cumque quia labore repellat dignissimos. Debitis magnam omnis voluptas repellat saepe.');

-- Categories

INSERT INTO Categories (CategoryName, Notes)
VALUES ('Category 1', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Categories (CategoryName, Notes)
VALUES ('Category 2', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Categories (CategoryName, Notes)
VALUES ('Category 3', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Categories (CategoryName, Notes)
VALUES ('Category 4', 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Categories (CategoryName)
VALUES ('Category 5');

-- Movies

INSERT INTO Movies (Title, DirectorId, CopyrightYear, Length, Rating, Notes)
VALUES ('Et aut nobis', 1, 2010, '1:30:24', 9.5, 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Movies (Title, Length, GenreId, CategoryId, Rating, Notes)
VALUES ('Sunt et blanditiis', '1:10:44', 2, 4, 4.5, 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Movies (Title, DirectorId, CopyrightYear, GenreId, CategoryId, Rating, Notes)
VALUES ('Nostrum aperiam sed', 3, 1910, 3, 5, 7.5, 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Movies (Title, DirectorId, CopyrightYear, Length, GenreId, CategoryId, Notes)
VALUES ('Aut ipsum voluptatem', 5, 1950, '1:50:21', 4, 1, 'Vitae impedit ut exercitationem sint repudiandae rerum. Enim autem deserunt. Reiciendis reiciendis sed deserunt perferendis sit.');

INSERT INTO Movies (Title, DirectorId, CopyrightYear, Length, GenreId, CategoryId, Rating)
VALUES ('Et illo id', 4, 2010, '1:48:54', 5, 2, 5.5);
