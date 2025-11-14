# Initialize clocks
clock1 = 0
clock2 = 0

# Local event
def event1():
    global clock1
    clock1 += 1
    print("Event at P1:", clock1)

# Send message
def send():
    global clock1
    clock1 += 1
    print("P1 sends message at:", clock1)
    return clock1

# Receive message
def receive(msg_time):
    global clock2
    clock2 = max(clock2, msg_time) + 1
    print("P2 receives message at:", clock2)
    
def event2():
    global clock2
    clock2 += 1
    print("Event at P2:", clock2)

# Simulation
event1()
msg = send()
receive(msg)
event2()

import ntplib
from time import ctime

# Create NTP client
client = ntplib.NTPClient()

# Request time from public NTP server
response = client.request('pool.ntp.org')

# Display synchronized time
print("Synchronized time:", ctime(response.tx_time))

import socket, struct, time

def ntp_time(host="time.google.com"):
    msg = b'\x1b' + 47 * b'\0'
    t1 = time.time()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(msg, (host, 123))
    data, _ = s.recvfrom(48)
    t4 = time.time()
    t = struct.unpack('!12I', data)[10] - 2208988800
    print("NTP Time:", time.ctime(t))
    print("Local Time:", time.ctime(time.time()))
    print("Offset:", t - (t1 + t4) / 2)

ntp_time()
