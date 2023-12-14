import speedtest
import os

s = speedtest.Speedtest(secure=True)

def clear_screen():
    # Clearing the Screen
    
    if(os.name == 'posix'): # posix is os name for Linux or mac
        os.system('clear')
    else: # else screen will be cleared for windows
        os.system('cls')

def server_choices():
    servers = s.get_servers()

    s1 = [servers[server] for server in servers]
    s2 = [svr for svrs in s1 for svr in svrs]
    names_only = [f'{s["sponsor"]:40} {s["name"]}' for s in s2]

    print("\nSPEED TEST SERVERS")
    print(f"\n{'No.':^5} {'Sponsor':^40} {'Name':^25}")
    print(f"----- ---------------------------------------- -------------------------")

    i = 0
    for svr in names_only:
        i += 1
        print(f"{i:<5} {svr}")
    return s2

clear_screen()
servers = server_choices()

s_num = 0

while s_num < 1 or s_num > len(servers):
    user_input = input("\nSelect a Server (Q to quit, R to reload servers): ")

    if user_input.lower() == "q":
        exit()
    if user_input.lower() == "r":
        clear_screen()
        servers = server_choices()
        continue
    

    s_num = int(user_input)

test_server = servers[s_num-1]

print("\nSELECTED SERVER")
print("---------------")
print(f'{test_server["sponsor"]:40} {test_server["name"]:25}')

print("\nTesting Internet Speed...")

best_server = s.get_best_server([test_server])

d = round((round(s.download()) / 1048576), 2)
u = round((round(s.upload()) / 1048576), 2)

print("\nSPEED TEST")
print("----------")
print(f"{best_server['sponsor']:40} {best_server['name']:25} download: {d} Mbps \t upload: {u} Mbps")
