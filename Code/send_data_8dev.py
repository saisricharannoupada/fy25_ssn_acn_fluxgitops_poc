from azure.iot.device import IoTHubDeviceClient, Message
import time
import random
 
# Define the connection strings for each device
DEVICE_CONNECTION_STRINGS = {
    "ID01": "HostName=fy25ioth1.azure-devices.net;DeviceId=ID01;SharedAccessKey=fWoKtPxwBNCQzEKXuntT+WhH43gbYEn69acghn/gYvY=",
    "ID02": "HostName=fy25ioth1.azure-devices.net;DeviceId=ID02;SharedAccessKey=tDKfSKOTVgHjbp7t+xABdFZX43QSU793tUka0R42uHQ=",
    "ID03": "HostName=fy25ioth1.azure-devices.net;DeviceId=ID03;SharedAccessKey=lXRRsNeCNmYuPbBTNyk0Y6nDeiwykhv6jFEsWZ7ojIk=",
    "ID04": "HostName=fy25ioth1.azure-devices.net;DeviceId=ID04;SharedAccessKey=BaYt80AOaVBAoj4wqRjYqxgqPNtF8FMyCBOty1nvEXI=",
   # "ID05": "",
   # "ID06": "",
   # "ID07": "",
   # "ID08": ""
}
 
# Define different data formats for each device
def get_device_data(device_id):
    if device_id == "ID01":
        # Example data for ID01: Environmental data
        return {"device_id": "01", "Temperature": random.uniform(15, 30), "Humidity": random.uniform(30, 70)}
    elif device_id == "ID02":
        # Example data for ID02: Motion sensor data
        return {"device_id": "02" ,"Motion_count": random.randint(0, 5)}
    elif device_id == "ID03":
        # Example data for ID03: Power consumption data
        return {"device_id": "03", "Power": random.uniform(100, 500), "Voltage": random.uniform(220, 240)}
    elif device_id == "ID04":
        # Example data for ID04: Location data
        return {"device_id": "04", "Latitude": random.uniform(-90, 90), "Longitude": random.uniform(-180, 180)}
    #elif device_id == "ID05":
    #    # Example data for ID06: Motion sensor data
    #    return {"device_id": "05" ,"Motion_count": random.randint(0, 5)}
    #elif device_id == "ID06":
    #    # Example data for ID07: Power consumption data
    #    return {"device_id": "06", "Power": random.uniform(100, 500), "Voltage": random.uniform(220, 240)}
    #elif device_id == "ID07":
    #    # Example data for ID08: Location data
    #    return {"device_id": "07", "Latitude": random.uniform(-90, 90), "Longitude": random.uniform(-180, 180)}
    #elif device_id == "ID08":
    #    # Example data for ID08: Location data
    #    return {"device_id": "08", "Temperature": random.uniform(15, 30), "Humidity": random.uniform(30, 70)}
    else:
        return {}
 
# Function to send data from a specific device
def send_data_from_device(device_id, connection_string):
    client = IoTHubDeviceClient.create_from_connection_string(connection_string)
    try:
        print(f"Connecting {device_id} to IoT Hub...")
        client.connect()
        while True:
            data = get_device_data(device_id)
            message = Message(str(data))
            print(f"{device_id} sending message: {data}")
            client.send_message(message)
            print(f"{device_id} message sent successfully!")
            time.sleep(5)  # Send data every 5 seconds
    except KeyboardInterrupt:
        print(f"Stopped {device_id} by the user.")
    finally:
        client.disconnect()
        print(f"Disconnected {device_id} from IoT Hub.")
 
# Main function to simulate all devices
if __name__ == "__main__":
    import threading
 
    # Create threads for each device
    threads = []
    for device_id, conn_str in DEVICE_CONNECTION_STRINGS.items():
        thread = threading.Thread(target=send_data_from_device, args=(device_id, conn_str))
        threads.append(thread)
        thread.start()
 
    # Wait for all threads to finish
    for thread in threads:
        thread.join()