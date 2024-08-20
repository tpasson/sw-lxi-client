# LXI Reader

This Python script allows you to connect to a lab multimeter or other lab equipment over a TCP/IP network using the LXI protocol and retrieve a DC voltage measurement. The script communicates with the multimeter using SCPI commands over a specified IP address and port. This script can easily be extended and adapted to retrieve other types of measurements or control different functions of the lab equipment. For example, by modifying the SCPI commands, you could measure current, resistance, or frequency, or even configure the instrument's settings. Additionally, you can extend the script to log data over time, automate calibration routines, or integrate with other data acquisition systems for more complex experiments.

## Features

- Connects to an LXI-compliant multimeter using TCP/IP.
- Sends SCPI command to measure DC voltage.
- Receives and displays the measurement result.

## Prerequisites

- Python 3.x
- A network-connected lab device that supports SCPI commands over TCP/IP (typically LXI-compliant).

## Tested Devices

- **Siglent SDM3045X**: This script has been tested and verified to work with the Siglent SDM3045X multimeter.

## Installation

Clone the repository to your local machine

## Usage

To use the script, run the `read_meter.py` script from the command line, passing the IP address of your multimeter as a command line argument.

### Example

```bash
python3 read_meter.py 192.168.10.100
```

This command connects to the multimeter at IP address `192.168.10.100` on port `5025`, sends the SCPI command to measure DC voltage, and prints the result.

### Command Line Parameters

- `<multimeter_ip>`: The IP address of your network-connected multimeter.

### Error Handling

If the connection to the multimeter fails (e.g., due to a timeout or incorrect IP address), the script will display an appropriate error message.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## Issues

If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

## Acknowledgements

- [SCPI (Standard Commands for Programmable Instruments)](https://en.wikipedia.org/wiki/Standard_Commands_for_Programmable_Instruments)
- [LXI (LAN eXtensions for Instrumentation)](https://www.lxistandard.org/)