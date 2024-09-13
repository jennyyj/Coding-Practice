-- Insert sample data into User table
INSERT INTO User (Username, Password, Email) VALUES
('Jenny', 'password1', 'jenny@example.com'),
('Jacob', 'password2', 'jacob@example.com');

-- Insert sample data into Task table
INSERT INTO Task (Title, Description, DueDate, Completed) VALUES
('Task 1', 'Task 1: Take out the trash', '2024-04-10', 0),
('Task 2', 'Task 2: Walk the dog', '2024-04-15', 0),
('Task 3', 'Task 3: Complete Assignment', '2024-04-20', 1);

-- Insert sample data into ListCategory table
INSERT INTO ListCategory (CategoryName) VALUES
('Work'),
('Personal');

-- Insert sample data into User_Task table
INSERT INTO User_Task (UserID, TaskID) VALUES
(1, 1),
(1, 2),
(2, 2),
(2, 3);

-- Insert sample data into Task_ListCategory table
INSERT INTO Task_ListCategory (TaskID, CategoryID) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 2);
