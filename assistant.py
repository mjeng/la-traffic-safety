from twilio.rest import Client
import polling, time, os

INTRO = os.environ.get("TWIML_INTRO")
ALLGOOD = os.environ.get("TWIML_ALLGOOD")
WARN = os.environ.get("TWIML_WARN")
HANGUP = os.environ.get("TWIML_HANGUP")

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH")
client = Client(account_sid, auth_token)

class Call:
    GOOD = "good"
    BAD = "bad"
    def __init__(self):
        print(list(os.environ.items()))
        self.call = client.calls.create(
                                url=INTRO,
                                to=os.environ.get("TWILIO_TO"),
                                from_=os.environ.get("TWILIO_FROM")
                            )
        self.last_state = Call.GOOD

    def update_good(self):
        assert self.call != None
        if self.last_state == Call.GOOD:
            return
        assert self.last_state == Call.BAD
        client.calls(self.call.sid).update(method='POST', url=ALLGOOD)
        self.last_state = Call.GOOD
        return

    def update_bad(self):
        assert self.call != None
        if self.last_state == Call.BAD:
            return
        assert self.last_state == Call.GOOD
        client.calls(self.call.sid).update(method='POST', url=WARN)
        self.last_state = Call.BAD
        return

    def end(self):
        assert self.call != None

        client.calls(self.call.sid).update(method='POST', url=HANGUP)
        return


    
def run():
    call = Call()
    time.sleep(20)
    polling.poll(
        lambda: assess_location(call),
        step=10,
        poll_forever=True
    )
    
def assess_location(call):
    # run smartcar API call
    # check if at dest, if yes return True
    # pass location to scoring block
    #
    return

def run_demo(data):
    data = [d[:2] for d in data]
    call = Call()
    time.sleep(20)
    polling.poll(
        lambda: assess_location_demo(call, data),
        step=10,
        poll_forever=True
    )

def assess_location_demo(call, data):
    if len(data) == 0:
        call.end()
        return
    curr_pt = data.pop(0)
    for _ in range(min(20, len(data))):
        data.pop(0)
    # send data through websocket to frontend
    # get score
    score = None
    if score < 0.5:
        call.update_good()
    elif score < 0.75:
        pass
    else:
        call.update_bad()