#!/bin/bash

docker-compose -f docker-compose-dev.yml run users-service python manage.py test
