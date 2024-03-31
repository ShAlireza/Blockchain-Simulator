class BlockchainNode:
    def __init__(self, kind):
        self.kind = kind

    def connect(self, *nodes):
        pass


class Connection:
    def connect(self, node):
        pass

    def connect_nodes(self, *nodes):
        pass


class Simulator:
    def run(self):
        pass


node1 = BlockchainNode(kind="Miner")
node2 = BlockchainNode(kind="Miner")
node3 = BlockchainNode(kind="Miner")
node4 = BlockchainNode(kind="Miner")
node5 = BlockchainNode(kind="Normal")
node6 = BlockchainNode(kind="Normal")

connection = Connection()
connection.connect_nodes(node1, node2, node3, node4, node5, node6)

simulator = Simulator()
simulator.run()


