from twilio.rest import Client
import polling, time

CURR = None
INTRO = "https://handler.twilio.com/twiml/EHab9c307ffe2116b32a69ff4fa9447522"
ALLGOOD = "https://handler.twilio.com/twiml/EHa16958d8d15597313ec30061f6b2421d"
WARN = "https://handler.twilio.com/twiml/EH4b40e44feb9cfe09d886d5212d27fb45"
HANGUP = "https://handler.twilio.com/twiml/EHc91eed7f8e8ba9a05b802fbd6cee5cab"

account_sid = 'AC91e95fc48cb37932aa55ca99d58f40d9'
auth_token = '368d12d3f3e75f039a206d11e0387c64'
client = Client(account_sid, auth_token)

class Call:
    GOOD = "good"
    BAD = "bad"
    def __init__(self):
        self.call = client.calls.create(
                                url=INTRO,
                                to='+19739085890',
                                from_='+12018176781'
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


import random
def assess_location(call):
    # run smartcar API call
    # check if at dest, if yes return True
    # pass location to scoring block
    #
    n = random.randint(1, 11)
    print("Running poll with num", n)
    if n <= 5:
        call.update_good()
    elif n <= 10:
        call.update_bad()
    else:
        call.end()
        return True
    return False

def run():
    call = Call()
    time.sleep(20)
    polling.poll(
        lambda: assess_location(call),
        step=10,
        poll_forever=True
    )
