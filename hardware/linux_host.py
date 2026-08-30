import platform
import socket
import subprocess

from .host_info import HostInfo


class LinuxHost(HostInfo):

    def get_hardware_info(self):
        self.hostname = platform.node()
        self.cpu = self.get_cpu()
        self.memory = self.get_memory()
        self.ip = socket.gethostbyname(self.hostname)
        self.disk_size = self.get_disk_size()

    def get_cpu(self):
        result = subprocess.check_output(
            "lscpu | grep 'Model name'",
            shell=True,
            text=True
        )

        return result.split(":", 1)[1].strip()

    def get_memory(self):
        result = subprocess.check_output(
            "free -h | grep Mem",
            shell=True,
            text=True
        )

        return result.split()[1]

    def get_disk_size(self):
        result = subprocess.check_output(
            "lsblk -b -d -o SIZE",
            shell=True,
            text=True
        )

        size = int(result.splitlines()[1])
        return f"{size / (1024 ** 3):.2f} GB"