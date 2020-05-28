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
            ('mioout', 'mio.*'),
            ],
        )

run(
        # Use the Print statements for debugging if necessary.
        # Otherwise, runs silently.
        # Print('pre', 'in') >>
        [
            PortFilter('bs2in') >> [
                # We send aftertouch to the Digitone, and Modwheel to the BSII.
                # It's not a perfect solution, but because the Digitone doesn't
                # route Pitchbend or Aftertouch, we have to compromise.
                Filter(NOTE|PITCHBEND|AFTERTOUCH) >> Output('dtout', 10),
                Filter(CTRL|PITCHBEND) >> Output('bs2out', 12)
                ],
            # Send messages on Channel 12 back to the BSII,
            # as well as Sync.
            PortFilter('dtin') >> [
                    ChannelFilter(12),
                    Filter(SYSRT_CLOCK),
            ] >> Output('bs2out', 12),
            PortFilter('dtin') >> Filter(SYSRT) >> Output('mioout', 1),
        ]
        # >> Print('post', 'out')
        )
