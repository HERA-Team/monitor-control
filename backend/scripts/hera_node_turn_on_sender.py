import udpSender
import time
import argparse

parser = argparse.ArgumentParser(description = 'Turn on SNAP relay, SNAPs, FEM and PAM via flags',
			formatter_class = argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('ip_addr', action = 'store', 
			help = 'Specify the Arduino IP address to send commands to')

parser.add_argument('-r', dest = 'snapRelay', action = 'store_true', default = False,
			help = 'Use this flag to turn on the snapRelay')
parser.add_argument('-s', dest = 'snaps', action = 'store_true', default = False,
			help = 'Use this flag to turn on all the snaps')
parser.add_argument('-s0', dest = 'snap01', action = 'store_true', default = False,
			help = 'Use this flag to turn on SNAP 0')
parser.add_argument('-s1', dest = 'snap23', action = 'store_true', default = False,
			help = 'Use this flag to turn on SNAP 1')
parser.add_argument('-s2', dest = 'snap01', action = 'store_true', default = False,
			help = 'Use this flag to turn on SNAP 2')
parser.add_argument('-s3', dest = 'snap23', action = 'store_true', default = False,
			help = 'Use this flag to turn on SNAP 3')
parser.add_argument('-p', dest = 'pam', action = 'store_true', default = False,
			help = 'Use this flag to turn on the PAM')
parser.add_argument('-f', dest = 'fem', action = 'store_true', default = False,
			help = 'Use this flag to turn on the FEM')
parser.add_argument('--reset', dest = 'reset', action = 'store_true', default = False,
			help = 'Use this flag to reset Arduino (turn everything off abruptly')
args = parser.parse_args()

# Instantiate a udpSenderClass object to send commands to Arduino
s = udpSender.UdpSender(args.ip_addr)

if args.snaps:
    print("Turning SNAP relay on")
    s.power_snap_relay('on')
    time.sleep(.1)
    print("Turning SNAP 0 on")
    s.power_snap_0('on')
    time.sleep(1)
    print("Turning SNAP 1 on")
    s.power_snap_1('on')
    time.sleep(1)
    print("Turning SNAP 2 on")
    s.power_snap_2('on')
    time.sleep(1)
    print("Turning SNAP 3 on")
    s.power_snap_3('on')
    time.sleep(1)

if args.snapRelay:
    print("Turning SNAP relay on")
    s.power_snap_relay('on')
    time.sleep(.1)

if args.snap0:
    print("Turning relay and SNAP 0 on")
    s.power_snap_relay('on')
    s.power_snap_0('on')
    time.sleep(1)

if args.snap1:
    print("Turning relay and SNAP 1 on")
    s.power_snap_relay('on')
    s.power_snap_1('on')
    time.sleep(1)

if args.snap2:
    print("Turning relay and SNAP 2 on")
    s.power_snap_relay('on')
    s.power_snap_2('on')
    time.sleep(1)

if args.snap3:
    print("Turning relay and SNAP 3 on")
    s.power_snap_relay('on')
    s.power_snap_3('on')
    time.sleep(1)

if args.pam:
    print("Turning PAM on")
    s.power_pam('on')
    time.sleep(1)

if args.fem:
    print("Turning FEM on")
    s.power_fem('on')
    time.sleep(1)

if args.reset:
    print("Resetting Arduino/Turning everything off at once")
    s.reset()

