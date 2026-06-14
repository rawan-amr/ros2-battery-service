import rclpy
from rclpy.node import Node

from battery_interfaces.srv import BatteryLevel
from std_msgs.msg import Int64


class BatteryServer(Node):

    def __init__(self):
        super().__init__("battery_server")

        self.current_battery = 0

        self.subscription = self.create_subscription(
            Int64,
            "battery_status",
            self.battery_callback,
            10
        )

        self.srv = self.create_service(
            BatteryLevel,
            "battery_level",
            self.battery_level_callback
        )

    def battery_callback(self, msg):
        self.current_battery = msg.data

        self.get_logger().info(
            f'Battery updated: {self.current_battery}%'
        )
    
    def battery_level_callback(self, request, response):
        
        response.battery_level = self.current_battery

        self.get_logger().info(
            f'Battery level requested: {response.battery_level}%'
            )
        
        return response
    

def main(args=None):

    rclpy.init(args=args)

    node = BatteryServer()
    
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()