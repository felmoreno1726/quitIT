import datetime
import json
from json import dumps
from flask import render_template, request, jsonify, make_response, abort
from flask_socketio import emit, send, join_room
from app import socketio, logger, session, context
from app.devices import bp

user_namespace = "/user_endpoint/channel"

@socketio.on('alert', namespace=user_namespace)
def handle_alert_message(message):
    """
    Handles alert message.
    Processes the alert, logs the location to the database
    and then forwards an alert message to the user's MobileApp
    """
    sid = request.sid
    
    
