📌 Project Overview
-----------------------
This project simulates one day of operations for a fictional logistics company called FastBox.
The system assigns delivery packages to the nearest delivery agents based on Euclidean distance, simulates deliveries, calculates total travel distance, and identifies the most efficient agent.

The program supports multiple test cases stored in a folder and generates a separate report for each one.

⚙ How the System Works
------------------------
1.Reads all JSON files from the testcases folder
2.For each package:
    ->Finds the nearest agent based on Euclidean distance
    ->Simulates travel: Agent → Warehouse → Destination
3.Calculates:
  ->Total distance per agent
  ->Number of packages delivered
  ->Efficiency = total_distance / packages_delivered
4.Selects the best (most efficient) agent
5.Saves a report for each testcase in the output folder

▶ How to Run
-------------
Place your test JSON files in the testcases folder
Open terminal in project directory
Run:
python main.py
Reports will be generated in the output folder

🎯 Evaluation Criteria Covered
-------------------------------
->JSON Parsing
->Euclidean Distance Calculation
->Correct Agent Assignment
->Simulation of Deliveries
->Report Generation
->Code Clarity and Modularity

🧑‍💻 Author
---------
R. Debashish Das
Python & AI/ML Enthusiast​
