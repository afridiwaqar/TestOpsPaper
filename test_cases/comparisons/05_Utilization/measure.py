import psutil
import time
import subprocess
import threading

def monitor_process(pid, interval=1):
    try:
        process = psutil.Process(pid)
        while True:
            cpu_usage = process.cpu_percent(interval=interval)
            memory_info = process.memory_info()
            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {memory_info.rss / (1024 * 1024):.2f} MB")
            time.sleep(interval)
    except psutil.NoSuchProcess:
        print("Process ended")
        return

def run_test_script(script_command):
    process = subprocess.Popen(script_command, shell=True)
    monitor_thread = threading.Thread(target=monitor_process, args=(process.pid,))
    monitor_thread.start()
    process.wait()
    monitor_thread.join()

# Example usage for a Selenium test script
selenium_command = "python3.8 /home/waqar/FAST/TestOps/test_cases/comparisons/01_Performance/selenium_multiple.py"
run_test_script(selenium_command)

# Similarly, you can run other test scripts like Playwright, Splinter, Behave, and Robot Framework
# playwright_command = "playwright test"
# run_test_script(playwright_command)

# splinter_command = "python splinter_test_script.py"
# run_test_script(splinter_command)

# behave_command = "behave features"
# run_test_script(behave_command)

# robot_command = "robot tests"
# run_test_script(robot_command)

