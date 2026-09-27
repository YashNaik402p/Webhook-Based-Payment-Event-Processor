
from flask import Flask,request
from database import init_db,update_payment_status
from logger import log_event
app=Flask(__name__)
init_db()
@app.route("/webhook", methods=["POST"])
def webhook():
    data=request.json
    print("Received webhook:",data)

    event=data.get("event")
    user_id=data.get("user_id")

    if not event or not user_id:
        return {"status":"error","message":"Missing user_id or event"},400
    if event not in ["payment_success", "payment_failed"]:
        return {"status": "error", "message": "Unknown event"}, 400
    
    print(f"Event: {event} | User ID: {user_id}")
    update_payment_status(user_id,event)
    log_event(user_id,event)


    return {"status": "received","event": event,"user_id":user_id}, 200

if __name__ == "__main__":
    app.run(port=5000)
    
