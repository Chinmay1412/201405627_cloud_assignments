Mininet is a network emulator. It runs a collection of end-hosts, switches, routers, and links on a single Linux kernel. It uses lightweight virtualization to make a single system look like a complete network, running the same kernel, system, and user code.

For running program, two command line arguments are needed. One specifies x number of hosts per switch and second number of switches. Here this program will create below topology:
->All the switches should be connected to each other
->Odd hosts can only talk to each other and even hosts can talk to each other
  E.g h1 should only be able to ping h3, h5 and h2 should be able to ping h4, h6
->All the communication should be throttled to 1 mbps for odd hosts and 2 mbps for even hosts  