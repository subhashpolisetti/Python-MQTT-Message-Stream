
# Python MQTT Message Stream

## Overview

This project demonstrates asynchronous message streaming using MQTT for Internet of Things (IoT) applications. We’ll set up a **Publisher** and a **Subscriber** to handle 1,000,000 messages via the Mosquitto MQTT broker.

## Table of Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Subscriber](#running-the-subscriber)
  - [Running the Publisher](#running-the-publisher)
- [Verifying Message Count](#verifying-message-count)
- [Implementation Details](#implementation-details)
- [Screenshots](#screenshots)
- [PDF Instructions](#pdf-instructions)

## Background

MQTT (Message Queue Telemetry Transport) is a messaging protocol developed by IBM in the late 1990s for linking sensors over satellite connections. It enables **asynchronous** communication, making it ideal for IoT applications. In this project, MQTT is used to publish and receive messages securely over a network.

## Prerequisites

1. **Mosquitto**: The MQTT broker to handle the message exchange.
2. **Python 3** with `paho-mqtt` package.

## Installation

1. **Install Mosquitto**:
   ```bash
   sudo apt-get update
   sudo apt-get install -y mosquitto mosquitto-clients
   ```

2. **Install Python package for MQTT**:
   ```bash
   pip install paho-mqtt
   ```

## Usage

### Step 1: Run the Mosquitto Broker
Start the Mosquitto broker to enable message streaming.

```bash
mosquitto -v
```

### Step 2: Running the Subscriber
In one terminal, start the subscriber to begin listening for messages.

```bash
python3 mqtt_sub_cmpe273.py
```

The subscriber will display a message count every 10,000 messages received until it reaches 1,000,000.

### Step 3: Running the Publisher
In a second terminal, start the publisher to send 1,000,000 messages to the topic.

```bash
python3 mqtt_pub_cmpe273.py
```

## Verifying Message Count
The subscriber script will display a cumulative message count to confirm it received all messages. The goal is to reach a total of 1,000,000 messages, matching the publisher’s output.

## Implementation Details
- **Publisher**: This script connects to the broker and publishes messages in a loop.
- **Subscriber**: This script connects to the broker and subscribes to the topic to receive and count messages.


- Subscriber Running and Receiving Messages
- Publisher Sending Messages
- Verification of Message Count




