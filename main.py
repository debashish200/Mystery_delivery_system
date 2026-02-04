import json
import math
import os


# Distance function
def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# Folder paths
TESTCASE_FOLDER = "testcases"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# Loop through all testcases
for filename in os.listdir(TESTCASE_FOLDER):
    if filename.endswith(".json"):
        filepath = os.path.join(TESTCASE_FOLDER, filename)

        with open(filepath, "r") as f:
            data = json.load(f)

        warehouses = data["warehouses"]
        agents = data["agents"]
        packages = data["packages"]

    
        # Initialize report structure
        report = {}
        for agent in agents:
            report[agent] = {
                "packages_delivered": 0,
                "total_distance": 0.0,
                "efficiency": 0.0
            }

        
        # Assign packages
        for pkg in packages:
            wh_location = warehouses[pkg["warehouse"]]

            min_dist = float("inf")
            chosen_agent = None

            for agent, agent_loc in agents.items():
                dist = euclidean(agent_loc, wh_location)
                if dist < min_dist:
                    min_dist = dist
                    chosen_agent = agent

            # Simulate delivery
            agent_loc = agents[chosen_agent]
            dest = pkg["destination"]

            dist_to_wh = euclidean(agent_loc, wh_location)
            dist_wh_to_dest = euclidean(wh_location, dest)

            total_trip = dist_to_wh + dist_wh_to_dest

            report[chosen_agent]["packages_delivered"] += 1
            report[chosen_agent]["total_distance"] += total_trip

        
        # Efficiency + Best Agent
        best_agent = None
        best_eff = float("inf")

        for agent in report:
            count = report[agent]["packages_delivered"]
            if count > 0:
                report[agent]["efficiency"] = round(
                    report[agent]["total_distance"] / count, 2
                )
            else:
                report[agent]["efficiency"] = 0

            report[agent]["total_distance"] = round(report[agent]["total_distance"], 2)

            if report[agent]["efficiency"] > 0 and report[agent]["efficiency"] < best_eff:
                best_eff = report[agent]["efficiency"]
                best_agent = agent

        report["best_agent"] = best_agent

        
        # Save report
        output_file = f"report_{filename}"
        output_path = os.path.join(OUTPUT_FOLDER, output_file)

        with open(output_path, "w") as f:
            json.dump(report, f, indent=4)

        print(f"Processed {filename} → {output_file}")
