from MechOS import mechos
import time

def chatter_callback(chatter_data):
    '''
    Callback function for subscriber to pass data into.

    Parameters:
        chatter_data: The data recieved over topic chatter from publisher. Each
        time a spinOnce is called, the data being sent from the publisher is
        inserted here.
    '''
    print(chatter_data.decode())


def listener():
    '''
    Example of a subsriber subscribing to topic "chatter"
    '''
    #initializes a node called listener
    listener_node = mechos.Node("listener")

    #create a subscriber to subscribe to topic chatter
    sub = listener_node.create_subscriber("chatter", chatter_callback)

    while(1):

        listener_node.spin_once()
        time.sleep(0.01)


if __name__ == "__main__":
    listener()
