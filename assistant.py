from twilio.rest import Client
import polling, time
import all_scores



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



# def run():
#     call = Call()
#     time.sleep(20)
#     polling.poll(
#         lambda: assess_location(call),
#         step=10,
#         poll_forever=True
#     )

# def run_real(data):
#     call = Call()
#     smart_car = new Vehicle(vehicleIds[0], auth.getAccessToken())
#     vin = smar_car.vin()

#     time.sleep(20)
#     polling.poll(
#         lambda: access_location_real(call, data, smart_car),
#         step=10,
#         poll_forever=True
#     )

# def assess_location(call,data,vehicle):
#     # run smartcar API call
#     # check if at dest, if yes return True
#     # pass location to scoring block
#     #
#     SmartcarResponse<VehicleLocation> locationResponse = vehicle.location();
#     VehicleLocation locationData = locationResponse.getData();
#     curr_loc = [locationData.getLatitude(),locationData.getLongitude()]

#     if len(data) == 0:
#         call.end()
#         return

#     curr_data_pt=data.pop(0)

def run_demo(data, grid):
    data = [d[:2] for d in data]
    call = Call()
    time.sleep(20)
    polling.poll(
        lambda: assess_location_demo(call, data, grid),
        step=10,
        poll_forever=True
    )

def assess_location_demo(call, data, grid):
    if len(data) == 0:
        call.end()
        return
    curr_pt = data.pop(0)
    for _ in range(min(20, len(data)):
        data.pop(0)
    # TODO send data through websocket to frontend
    score = grid.get_score(curr_pt, 0.007)
    if score < 0.5:
        call.update_good()
    elif score < 0.65:
        pass
    else:
        call.update_bad()
