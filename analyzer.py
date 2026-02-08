# analyzer.py
import time
from config import (
    CPU_THRESHOLD_PERCENT,
    CPU_SUSTAINED_SECONDS,
    MEMORY_THRESHOLD_PERCENT,
    DISK_MIN_FREE_PERCENT
)

_cpu_high_start_time = None


def analyze(metrics):
    """
    Input: metrics dict from observer
    Output: list of alert dicts
    """
    global _cpu_high_start_time
    alerts = []

    # ---- CPU (sustained) ----
    if metrics["cpu"] > CPU_THRESHOLD_PERCENT:
        if _cpu_high_start_time is None:
            _cpu_high_start_time = time.time()
        else:
            duration = time.time() - _cpu_high_start_time
            if duration >= CPU_SUSTAINED_SECONDS:
                alerts.append({
                    "type": "CPU_HIGH",
                    "severity": "HIGH",
                    "message": f"CPU usage above {CPU_THRESHOLD_PERCENT}% for {int(duration)} seconds"
                })
    else:
        _cpu_high_start_time = None

    # ---- Memory ----
    if metrics["memory"] > MEMORY_THRESHOLD_PERCENT:
        alerts.append({
            "type": "MEMORY_HIGH",
            "severity": "MEDIUM",
            "message": f"Memory usage above {MEMORY_THRESHOLD_PERCENT}%"
        })

    # ---- Disk ----
    for disk in metrics["disks"]:
        if disk["free_percent"] < DISK_MIN_FREE_PERCENT:
            alerts.append({
                "type": "DISK_LOW",
                "severity": "HIGH",
                "message": f"Low disk space on {disk['mount']} (free {disk['free_percent']}%)"
            })

    return alerts
