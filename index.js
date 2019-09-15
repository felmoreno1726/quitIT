'use strict'
const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);
exports.sendAlert = functions.database.ref('/trigger')
   			 .onUpdate((event,context) => {
    const alert_path = admin.database().ref('/Update/');
    console.log("value");
    return admin.database().ref('/trigger/trigger').once('value').then(function(datasnapshot){
            console.log("value",datasnapshot.val());
              if (datasnapshot.val() == false){
                 alert_path.once('value').then(function(snapshot) {
                        var newAlertRef = alert_path.push();  
                        console.log("push", newAlertRef);
                        newAlertRef.set({"longitude":"180", "latitude":"120"});        	
                 });
             }
            admin.database().ref('/trigger/trigger').set(false)    
     }); 
}); 