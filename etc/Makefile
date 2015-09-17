vm:
	@vagrant up
	@echo "Run: export DOCKER_HOST=\"tcp://`vagrant ssh-config | sed -n "s/[ ]*HostName[ ]*//gp"`:2375\""

py3:
	python3 -m venv venv
