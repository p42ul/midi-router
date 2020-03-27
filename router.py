from mididings import *

config(
        in_ports = [
            ('bs2in', '24:0'),
            ('dtin', '20:0'),
            ],
        out_ports = [
            ('dtout', '20:0'),
            ('bs2out', '24:0'),
            ],
)

run(
    Print() >> [
        ChannelFilter(10) >> Filter(NOTE) >> Output('dtout', 10),
        ChannelFilter(10) >> Filter(CTRL|PITCHBEND|AFTERTOUCH) >> Output('bs2out', 10),
        ChannelFilter(9) >> Output('bs2out', 10)
        ]
)

