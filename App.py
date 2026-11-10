import json, os, datetime
from mcstatus import JavaServer

host = os.environ.get("MC_HOST", "localhost")
port = int(os.environ.get("MC_PORT", 25565))

try:
    server = JavaServer.lookup(f"{host}:{port}", timeout=5)
    status = server.status()

    # Ping (latency) dari query
    ping = round(status.latency, 2)  # dalam ms

    # Players online
    players = status.players.online

    # TPS, RAM, CPU: tidak tersedia via query publik.
    # Ganti dengan nilai dari RCON/plugin jika ada.
    # Contoh dummy (hapus jika sudah punya sumber nyata):
    tps = 20.0
    ram = 0
    cpu = 0

    data = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        "players": players,
        "tps": tps,
        "ram": ram,
        "cpu": cpu,
        "ping": ping
    }

except Exception as e:
    print(f"Gagal query server: {e}")
    # Tetap update timestamp agar dashboard tahu percobaan terakhir
    data = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        "players": 0, "tps": 0, "ram": 0, "cpu": 0, "ping": 0,
        "error": str(e)
    }

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print("Metrics updated:", data)
