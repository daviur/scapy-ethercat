# The MIT License (MIT)
#
# Copyright (c) 2016 David I Urbina
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from scapy import all as scapy_all


class ETHERCAT(scapy_all.Packet):
    name = "EtherCAT"
    fields_desc = [
        scapy_all.LEShortField('header', 0),
        scapy_all.ByteField('command', 0),
        scapy_all.ByteField('index', 0),
        scapy_all.LEIntField('log-address', 0),
        scapy_all.LEShortField('length', 0),
        scapy_all.LEShortField('interrupt', 0),
        scapy_all.LEIntField('join1', 0),
        scapy_all.LEShortField('mode1', 0),
        scapy_all.StrFixedLenField('padding1', 0, length=34),
        scapy_all.LEIntField('join2', 0),
        scapy_all.LEShortField('mode2', 0),
        scapy_all.StrFixedLenField('padding2', 0, length=34),
        scapy_all.LEIntField('join3', 0),
        scapy_all.LEShortField('mode3', 0),
        scapy_all.StrFixedLenField('padding3', 0, length=34),
        scapy_all.LEIntField('join4', 0),
        scapy_all.LEShortField('mode4', 0),
        scapy_all.StrFixedLenField('padding4', 0, length=34),
        scapy_all.LEIntField('join5', 0),
        scapy_all.LEShortField('mode5', 0),
        scapy_all.StrFixedLenField('padding5', 0, length=234),
        scapy_all.LEShortField('working-counter', 0)
    ]

scapy_all.bind_layers(scapy_all.Ether, ETHERCAT, type=0x88a4)