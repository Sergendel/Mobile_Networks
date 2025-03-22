# Graph Connectivity Problem

## Repository Overview

This repository contains a solution to the graph connectivity problem inspired by a hypothetical scenario involving a mobile network in city N. In this scenario, each district has a mobile network tower, and all users within that district rely on their respective tower for network services. The towers form a network where users from different districts can communicate as long as the towers remain interconnected.

The purpose of this repository is to provide a tool that calculates how many users become disconnected and therefore unable to receive emergency broadcasts if certain towers within the network are destroyed.

## Input Description

The input is provided in JSON format, including four components:

1. **Network structure:** Connections between towers as pairs.
2. **Users per tower:** Number of users connected to each tower.
3. **Source tower:** Tower initiating the emergency broadcast.
4. **Destroyed towers:** List of towers that are no longer operational.

### Example Input and Output

**Input Example:**
```json
[
  [["A", "B"], ["B", "C"], ["C", "D"]],
  {"A": 10, "B": 20, "C": 30, "D": 40},
  "A",
  ["C"]
]
```

**Output:**
```
70
```

### ASCII Illustration

```
Connected state:
----         ----      ----     ----    
|10| --------|20|------|30|-----|40|
----         ----      ----     ----    
  A           B         C        D

Disconnected state (Tower 'C' destroyed):
----         ----      ----     ----    
|10| --------|20|      |30|     |40|
----         ----      ----     ----    
  A           B         C        D

Total disconnected users: 70 (30 from C + 40 from D)
```

## Repository Structure

### task_1
- **Basic Algorithm Implementation:** A fundamental Python implementation solving the connectivity problem.
- **Documentation:** Detailed instructions on how to build, run the program, and description of the input file format.

### task_2
- **Client-Server Docker Implementation:**
  - Containers hosted separately (client and server).
  - Communication via network sockets.
  - Docker images available on Docker Hub (private account recommended).
  - Multiple input data sets handled sequentially by the client.
  - Demonstration instructions provided for [Play with Docker](https://labs.play-with-docker.com/).

### task_3
- **Web Server Docker Implementation:**
  - Docker container for server implemented as a web server.
  - Client and server deployed using Docker Compose via HTTP REST API.
  - Docker images hosted privately on Docker Hub.
  - YAML deployment file (`docker-compose.yml`) provided for convenient setup.
  - Detailed instructions for demonstration on [Play with Docker](https://labs.play-with-docker.com/).

Explore the repository for detailed instructions on setup, deployment, and demonstration.