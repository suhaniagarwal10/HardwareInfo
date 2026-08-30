import json
import platform

from hardware.windows_host import WindowsHost
from hardware.linux_host import LinuxHost


def main():

    if platform.system() == "Windows":
        host = WindowsHost()

    elif platform.system() == "Linux":
        host = LinuxHost()

    else:
        raise OSError("Unsupported operating system")

    host.get_hardware_info()

    hardware_info = host.display_hardware_info()

    print(json.dumps(hardware_info, indent=4))


if __name__ == "__main__":
    main()