test:
	flake8
	nosetests --with-coverage --cover-package=redisext

redis:
	docker run --name redisext -p 6379:6379 -d redis

vm:
	ansible-galaxy install angstwad.docker_ubuntu
	vagrant up
	export DOCKER_HOST="tcp://`vagrant ssh-config | sed -n "s/[ ]*HostName[ ]*//gp"`:2375"
