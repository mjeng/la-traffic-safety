import uuid from 'uuid/v1'

export class Socket {
    static ws = null;

    static initialize(onmsghandler) {
        const url = window.location.hostname;
        Socket.ws = new WebSocket('wss://' + url + '/subscribe-ws');
        Socket.ws.onerror = (e) => {
            console.log("Websocket error observed:", e);
        };
        Socket.ws.onopen = (e) => {
            console.log(`Websocket opened from server to ${url}.`);
        };
        Socket.ws.onmessage = (e) => {
            const msg = JSON.parse(e.data);
            console.log("Socket.ws.onmessage triggered");
            console.log("Lat:", msg.lat, "Long:", msg.long);
            setTimeout(() => {
                onmsghandler(msg.lat, msg.long);
            }, 50)
        };
        Socket.ws.onclose = (e) => {
            console.log("Original websocket closed:", e, "\nCreating new one...");
            setTimeout(Socket.initialize, 50);
        };
    }
}