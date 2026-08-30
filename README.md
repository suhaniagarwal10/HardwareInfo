# Hardware Info

A Python program that collects basic hardware information from a Windows or Linux system and displays it in JSON format.

## Features

- Detects the operating system
- Collects hostname
- Collects CPU information
- Collects memory information
- Collects IP address
- Collects disk size
- Displays the information in JSON format
- Uses OOP with an abstract base class
- Supports Windows and Linux

## Project Structure

    HardwareInfo/
    ├── hardware/
    │   ├── __init__.py
    │   ├── host_info.py
    │   ├── windows_host.py
    │   └── linux_host.py
    ├── output/
    │   └── hardware_info.json
    ├── screenshots/
    ├── main.py
    ├── README.md
    └── .gitignore

## Requirements

- Python 3.x

## Run

    python main.py

## Output

The program displays the following information:

- Hostname
- Memory
- CPU
- IP address
- Disk size

The output is also saved as a JSON file in the `output` folder.

## OOP Concepts Used

- Abstract class
- Inheritance
- Method overriding
- Polymorphism

`HostInfo` is the parent class, while `WindowsHost` and `LinuxHost` are the child classes.

## Platform Support

Windows uses PowerShell system commands to collect hardware information.

Linux uses Linux system commands such as `lscpu`, `free`, and `lsblk`.