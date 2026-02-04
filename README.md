📌 Project Overview
-----------------------
This project simulates one day of operations for a fictional logistics company called FastBox.
The system assigns delivery packages to the nearest delivery agents based on Euclidean distance, simulates deliveries, calculates total travel distance, and identifies the most efficient agent.

The program supports multiple test cases stored in a folder and generates a separate report for each one.

🗂 Folder Structure
---------------------
Mystery_Delivery_System/
│
├── testcases/
│   ├── case1.json
│   ├── case2.json
│   └── case3.json
│
├── output/
│   ├── report_case1.json
│   ├── report_case2.json
│   └── report_case3.json
│
└── main.py

📥 Input Format (JSON)
-----------------------
{
  "warehouses": {
    "W1": [0, 0],
    "W2": [50, 75]
  },
  "agents": {
    "A1": [5, 5],
    "A2": [60, 60]
  },
  "packages": [
    {"id": "P1", "warehouse": "W1", "destination": [30, 40]},
    {"id": "P2", "warehouse": "W2", "destination": [70, 90]}
  ]
}

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

Output Format (Report)
----------------------
Example output (report_case1.json):
{
  "A1": {
    "packages_delivered": 2,
    "total_distance": 85.32,
    "efficiency": 42.66
  },
  "A2": {
    "packages_delivered": 2,
    "total_distance": 120.12,
    "efficiency": 60.06
  },
  "A3": {
    "packages_delivered": 1,
    "total_distance": 50.0,
    "efficiency": 50.0
  },
  "best_agent": "A1"
}

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
