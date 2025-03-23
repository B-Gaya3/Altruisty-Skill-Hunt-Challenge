def analyze_power_consumption(readings):
    if any(r < 10 or r > 200 for r in readings):
        print("INVALID INPUT")
        return
    sensors = [0] * 5
    for i in range(5):
        sensors[i] = sum(readings[i::5]) / 4

    if all(avg < 50 for avg in sensors):
        print("Energy consumption is optimal.")
        return

    max_avg = max(sensors)
    sensor_number = sensors.index(max_avg) + 1
    print("Sensor Number :", sensor_number)


readings = list(map(int, input().split()))

if len(readings) != 20:
    print("INVALID INPUT")
else:
    analyze_power_consumption(readings)
