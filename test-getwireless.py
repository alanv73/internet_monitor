import speedtest

source="67.22.28.251"
speedtest.SOURCE=source

s = speedtest.Speedtest(secure=True)

best_server = s.get_best_server([{'url': 'http://speedtest.getwireless.net:8080/speedtest/upload.php', 
            'lat': '40.7914', 'lon': '-77.8586', 'name': 'State College, PA', 
            'country': 'United States', 'cc': 'US', 'sponsor': 'Getwireless.net', 
            'id': '1624', 'host': 'speedtest.getwireless.net:8080', 'd': 0.5488017180303226}])

print("\nSELECTED SERVER")
print("---------------")
print(f"{best_server['sponsor']:40} \t {best_server['name']}", end="\n\n")

print("\nTesting Internet Speed...")

d = round((round(s.download()) / 1048576), 2)
u = round((round(s.upload()) / 1048576), 2)

print("\nSPEED TEST")
print("----------")
print(f"{best_server['sponsor']:40} {best_server['name']:25} download: {d} Mbps \t upload: {u} Mbps")
