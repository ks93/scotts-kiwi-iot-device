from azure.iot.device import IoTHubDeviceClient


def iothub_client_init(connection_string):
    client = IoTHubDeviceClient.create_from_connection_string(connection_string)
    return client
