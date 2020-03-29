#!/usr/bin/env python2
from mididings import *


config(
        start_delay = 0.5,
        in_ports = [
            ('bs2in', 'Bass Station II.*'),
            ('dtin', 'Elektron Digitone.*'),
            ],
        out_ports = [
            ('bs2out', 'Bass Station II.*'),
            ('dtout', 'Elektron Digitone.*'),
            ],
        )

run(
        # Use the Print statements for debugging if necessary.
        # Otherwise, runs silently.
        # Print('pre', 'in') >>
        [
            PortFilter('bs2in') >> [
                Filter(NOTE) >> Output('dtout', 10),
                Filter(CTRL|PITCHBEND|AFTERTOUCH) >> Output('bs2out', 12)
                ],
            PortFilter('dtin') >> ChannelFilter(12) >> Output('bs2out', 12),
            ]
        # >> Print('post', 'out')
        )
