#!/bin/bash

uvicorn src.main:app --host "${SERVER_HOST}" --port ${SERVER_PORT}
