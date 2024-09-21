# Layer_2_Port-Channel_Automation
This Python script automates the configuration of Port-Channel (EtherChannel) interfaces across multiple Cisco switches using the Netmiko library. It allows network engineers to quickly configure trunking and EtherChannel on a range of interfaces across multiple devices.
# Cisco Port-Channel Automation Script

This Python script automates the configuration of Port-Channel (EtherChannel) interfaces on multiple Cisco switches. It uses the Netmiko library to establish SSH connections to the devices and apply interface trunking and EtherChannel settings. The script allows network administrators to streamline the configuration process for port aggregation, ensuring consistent settings across multiple devices.

## Features

- **Batch Device Configuration**: Configures multiple switches by taking a list of IP addresses.
- **Port-Channel Setup**: Configures interfaces as trunk and adds them to an EtherChannel group.
- **Verification**: Automatically verifies the EtherChannel setup by showing the summary after configuration.
- **Trunk Settings**: Sets up the interface with trunk encapsulation and mode.

## Requirements

- Python 3.x
- Netmiko library (`pip install netmiko`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/asarmohammad125/Layer_2_Port-Channel_Automation.git
    ```

2. Install the required Python libraries:
    ```bash
    pip install netmiko
    ```

3. Update the `host_list` variable in the script with the IP addresses of your Cisco devices.

## Usage

1. Run the script:
    ```bash
    python port_channel_automation.py
    ```

2. You will be prompted to provide the following inputs:
    - **Username**: Your SSH username for the Cisco devices.
    - **Password**: Your SSH password.
    - **Interface Range**: The interface range you wish to configure as Port-Channel (e.g., Gig0/0-3).

3. The script will:
    - Log into each device listed in the `host_list`.
    - Apply the configuration for the specified interface range to set trunk mode and Port-Channel.
    - Verify the EtherChannel setup by displaying the `show etherchannel summary` output.

## Example

```bash
Enter the Username: admin
Enter the Password: *****
Enter the interface range Gig0/0-? Note: value should only be number eg.; 1,2,3 etc: 3
