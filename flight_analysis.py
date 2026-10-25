import csv
import os


def load_flight_data(filepath):
  """Requirement 1 & 4: Reads information from a file using the csv and os modules."""
  flights = []
  if not os.path.exists(filepath):
    print(f"Error: The file '{filepath}' was not found.")
    return flights

  with open(filepath, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
      flights.append(row)
  return flights


def analyze_and_save_delays(flights, output_filename="flight_summary_report.txt"):
  """Requirements 2, 3, & 5: Uses loops, if statements, two functions, and writes the

  analysis results to a file.
  """
  total_records = len(flights)
  if total_records == 0:
    print("No flight records found to analyze.")
    return

  delayed_count = 0
  on_time_count = 0
  valid_flight_count = 0
  total_dep_delay = 0.0

  # Requirement 2: for loop iterating through flight records
  for flight in flights:
    raw_delay = flight.get("DepDelayMinutes", "").strip()

    # Skip cancelled or missing delay values
    if not raw_delay:
      continue

    try:
      dep_delay = float(raw_delay)
      total_dep_delay += dep_delay
      valid_flight_count += 1

      # Requirement 3: if statement evaluating delay status (>15 mins)
      if dep_delay > 15:
        delayed_count += 1
      else:
        on_time_count += 1
    except ValueError:
      continue

  avg_delay = (
      total_dep_delay / valid_flight_count if valid_flight_count > 0 else 0
  )

  # Requirement 5: Write something to a file
  report_content = (
      f"=== FLIGHT DATA ANALYSIS REPORT ===\n"
      f"Total Records in File: {total_records}\n"
      f"Valid Flights Analyzed: {valid_flight_count}\n"
      f"Delayed Flights (>15 mins): {delayed_count}\n"
      f"On-Time / Minor Delay Flights: {on_time_count}\n"
      f"Average Departure Delay: {avg_delay:.2f} minutes\n"
  )

  with open(output_filename, "w", encoding="utf-8") as out_file:
    out_file.write(report_content)

  print(f"Analysis complete! Report successfully saved to {output_filename}")


if __name__ == "__main__":
  # File provided for analysis
  data_file = "subsample_100_GNV (1).csv"

  print(f"Reading flight records from {data_file}...")
  flight_data = load_flight_data(data_file)

  if flight_data:
    analyze_and_save_delays(flight_data)