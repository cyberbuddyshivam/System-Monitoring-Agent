# agent.py
import time
from observer import observe
from analyzer import analyze
from memory import should_alert, record_alert
from notifier import send_sms
from config import CHECK_INTERVAL_SECONDS


def print_system_snapshot(metrics):
    print("📊 System Snapshot:")
    print(f"   CPU Usage    : {metrics['cpu']}%")
    print(f"   Memory Usage : {metrics['memory']}%")

    for d in metrics["disks"]:
        print(f"   Disk {d['mount']} Free : {d['free_percent']}%")

    if metrics["battery"]:
        print(
            f"   Battery      : {metrics['battery']['percent']}% "
            f"({'Plugged' if metrics['battery']['plugged'] else 'On Battery'})"
        )


print("🟢 System Monitoring Agent running (production mode)")

while True:
    print("⏱️ Agent heartbeat — monitoring system...")

    metrics = observe()
    alerts = analyze(metrics)

    if not alerts:
        # No alerts this cycle
        time.sleep(CHECK_INTERVAL_SECONDS)
        continue

    for alert in alerts:
        if should_alert(alert["type"]):
            print("\n" + "=" * 50)
            print(f"🚨 ALERT TRIGGERED: {alert['type']}")
            print(f"Severity : {alert['severity']}")
            print(f"Reason   : {alert['message']}")
            print_system_snapshot(metrics)
            print("=" * 50)

            sms_text = (
                f"ALERT [{alert['severity']}]\n"
                f"{alert['type']}\n"
                f"{alert['message']}"
            )

            send_sms(sms_text)
            print("✅ SMS sent successfully")

            record_alert(alert["type"])
        else:
            print(f"⏳ Suppressed alert (cooldown): {alert['type']}")

    time.sleep(CHECK_INTERVAL_SECONDS)
