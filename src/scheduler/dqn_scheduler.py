"""Lightweight DQN-style scheduler placeholder used for reproducible demo.

The paper describes a DQN scheduler. This script provides a minimal
decision function for reviewer-side execution and integration testing.
"""

def select_scheduling_action(cpu_usage, memory_usage, queue_length, io_wait):
    risk_load = 0.4 * cpu_usage + 0.3 * memory_usage + 0.2 * queue_length + 0.1 * io_wait
    if risk_load > 85:
        return "defer_or_restrict"
    if risk_load > 65:
        return "adjust_priority"
    return "normal_schedule"

if __name__ == "__main__":
    action = select_scheduling_action(cpu_usage=82, memory_usage=61, queue_length=12, io_wait=8)
    print({"scheduler_action": action})
