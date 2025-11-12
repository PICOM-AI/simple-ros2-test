from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node

class HelloService(Node):
    def __init__(self):
        super().__init__("hello_service")
        self.srv = self.create_service(AddTwoInts, "add_two_ints", self.callback)

    def callback(self, request, response):
        self.get_logger().info(f"Request: {request.a}, {request.b}")
        response.sum = request.a + request.b
        return response

def main():
    rclpy.init()
    node = HelloService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
