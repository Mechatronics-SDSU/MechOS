from MechOS import mechos
import time

def talker():
    '''
    Example of publishing continuous data to topic "chatter"
    '''
    #initializes a node called talker
    talker_node = mechos.Node("talker")

    #create a tcp publisher to publish to topic chatter
    pub = talker_node.create_publisher("chatter")

    while(1):

        #publish message to chatter (must be encoded as type bytes)
        pub.publish("Hello World".encode("utf-8"))
        time.sleep(0.01)

if __name__ == "__main__":
    talker()
