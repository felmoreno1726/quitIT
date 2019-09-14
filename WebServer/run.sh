export FLASK_APP=app
export FLASK_ENV=development
thisDir=$(cd $(dirname "$0") && pwd)
#rootDir=$(cd .. && pwd)
#commonDir=$(cd ../common && pwd)
#export PYTHONPATH=$PYTHONPATH:$thisDir:$rootDir:$commonDir
#flask run --host=0.0.0.0
python3 "${thisDir}/run.py"
