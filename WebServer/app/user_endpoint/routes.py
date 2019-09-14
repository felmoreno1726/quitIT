import datetime
import json
from json import dumps
from flask import render_template, request, jsonify, make_response, abort
from flask_socketio import emit, send, join_room
from app import socketio, logger, session, context
from app.devices import bp

user_namespace = "/user_endpoint"

@socketio.on('alert', namespace=user_namespace)
def handle_alert_message(message):
    """
    Handles alert message comming from RaspberryPi.
    Processes the alert, logs the location to t database
    and then forwards an SMS alert to the user's phone
    """
    sid = request.sid
    user_context = session.get(sid)
    
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
socketio.on('join', namespace=user_namespace)
def on_join(data):
    """
    """
    logger.info("Joining room. Data: " + str(data))
    username = data["username"]
    phone_number = data["phone_number"]
    join_room(username)
    sid = request.sid
    session[sid] = {"username": username, "phone_number" : phone_number}
    logger.info("Session updated\n Current session: " + str(session))
