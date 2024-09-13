-- Create User table
CREATE TABLE User (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL
);

-- Create Task table
CREATE TABLE Task (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Description TEXT,
    DueDate DATE,
    Completed BOOLEAN DEFAULT 0
);

-- Create ListCategory table
CREATE TABLE ListCategory (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(50) NOT NULL
);

-- Create User_Task table for many-to-many relationship between User and Task
CREATE TABLE User_Task (
    UserID INT,
    TaskID INT,
    PRIMARY KEY (UserID, TaskID),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (TaskID) REFERENCES Task(TaskID)
);

-- Create Task_ListCategory table for many-to-many relationship between Task and ListCategory
CREATE TABLE Task_ListCategory (
    TaskID INT,
    CategoryID INT,
    PRIMARY KEY (TaskID, CategoryID),
    FOREIGN KEY (TaskID) REFERENCES Task(TaskID),
    FOREIGN KEY (CategoryID) REFERENCES ListCategory(CategoryID)
);


