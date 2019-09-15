#!/bin/bash

curl -X POST -u "apikey:Pe07noGok6IHZ6wPEyG0Dyrc4Gx0-0UJ_kPmU7o1Vu06" -F "images_file=@test.jpeg" -F "threshold=0.5" -F "classifier_ids=SmokingClassification_1954917514" "https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?version=2018-03-19" > out.txt