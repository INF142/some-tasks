
class ToyHost:
    def __init__(self, name, address, nic):
        self._name = name
        self._address = address
        self._nic = nic

    def send(self, destination_address, message):
        print(f"{self._name}| Sending message: {message} from {self._address} "
              f"to {destination_address}")
        self._nic.forward(destination_address, message)

    def recv(self, message):
        print(f"{self._name}| Receiving message: {message}")


class ToySwitch:
    def __init__(self, name, forwarding_table={}):
        self._name = name
        self._forwarding_table = forwarding_table

    def load_forwarding_table(self, forwarding_table):
        self._forwarding_table = forwarding_table

    def forward(self, destination_address, message):
        if destination_address not in self._forwarding_table:
            print("The forwarding table does not have an entry "
                  f"for {destination_address}")
        else:
            nic = self._forwarding_table[destination_address]
            self._pass_through_nic(nic, destination_address, message)

    def _pass_through_nic(self, nic, destination_address, message):
        if isinstance(nic, ToySwitch):
            print(f"{self._name}| Forwarding message: {message} "
                  f"to {destination_address}")
            nic.forward(destination_address, message)
        elif isinstance(nic, ToyHost):
            print(f"{self._name}| Delivering message: {message} "
                  f"to {destination_address}")
            nic.recv(message)
        else:
            print("The device connected to the NIC is not recognized")


if __name__ == "__main__":
    # Example
    switch = ToySwitch("Switch")
    host1 = ToyHost("Host 1", "1.1.1.33", switch)
    host2 = ToyHost("Host 2", "1.1.1.55", switch)
    switch.load_forwarding_table({
        "1.1.1.33": host1,
        "1.1.1.55": host2
    })

    host1.send("1.1.1.55", "Hi there!")
