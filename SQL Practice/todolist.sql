SELECT * FROM Task
WHERE TaskID IN (SELECT TaskID FROM User_Task WHERE UserID = 1);

UPDATE Task
SET Completed = 1
WHERE TaskID = 1;

SELECT * FROM Task
ORDER BY DueDate;

SELECT * FROM Task
WHERE TaskID IN (SELECT TaskID FROM Task_ListCategory WHERE CategoryID = 1);

SELECT ListCategory.CategoryName, COUNT(Task_ListCategory.TaskID) AS TaskCount
FROM ListCategory
LEFT JOIN Task_ListCategory ON ListCategory.CategoryID = Task_ListCategory.CategoryID
GROUP BY ListCategory.CategoryName;


