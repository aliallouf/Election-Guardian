import random
import time
import sys
import os

# Ensure the script can find the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import StreamMonitor

def run_simulation(duration=20, flood_intensity=0.6):
    monitor = StreamMonitor(strict=True)
    history = []
    bad_actor_ip = "192.168.1.100"
    
    print("="*50)
    print("🚀 ELECTION GUARDIAN: STARTING NETWORK MONITORING")
    print(f"Targeting intensity: {flood_intensity*100}% | Mode: Strict Majority")
    print("="*50)
    
    try:
        for i in range(duration):
            # 60% chance of the bad actor, 40% chance of random noise
            if random.random() < flood_intensity:
                ip = bad_actor_ip
            else:
                ip = f"10.0.0.{random.randint(1, 255)}"
                
            history.append(ip)
            current_lead = monitor.process_element(ip)
            
            # Print a status bar
            print(f"Packet {i+1:02d}: {ip:<15} | Lead: {current_lead:<15} | Votes: {monitor.votes}")
            time.sleep(0.2)

        print("-" * 50)
        final_result = monitor.verify_majority(history)
        
        if final_result != -1:
            print(f"⚠️  ALERT: Dominant Signal Confirmed! Bad Actor: {final_result}")
        else:
            print("✅ STATUS: No dominant bad actor detected. System safe.")
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    run_simulation()
import random
import time
import sys
import os

# Ensure the script can find the 'src' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.monitor import StreamMonitor

def run_simulation(duration=20, flood_intensity=0.6):
    monitor = StreamMonitor(strict=True)
    history = []
    bad_actor_ip = "192.168.1.100"
    
    print("="*50)
    print("🚀 ELECTION GUARDIAN: STARTING NETWORK MONITORING")
    print(f"Targeting intensity: {flood_intensity*100}% | Mode: Strict Majority")
    print("="*50)
    
    try:
        for i in range(duration):
            # 60% chance of the bad actor, 40% chance of random noise
            if random.random() < flood_intensity:
                ip = bad_actor_ip
            else:
                ip = f"10.0.0.{random.randint(1, 255)}"
                
            history.append(ip)
            current_lead = monitor.process_element(ip)
            
            # Print a status bar
            print(f"Packet {i+1:02d}: {ip:<15} | Lead: {current_lead:<15} | Votes: {monitor.votes}")
            time.sleep(0.2)

        print("-" * 50)
        final_result = monitor.verify_majority(history)
        
        if final_result != -1:
            print(f"⚠️  ALERT: Dominant Signal Confirmed! Bad Actor: {final_result}")
        else:
            print("✅ STATUS: No dominant bad actor detected. System safe.")
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    run_simulation()