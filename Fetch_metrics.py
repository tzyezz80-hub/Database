import json, datetime
from mcstatus import JavaServer

# GANTI DENGAN IP SERVER MINECRAFT KAMU
SERVER_IP = "hidupuntukjokowi.falix.me" 

try:
    server = JavaServer.lookup(SERVER_IP, timeout=5)
    status = server.status()
    players = status.players.online
    ping = round(status.latency, 2)
    
    data = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        "players": players,
        "tps": 20.0,
        "ram": 50,
        "cpu": 30,
        "ping": ping,
    }
except Exception as e:
    print(f"Gagal query: {e}")
    data = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        "players": 0, "tps": 0, "ram": 0, "cpu": 0, "ping": 0,
    }

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
