import platform
import socket
import subprocess

from .host_info import HostInfo


class WindowsHost(HostInfo):

    def get_hardware_info(self):
        self.hostname = platform.node()
        self.cpu = self.get_cpu()
        self.memory = self.get_memory()
        self.ip = socket.gethostbyname(self.hostname)
        self.disk_size = self.get_disk_size()

    def get_cpu(self):
        result = subprocess.check_output(
            [
                "powershell",
                "-Command",
                "(Get-CimInstance Win32_Processor).Name"
            ],
            text=True
        )

        return result.strip()

    def get_memory(self):
        result = subprocess.check_output(
            [
                "powershell",
                "-Command",
                "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory"
            ],
            text=True
        )

        memory = int(result.strip())
        return f"{memory / (1024 ** 3):.2f} GB"

    def get_disk_size(self):
        result = subprocess.check_output(
            [
                "powershell",
                "-Command",
                "(Get-CimInstance Win32_LogicalDisk -Filter \"DeviceID='C:'\").Size"
            ],
            text=True
        )

        size = int(result.strip())
        return f"{size / (1024 ** 3):.2f} GB"