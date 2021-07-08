import csv
import os


csv_ext = ".csv"
csv_file = f"emails{csv_ext}"
new_domain = "@hello.com"
final_filename = f"new_emails{csv_ext}"

emails = []
with open(csv_file, mode="r") as csvfile:
    email_reader = csv.DictReader(csvfile)
    line_count = 0
    header = []
    for row in email_reader:
        emails.append(row)
        if line_count == 0:
            header = row.keys()
        e_add = row["EmailAddress"]
        username = e_add.split("@")[0]
        new_add = f"{username}{new_domain}"
        row["EmailAddress"] = new_add
        line_count += 1

i = 0
while os.path.exists(final_filename):
    final_filename = f"new_emails_{i}{csv_ext}"
    i += 1

with open(final_filename, "w") as f:
    dict_writer = csv.DictWriter(f, fieldnames=header)
    dict_writer.writeheader()
    dict_writer.writerows(emails)
