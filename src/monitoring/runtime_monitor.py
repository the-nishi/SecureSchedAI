"""Runtime monitoring demo using psutil."""

import psutil
import json

def collect_runtime_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "process_count": len(psutil.pids()),
        "disk_io": psutil.disk_io_counters()._asdict() if psutil.disk_io_counters() else {},
        "network_io": psutil.net_io_counters()._asdict() if psutil.net_io_counters() else {}
    }

if __name__ == "__main__":
    print(json.dumps(collect_runtime_metrics(), indent=2))
