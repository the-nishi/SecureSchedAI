"""Security-aware enforcement command generator.

For safety and portability, this script prints Linux commands instead of
executing them automatically.
"""

def enforcement_command(pid, action):
    if action == "deprioritize":
        return f"renice +10 -p {pid}"
    if action == "restrict_cpu":
        return f"taskset -cp 0 {pid}"
    if action == "suspend":
        return f"kill -SIGSTOP {pid}"
    if action == "terminate":
        return f"kill -SIGKILL {pid}"
    return "no_action"

if __name__ == "__main__":
    for action in ["deprioritize", "restrict_cpu", "suspend", "terminate"]:
        print(action, "->", enforcement_command(4182, action))
