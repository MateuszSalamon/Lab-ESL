import myhdl
from myhdl import delay, Signal, intbv, instance, block, StopSimulation
import os
import random

T_9600 = int(1e9 / 9600)


def rs232_tx(tx, data, duration=T_9600):

    """ Simple rs232 transmitter procedure.

    tx -- serial output data
    data -- input data byte to be transmitted
    duration -- transmit bit duration

    """

    print("-- Transmitting %s --" % hex(data))
    print("TX: start bit")
    tx.next = 0
    yield delay(duration)

    for i in range(8):
        print("TX: %s" % data[i])
        tx.next = data[i]
        yield delay(duration)

    print("TX: stop bit")
    tx.next = 1
    yield delay(duration)


def rs232_rx(rx, data, duration=T_9600, timeout=T_9600-1):

    """ Simple rs232 receiver procedure.

    rx -- serial input data
    data -- data received
    duration -- receive bit duration

    """

    # wait on start bit until timeout
    yield rx.negedge, delay(timeout)
    if rx == 1:
        raise StopSimulation

    # sample in the middle of the bit duration
    yield delay(duration // 2)
    print("RX: start bit")

    for i in range(8):
        yield delay(duration)
        print("RX: %s" % rx)
        data[i] = rx

    yield delay(duration)
    print("RX: stop bit")
    print("-- Received %s --" % hex(data))


testvals = (0xc5, 0x3a, 0x4b)


def stimulus():
    tx = Signal(1)
    for val in testvals:
        txData = intbv(val)
        yield rs232_tx(tx, txData)


def test():
    tx = Signal(1)
    rx = tx
    rxData = intbv(0)
    for val in testvals:
        txData = intbv(val)
        yield rs232_rx(rx, rxData), rs232_tx(tx, txData)


def testTimeout():
    tx = Signal(1)
    rx = Signal(1)
    rxData = intbv(0)
    for val in testvals:
        txData = intbv(val)
        yield rs232_rx(rx, rxData, timeout=4*T_9600-1), rs232_tx(tx, txData)


a = [stimulus(), test(), testTimeout()]
#
# for kur in a:
#     for kurw in kur:
#         pass

for ku in a[1]:
    for bu in ku:
        for nu in bu:
                pass
