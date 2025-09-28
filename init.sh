#!/bin/bash
source venv/bin/activate
nohup venv/bin/python gateway.py > logs/gateway.log 2>&1 &
nohup venv/bin/python ipc_server.py > logs/ipc.log 2>&1 &
