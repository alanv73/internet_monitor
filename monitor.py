import speedtest
import datetime
import csv
import time
from datetime import date

print("monitoring...")

# servers = [{'url': 'http://speedtest.getwireless.net:8080/speedtest/upload.php', 
#             'lat': '40.7914', 'lon': '-77.8586', 'name': 'State College, PA', 
#             'country': 'United States', 'cc': 'US', 'sponsor': 'Getwireless.net', 
#             'id': '1624', 'host': 'speedtest.getwireless.net:8080', 'd': 0.5488017180303226}]

servers = [{'url': 'http://speedtest.elevatedmsp.com:8080/speedtest/upload.php', 
            'lat': '40.2697', 'lon': '-76.8756', 'name': 'Harrisburg, PA', 
            'country': 'United States', 'cc': 'US', 'sponsor': 'Elevated MSP', 
            'id': '48550', 'host': 'speedtest.elevatedmsp.com:8080', 'd': 101.8194522826376}]

s = speedtest.Speedtest(secure=True)
# s.get_servers()
best_server = s.get_best_server(servers)

dd = date.today().strftime("%Y%m%d")

with open(f'speed_{dd}.csv', mode='w', newline='') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'downspeed', 'upspeed'])
    csv_writer.writeheader()
    while True:
        
        time_now = datetime.datetime.now().strftime("%H:%M:%S")

        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)

        csv_writer.writerow({
            'time': time_now,
            'downspeed': downspeed,
            "upspeed": upspeed
            })
        
        speedcsv.flush()

        n = datetime.datetime.now().strftime("%m/%d/%y %I:%M:%S %p")
        print(f"{n}: {best_server['sponsor']:20} {best_server['name']:20} download: {downspeed} Mbps \t upload: {upspeed} Mbps")

        # 5 minutes sleep
        time.sleep(300)