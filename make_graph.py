import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker
from datetime import date

times = []
download = []
upload = []

dt = date.today().strftime("%m/%d/%Y")
dd = date.today().strftime("%Y%m%d")

with open(f'speed_{dd}.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        times.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))

# print(times, "\n", download, "\n", upload)

plt.figure(figsize=(30, 10))
plt.plot(times, download, label='download', color='r')
plt.plot(times, upload, label='upload', color='b')
plt.xlabel('time').figure.autofmt_xdate(rotation=30)
plt.ylabel('speed in Mb/s')
plt.title(f"internet speed {dt}")
plt.legend()
plt.xticks(times[::3])
plt.savefig(f'speed_graph_{dd}.jpg', bbox_inches='tight')

print("done")
