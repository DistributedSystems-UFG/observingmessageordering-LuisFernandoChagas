#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.78.41','172.31.65.227','172.31.74.212','172.31.75.17','172.31.72.48','172.31.75.162']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
PEERS_SAME_REGION = ['100.26.114.192','34.203.85.178','34.230.137.115','44.215.75.173','54.146.146.220','3.238.97.251']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['100.26.114.192','34.203.85.178','34.230.137.115','44.215.75.173','172.31.39.6','172.31.41.233']


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 6   # Number of peers
SERVER_ADDR ='100.26.114.192'
SERVER_PORT = 5678

