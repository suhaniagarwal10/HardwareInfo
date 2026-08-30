from abc import ABC, abstractmethod


class HostInfo(ABC):

    def __init__(self):
        self.hostname = ""
        self.memory = ""
        self.cpu = ""
        self.ip = ""
        self.disk_size = ""

    @abstractmethod
    def get_hardware_info(self):
        pass

    def display_hardware_info(self):
        return {
            "hostname": self.hostname,
            "memory": self.memory,
            "cpu": self.cpu,
            "ip": self.ip,
            "disk_size": self.disk_size
        }