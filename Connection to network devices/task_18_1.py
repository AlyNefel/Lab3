from netmiko import ConnectHandler, NetmikoTimeoutException
import yaml

def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            return ssh.send_command(command)
    except NetmikoTimeoutException:
        return f"⏱️ Connection timed out for {device['ip']}"

if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))
