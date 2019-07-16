import csv

with open("onsite_6-18.csv", "r") as rfh, open("onsite_6-18.csv", "a") as wfh:
	r = csv.reader(rfh, delimiter=',')
	w = csv.writer(wfh)
	w.writerow("********TEST************, *****************MAXLITE TEST, 100, 100, 100, ")
	for row in r:
			print(", ".join(row))