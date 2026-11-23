import os


def generate_report(candidates, output_folder="outputs"):

    os.makedirs(output_folder, exist_ok=True)

    report_path = os.path.join(
        output_folder,
        "candidate_report.txt"
    )

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("AUTOMATED RESUME SCREENING REPORT\n")
        file.write("=" * 40 + "\n\n")

        for candidate in candidates:

            file.write("Candidate: " + candidate["candidate_name"] + "\n")

            file.write(
                "Matching Score: "
                + str(candidate["match_percentage"])
                + "%\n"
            )

            file.write(
                "Matched Skills: "
                + ", ".join(candidate["matched_skills"])
                + "\n"
            )

            file.write(
                "Missing Skills: "
                + ", ".join(candidate["missing_skills"])
                + "\n"
            )

            file.write("-" * 40 + "\n\n")

    print("\nReport generated successfully!")
    print("Saved at:", report_path)