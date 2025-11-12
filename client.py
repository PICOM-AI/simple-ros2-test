import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class HelloClient(Node):
    def __init__(self):
        super().__init__("hello_client")
        self.cli = self.create_client(AddTwoInts, "add_two_ints")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting...")

    def send_request(self, a, b):
        req = AddTwoInts.Request()
        req.a = a
        req.b = b
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main():
    rclpy.init()
    client = HelloClient()
    response = client.send_request(5, 7)
    client.get_logger().info(f"Result: {response.sum}")
    client.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
