import mechos
import time

def chatter_callback(chatter_data):
    '''
    Callback function for subscriber to pass data into.

    Parameters:
        chatter_data: The data recieved over topic chatter from publisher. Each
        time a spinOnce is called, the data being sent from the publisher is
        inserted here.
    '''
    print(chatter_data)


def listener():
    '''
    Example of a subsriber subscribing to topic "chatter"
    '''
    #initializes a node called listener
    count = 0
    listener_node = mechos.Node("listener")

    #create a subscriber to subscribe to topic chatter
    sub = listener_node.create_subscriber("chatter", chatter_callback)
    start = time.time()
    try:
        while(1):
            #receive available message for subsriber sub
            listener_node.spinOnce(sub)
            count = count + 1
            #time.sleep(0.5)
    except:
        end = time.time()
        print(count/(end - start))

if __name__ == "__main__":
    listener()
