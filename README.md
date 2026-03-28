>[!WARNING]
> This tool is intended for **educational purposes only**.
> Using this tool on systems you do not own or without **explicit written authorization** is illegal.
> Unauthorized use may violate laws such as the
> **Computer Fraud and Abuse Act (CFAA)** and similar legislation in other jurisdictions.
> The author assumes **no responsibility** for misuse or damage caused by this tool.
> Always operate in **controlled and authorized environments only**.

# Reverse-Shell-Python

A simple reverse shell implementation in Python using TCP sockets, built for educational purposes to understand how remote access techniques work in cybersecurity and penetration testing.

---

## How it works?

In a standard shell session, the client connects to a listening server. A reverse shell inverts this model:

1. The **listener** sets up on a specific IP and port and waits for incoming connections
2. The **client** (target) connects outbound to the listener
3. Once connected, the listener can execute commands remotely on the target machine

---

## Why reverse?

Firewalls and NAT typically block inbound connections to internal machines, but allow outbound traffic freely. Since the target initiates the connection, it bypasses most firewall rules making reverse shells far more reliable than bind shells in real world scenarios.

---

## Usage

**1. Start the listener on your machine:**
```bash
python listener.py
```

**2. Run the client on the target machine:**
```bash
python client.py
```

**3. Execute commands from the listener:**
```
[*] Listening on port 8888...
[+] Connection established with ('192.168.1.x', 12345)
shell> whoami
shell> ls
shell> exit
