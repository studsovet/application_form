set -a
source ./.env
set +a

python3 manage.py runserver
