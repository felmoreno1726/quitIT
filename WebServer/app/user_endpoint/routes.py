import datetime
import json
from json import dumps

from flask import render_template, request, jsonify, make_response, abort
from flask_socketio import emit, send, join_room
from app import socketio, logger, sessions, sids, db, user_endpoint
from app.user_endpoint import bp

from app.models import Alert, User

user_namespace = "/user_endpoint"

@socketio.on('alert', namespace=user_namespace)
def handle_alert_message(message):
    """
    Handles alert message comming from RaspberryPi.
    Processes the alert, logs the location to t database
    and then forwards an SMS alert to the user's phone
    """
    # get the time and create Alert Entry
    time = datetime.utcnow()

    sid = request.sid
    user_context = sessions.get(sid)
    alert = Alert(time=time, coordinates=user_context["location"])
    db.session.add(alert)
    db.session.commit()

@socketio.on('doctor_help', namespace=user_namespace)
def handle_doctor_help(message):
    """
    Handles a request from the MobileApp to get the user professional help
    """


@socketio.on('current_location', namespace=user_namespace)
def handle_update_location(message):
    """
    Handles a MobileApp request to update geographical location
    Checks if the location matches that of a red zone, if yes
    then sends an SMS alert to the user's phone.
    """
    sid = request.sid
    username = sids[sid]
    coordinates = message["coordinates"] # (x, y)
    sessions[username]['coordinates'] = coordinates
    #only one user
    user = User.query.get_or_404(1)
    user.coordinates = coordinates
    db.commit()
socketio.on('join', namespace=user_namespace)


def on_join(data):
    """
    """
    logger.info("Joining room. Data: " + str(data))
    username = data["username"]
    phone_number = data.get("phone_number")
    # update session with loggin parameters
    if username in sessions:
        # then update with phone number if present
        if phone_number is not None:
            sessions[username]["phone_number"] = phone_number
            user = User.query.get_or_404(1)
            user.phone_number = phone_number
    else:
        # create entry for user
        user = User(username=username)
        if phone_number is not None:
            sessions[username] = {"phone_number": phone_number}
            user.phone_number = phone_number
        db.session.add(user)
    join_room(username)
    # update sids to point to the username
    sid = request.sid
    sids[sid] = username
    logger.info("Device joined\n sids: " + str(sids))
    logger.info("sessions: " + str(sessions))
    db.session.commit()
