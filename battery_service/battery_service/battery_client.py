import rclpy
from rclpy.node import Node

from battery_interfaces.srv import BatteryLevel


class BatteryClient(Node):

    def __init__(self):
        super().__init__("battery_client")

        self.client = self.create_client(
            BatteryLevel,
            "battery_level"
        )

        while not self.client.wait_for_service(timeout_sec = 1.0):
            self.get_logger().info(
                "Waiting for battery service..."
            )
        
        self.request = BatteryLevel.Request()

    def send_request(self):

        future = self.client.call_async(
            self.request
        )

        rclpy.spin_until_future_complete(
            self,
            future
        )

        return future.result()
    

def main(args=None):

    rclpy.init(args=args)

    node = BatteryClient()

    response = node.send_request()

    node.get_logger().info(
        f"Current Battery Level: {response.battery_level}%"
    )

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()