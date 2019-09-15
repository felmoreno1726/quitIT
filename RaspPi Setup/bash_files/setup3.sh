#!/bin/bash

curl 'https://api.twilio.com/2010-04-01/Accounts/ACa237ebc4a15e725e79b64e4d65e38654/Messages.json' -X POST \
--data-urlencode 'To=+14704487334' \
--data-urlencode 'From=+12053410326' \
--data-urlencode 'Body=quitIT!: Please have a nicotine lozenge, or gum. See app for more information! ' \
-u ACa237ebc4a15e725e79b64e4d65e38654:401dc81558a49f4548ae47bf9d43e56a