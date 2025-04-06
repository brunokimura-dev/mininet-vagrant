# Mininet Vagrant VM Setup

This repository provides a Vagrant-based virtual environment to run Mininet experiments quickly and consistently.

## Requirements

You must first install [**Vagrant**](https://developer.hashicorp.com/vagrant/install) and [**VirtualBox**](https://www.virtualbox.org/wiki/Downloads) on your host system:

```bash
cd ~
sudo apt-get update
sudo apt-get install -y vagrant virtualbox
```

---

## Step 1: Installation

### Clone the Repository

Download the Vagrant configuration files from this repository:

```bash
cd ~
git clone https://github.com/brunokimura-dev/mininet-vagrant.git
```

### Navigate to the Vagrant Configuration Directory

```bash
cd ~/mininet-vagrant/Vbox/
```

### Deploy the Virtual Machine (Only Once)

Run this command only **once**, as it will create and provision the virtual machine from scratch. Running it again will reset the environment and reinstall everything.

```bash
vagrant up
```

---

## Step 2: Start and Connect to the Vagrant VM

To restart and connect to your virtual machine:

```bash
cd ~/mininet-vagrant/Vbox/
vagrant reload
vagrant ssh
```

---

## Step 3: Run Mininet Experiments

Once connected to the VM, navigate to the shared `workstation` directory, accessible from both your host and the VM:

```bash
cd /workstation/
sh mininet_run.sh mn-ex-base-1.py
```

The script `mininet_run.sh` cleans up previous Mininet instances and executes the provided Python script (`mn-ex-base-1.py`). By default, this script sets up a simple network topology consisting of a client (c), two routers (r1 and r2), and a server (s), as illustrated below:

```
c -- r1 -- r2 -- s
```

The `mn-ex-base-1.py` file defines the network topology, IP addressing, and basic test commands (`ping`, `traceroute`, and `iperf`) between the client and server.

---

## Step 4: Modify and Improve the Network

You can modify the Python script (`mn-ex-base-1.py`) to experiment with different network configurations:

### Edit the Python script

```bash
nano mn-ex-base-1.py
```

### Run the experiment again to test changes

```bash
sh mininet_run.sh mn-ex-base-1.py
```

---
