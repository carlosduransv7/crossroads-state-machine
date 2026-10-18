from enum import Enum

class State(Enum):
    THRESHOLD = "threshold"
    AGREEMENT = "agreement"
    BREACH = "breach"
    STORM = "storm"
    SILENCE = "silence"

def transition(state, breaks_promise=False):
    if state == State.THRESHOLD:
        return State.AGREEMENT
    if state == State.AGREEMENT and breaks_promise:
        return State.BREACH
    if state == State.BREACH:
        return State.STORM
    if state == State.STORM:
        return State.SILENCE
    return state

if __name__ == "__main__":
    s = State.THRESHOLD
    print("Crossroads protocol: fictional simulation")
    for broken in (False, True, False, False):
        s = transition(s, broken)
        print("state:", s.value)
