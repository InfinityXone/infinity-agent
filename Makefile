
install:
	bash install_infinity_agent.sh

start:
	venv/bin/python gateway.py & venv/bin/python ipc_server.py &

clean:
	rm -rf __pycache__ logs/*.log

