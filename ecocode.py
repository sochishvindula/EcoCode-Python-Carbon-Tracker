import psutil
import time
import threading
from functools import wraps

class EcoCode:
    """
    I built this to track your code's environmental impact in real-time.
    Think of it as a fitness tracker, but for your code's carbon footprint.
    """
    
    def __init__(self):
        self.is_monitoring = False
        self.energy_data = []
        self.carbon_intensity = 0.4  # kg CO2 per kWh (EU average)
        
    def start_monitoring(self):
        """I start tracking your system's energy usage here"""
        self.is_monitoring = True
        self.monitoring_thread = threading.Thread(target=self._collect_energy_data)
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()
        
    def stop_monitoring(self):
        """I stop the monitoring and calculate your total impact"""
        self.is_monitoring = False
        return self._calculate_carbon_footprint()
        
    def _collect_energy_data(self):
        """I continuously collect CPU and memory usage while your code runs"""
        while self.is_monitoring:
            cpu_percent = psutil.cpu_percent(interval=0.1)
            memory_percent = psutil.virtual_memory().percent
            
            # I estimate energy consumption based on hardware usage
            estimated_watts = self._estimate_power_consumption(cpu_percent, memory_percent)
            
            self.energy_data.append({
                'timestamp': time.time(),
                'watts': estimated_watts,
                'cpu_percent': cpu_percent,
                'memory_percent': memory_percent
            })
            time.sleep(0.5)  # I sample every half second
            
    def _estimate_power_consumption(self, cpu_percent, memory_percent):
        """
        I calculate approximate power usage based on component activity.
        This is my simplified model - real systems vary, but it gives you 
        a meaningful estimate for comparison.
        """
        base_power = 15  # Idle system power (watts)
        cpu_power = (cpu_percent / 100) * 65  # Max CPU power under full load
        memory_power = (memory_percent / 100) * 10  # RAM power usage
        
        return base_power + cpu_power + memory_power
        
    def _calculate_carbon_footprint(self):
        """I convert your energy usage into CO2 emissions"""
        if not self.energy_data:
            return {'error': 'No monitoring data collected'}
            
        total_time_hours = (self.energy_data[-1]['timestamp'] - 
                          self.energy_data[0]['timestamp']) / 3600
        
        avg_watts = sum(d['watts'] for d in self.energy_data) / len(self.energy_data)
        energy_kwh = (avg_watts * total_time_hours) / 1000
        
        co2_grams = energy_kwh * self.carbon_intensity * 1000
        
        return {
            'duration_seconds': len(self.energy_data) * 0.5,
            'average_watts': round(avg_watts, 2),
            'energy_kwh': round(energy_kwh, 6),
            'co2_grams': round(co2_grams, 3),
            'equivalent_trees_needed': round(co2_grams / 21000, 4)
        }

def eco_monitor(func):
    """
    I created this decorator so you can easily track any function's impact.
    Just add @eco_monitor above your function and I'll do the rest.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracker = EcoCode()
        
        print(f"🌱 I'm now monitoring the environmental impact of '{func.__name__}'")
        tracker.start_monitoring()
        
        try:
            result = func(*args, **kwargs)
        finally:
            impact = tracker.stop_monitoring()
            
            print(f"\n📊 Environmental Impact Report for '{func.__name__}':")
            print(f"   ⏱️  Duration: {impact['duration_seconds']:.1f} seconds")
            print(f"   ⚡ Average Power: {impact['average_watts']} watts")
            print(f"   🔋 Energy Used: {impact['energy_kwh']} kWh")
            print(f"   🌍 CO2 Emitted: {impact['co2_grams']} grams")
            print(f"   🌳 Tree-hours needed to offset: {impact['equivalent_trees_needed']}")
            
            if impact['co2_grams'] > 10:
                print(f"   ⚠️  I noticed high emissions - consider optimizing this function!")
            else:
                print(f"   ✅ Great job! This function has low environmental impact.")
        
        return result
    return wrapper
