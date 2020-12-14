#! /usr/bin/env python3 

from cellulariot import cellulariot
import time

import logging

log = logging.getLogger("bg96")
#library use
#logging.getLogger('foo').addHandler(logging.NullHandler())


def cmd_on(node, **kwargs):
    node.enable()
    time.sleep(1)
    node.powerUp()
    time.sleep(1)
    node.sendATComm("ATE1","OK\r\n")


def cmd_unlock(node, **kwargs):
    pin = kwargs['pin']
    node.sendATComm("AT+CPIN={0}".format(pin), "OK\r\n")


def cmd_off(node, **kwargs):
    node.setupGPIO()
    node.disable()
    time.sleep(1)


def cmd_device_info(node, **kwargs):
    node.getIMEI()
    time.sleep(0.5)
    node.getFirmwareInfo()
    time.sleep(0.5)
    node.getHardwareInfo()
    time.sleep(0.5)
    node.getICCID()
    time.sleep(0.5)


def cmd_connect(node, **kwargs):
    node.setGSMBand(node.GSM_900)
    time.sleep(0.5)
    node.setCATM1Band(node.LTE_B5)
    time.sleep(0.5)
    node.setNBIoTBand(node.LTE_B20)
    time.sleep(0.5)
    node.getBandConfiguration()
    time.sleep(0.5)  
    node.setMode(node.GSM_MODE)
    time.sleep(0.5)

    node.getOperator()
    time.sleep(0.5)
    node.connectToOperator()
    time.sleep(0.5)
    node.getSignalQuality()
    time.sleep(0.5)
    node.getQueryNetworkInfo()
    time.sleep(0.5)


def main(commands, serial_port=None, **kwargs):

    commands = {
        'on' :      cmd_on,
        'unlock':   cmd_unlock,
        'off':      cmd_off,
        'info':     cmd_device_info,
        'connect':  cmd_connect,
    }

    log.info("Commands to run: {0}".format(' '.join(args.commands)))

    if serial_port == None:
        raise Exception("serial_port not set")

    # Verify commands
    for cmd in args.commands:
        if cmd not in commands.keys(): raise Exception("Command not found {0}".format(cmd))

    # Setup node object
    node = cellulariot.CellularIoT(serial_port=serial_port)
    node.setupGPIO()

    # Call commands
    for cmd in args.commands:
        cmd_def = commands[cmd]
        log.info('Calling command \'{0}\''.format(cmd))
        cmd_def(node, **kwargs)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Quectel BG-96')
    parser.add_argument('commands', nargs='+')
    parser.add_argument('--serial_port', '-s', dest='serial_port', metavar='/dev/ttyS0', default='/dev/ttyUSB2', help='Serial port')
    parser.add_argument('--pin', '-p', dest='pin', metavar='N', default=None, help='PIN code')
    #parser.add_argument('--bar', '-b', dest='bar', metavar='bar', help='bar')
    #parser.add_argument('-d', dest='debug', action='store_true', help='debug log')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--log', '-l', dest='loglevel', choices=['DEBUG', 'INFO', 'ERROR'], 
                       default='INFO', help='log level')
    group.add_argument('-d', '--debug', dest='debug', action='store_true')
    
    args = parser.parse_args()
    if args.debug:
        args.loglevel = 'DEBUG'
    loglevel = getattr(logging, args.loglevel)
    log.setLevel(loglevel)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG) #effective loglevel
    handler.setFormatter(logging.Formatter("%(message)s")) #"%(levelname)s: %(name)s" or "%(pathname)s:%(lineno)d/%(levelname)s %(message)s"
    log.addHandler(handler)

    #handler0 = logging.StreamHandler()
    #handler0.setLevel(logging.INFO) #effective loglevel
    #handler0.setFormatter(logging.Formatter("FOO %(levelname)s: %(message)s"))
    #log.addHandler(handler0)

    main(args.commands, serial_port=args.serial_port, **{'pin': args.pin})

    logging.shutdown()
