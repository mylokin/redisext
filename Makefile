test:
	flake8
	nosetests --with-coverage --cover-package=redisext

redis:
	docker run --name redisext -p 6379:6379 -d redis

publish:
	python setup.py sdist bdist_wheel upload

clean:
	rm -rf build dist redisext.egg-info
