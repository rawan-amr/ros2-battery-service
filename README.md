# ROS2 Battery Service

## Project Overview

This project extends the Robot Status Monitor project by exposing live battery data through a custom ROS2 service.

The system subscribes to the `/battery_status` topic published by the Robot Status Monitor package and provides the current battery level through a ROS2 service.

The project was built using ROS2 Jazzy and Python.

## Project Dependency

This project builds on the Robot Status Monitor project.

The `battery_server` node subscribes to the `/battery_status` topic published by the `battery_publisher` node from the Robot Status Monitor package.

This demonstrates communication between independent ROS2 packages using ROS2 topics and services.

Workflow:

```text
Robot Status Monitor
        |
        v
 /battery_status
        |
        v
 Battery Service
        |
        v
 /battery_level
```

## Motivation

The goal of this project was to gain hands-on experience with:

* ROS2 Services
* Service Servers and Clients
* Custom ROS2 Interfaces
* Inter-package communication
* ROS2 asynchronous service calls
* Integration between publishers, subscribers, and services
* ROS2 build workflow and interface generation

## System Architecture

```text
Battery Publisher
        |
        v
 /battery_status (Int64)
        |
        v
 Battery Server
        |
        v
 /battery_level Service
        |
        v
 Battery Client
```

## Packages

### battery_interfaces

Contains the custom ROS2 service definition.

Service:

```text
BatteryLevel.srv
```

Definition:

```text
---
int64 battery_level
```

### battery_service

Contains:

* battery_server
* battery_client

## Topics

### /battery_status

Message Type:

```text
std_msgs/msg/Int64
```

Provides the current battery percentage published by the Robot Status Monitor project.

Example output:

```text
Battery: 100%
Battery: 99%
Battery: 98%
```

## Services

### /battery_level

Service Type:

```text
battery_interfaces/srv/BatteryLevel
```

Returns the latest battery level received from `/battery_status`.

## Nodes

### battery_server

Responsibilities:

* Subscribes to `/battery_status`
* Stores the latest battery value
* Provides the `/battery_level` service
* Returns the current battery percentage when requested

### battery_client

Responsibilities:

* Sends a request to `/battery_level`
* Receives the service response
* Displays the current battery level

## Example Output

### Server

```text
Battery updated: 75%
Battery updated: 74%
Battery updated: 73%
```

### Client

```text
Current Battery Level: 73%
```

### ROS2 CLI Service Call

Command:

```bash
ros2 service call /battery_level battery_interfaces/srv/BatteryLevel
```

Example response:

```text
requester: making request: battery_interfaces.srv.BatteryLevel_Request()

response:
battery_interfaces.srv.BatteryLevel_Response(
    battery_level=73
)
```

## Technologies Used

* ROS2 Jazzy
* Python
* Ubuntu 24.04
* Git
* GitHub

## How to Run

Build the packages:

```bash
colcon build 
source install/setup.bash
```

Start the battery publisher from the Robot Status Monitor project:

```bash
ros2 run robot_status battery_publisher
```

Run the service server:

```bash
ros2 run battery_service battery_server
```

Run the service client:

```bash
ros2 run battery_service battery_client
```

Optional CLI test:

```bash
ros2 service call /battery_level battery_interfaces/srv/BatteryLevel
```

## Lessons Learned

During development I learned how to:

* Create custom ROS2 service interfaces
* Generate interfaces using ROS2 build tools
* Implement service servers and clients
* Use asynchronous service requests
* Connect ROS2 services with live topic data
* Build systems that communicate across multiple ROS2 packages
* Integrate ROS2 topics and services within the same workflow

## Future Improvements

Possible future enhancements include:

* Returning additional battery information
* Creating more robot monitoring services
* Supporting multiple service requests
* Adding launch files for automated startup
* Integrating ROS2 Actions for long-running robot operations
```
