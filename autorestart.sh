#!/bin/bash

# Change this to your path.
ROUTER_PATH="/home/pi/Coding/midi-router/router.py"
ROUTER_PID=""
MIDI_DEVICES=""

restart_router() {
	kill_router
	"$ROUTER_PATH" & ROUTER_PID="$!"
	echo "MIDI router started with PID: ${ROUTER_PID}"
}

kill_router() {
	if [[ -n $ROUTER_PID ]]; then
		echo "Killing router with PID: ${ROUTER_PID}."
		kill "${ROUTER_PID}"
	fi
}

main() {
	trap kill_router EXIT
	while true; do
		NEW_MIDI_DEVICES="$(amidi --list-devices)"
		if [[ "$MIDI_DEVICES" != "$NEW_MIDI_DEVICES" ]]; then
			if [[ -n "$MIDI_DEVICES" ]]; then
				echo "MIDI devices have changed."
			fi
			restart_router
		fi
		MIDI_DEVICES="${NEW_MIDI_DEVICES}"
		sleep 1
	done
}

main
