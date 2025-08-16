# Internship_CodSoft_Python
Hey Everyone My name is Aditya Verma i am from UttarPradesh Pratapgarh, currently i am pursuing B-Tech from Noida Institute of Engineering and Technology.
## About this project
This Python script is a console-based To-Do List Manager that allows a user to manage tasks interactively. The application supports adding, viewing, completing, and deleting tasks.
1. Menu Display Function
- This function displays the available actions (options 1–5).
- It runs inside a loop so the user can continuously choose actions until exiting.
2. View Tasks
- Displays all tasks with numbering (1, 2, 3...).
- Each task shows its title and status (Completed or Pending).
- If there are no tasks, a message is shown.
3. Add a New Task
- Prompts the user to enter a task title.
- The task is stored in a dictionary
4. Mark Task as Completed
- First checks if there are tasks.
- Shows task list, then asks for a task number.
- Updates completed status to True for that task.
- Handles invalid inputs gracefully.
5. Delete a Task
- Shows available tasks.
- Lets the user pick one by number and removes it from the list.
- Uses .pop() to delete and display the removed task.
6. Main Program Execution
- Starts with an empty task list (tasks = []).
- Runs an infinite loop (while True) to continuously show the menu.
- Executes functions based on user choice:
1 → View tasks
2 → Add task
3 → Mark completed
4 → Delete task
5 → Exit
