# observer.py
import psutil

def observe():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent

    disks = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disks.append({
                "mount": part.mountpoint,
                "free_percent": 100 - usage.percent
            })
        except PermissionError:
            continue

    battery = None
    if hasattr(psutil, "sensors_battery"):
        b = psutil.sensors_battery()
        if b:
            battery = {
                "percent": b.percent,
                "plugged": b.power_plugged
            }

    return {
        "cpu": cpu_percent,
        "memory": memory_percent,
        "disks": disks,
        "battery": battery
    }
