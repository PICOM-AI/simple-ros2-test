# simple-ros2-test


## Test 1
Setup hardware as figure bellow
![Test 1](figs/1.jpg)

### Prepare (need internet)
#### On Raspberry Pi:
Build docker for Publisher
```bash
git clone https://github.com/PICOM-AI/simple-ros2-test.git
cd simple-ros2-test
bash 1.1.build_publisher.sh
```

#### On Laptop:
Build docker for Subscriber
```bash
git clone https://github.com/PICOM-AI/simple-ros2-test.git
cd simple-ros2-test
bash 2.1.build_subscriber.sh
```

### Perform Test (no need internet anymore):
#### On Raspberry Pi:
This will publish data to /map in 90 seconds. If it done, just run this script again.

```bash
cd simple-ros2-test
bash 1.2.run_publisher.sh
```

#### On Laptop:
This should printout stream messages at CLI.

```bash
cd simple-ros2-test
bash 2.2.run_subscriber.sh
```



## Test 2
Setup hardware as figure bellow
![Test 2](figs/2.jpg)

### Prepare (need internet)
#### On Raspberry Pi:
Build docker for Service Server
```bash
cd simple-ros2-test
bash 3.1.build_server.sh
```

#### On Laptop:
Build docker for Service Client
```bash
cd simple-ros2-test
bash 4.1.build_client.sh
```

### Perform Test (no need internet anymore):
#### On Raspberry Pi:
This will serve the server

```bash
cd simple-ros2-test
bash 3.2.run_server.sh
```

#### On Laptop:

This will send a request to server and get result.
```bash
cd simple-ros2-test
bash 4.2.run_client.sh
```

This should print out this message if it success, if nothing printout, means it fail.

`[INFO] [1762961239.313774629] [hello_client]: Result: 12`




## Test 3
Setup hardware as figure bellow
![Test 3](figs/3.jpg)

### Prepare (need internet)
#### On Raspberry Pi:
Build docker for Service Server
```bash
cd simple-ros2-test
bash 5.1.build_socket_publisher.sh
```

#### On Laptop:
Build docker for Service Client
```bash
cd simple-ros2-test
bash 6.1.build_socket_subscriber.sh
```

### Perform Test (no need internet anymore):
#### On Raspberry Pi:
This will serve the socket server

```bash
cd simple-ros2-test
bash 5.2.run_socket_publisher.sh
```

#### On Laptop:
Please open the script `6.2.run_socket_subscriber.sh` and replace `SOCKET_SERVER_HOST="127.0.0.1"` by the Raspberry Pi IP (this should be VxLAN or P4 assigned IP for the Raspberry Pi).

This will connect to the socket server get result.
```bash
cd simple-ros2-test
bash 6.2.run_socket_subscriber.sh
```

This should print out this message if it success, if nothing printout, means it fail.

`{"count": 308, "rand": "wX3zGSTx", "ts": 1762963811.2644305}`

`{"count": 309, "rand": "JSmiyOUO", "ts": 1762963812.264774}`