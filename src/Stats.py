import csv
import os

# Function to update or create the CSV file
def update_stats(labeled_correctly, labeled_incorrectly):
    file_path = 'lifetime_stats.csv'

    # Check if the CSV file exists
    if os.path.exists(file_path):
        # If it exists, read the existing data
        try:
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                
                # Extract existing values
                for row in reader:
                    existing_correct = int(row['Correctly_Labeled'])
                    existing_incorrect = int(row['Incorrectly_Labeled'])

                    # Update with the new values
                    labeled_correctly += existing_correct
                    labeled_incorrectly += existing_incorrect
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    # Write the updated data to the CSV file
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Correctly_Labeled', 'Incorrectly_Labeled']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write the updated values
        writer.writerow({'Correctly_Labeled': labeled_correctly, 'Incorrectly_Labeled': labeled_incorrectly})
    
    return labeled_correctly, labeled_incorrectly
