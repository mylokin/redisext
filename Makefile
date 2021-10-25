test:
	flake8 redisext tests docs
	nosetests --with-coverage --cover-package=redisext

redis:
	docker run --name redisext -p 6379:6379 -d redis

publish: test
	python setup.py sdist bdist_wheel upload

clean:
	rm -rf build dist redisext.egg-info

docs:
	rm -rf docs/_build/*
	python setup.py build_sphinx
	python setup.py upload_sphinx

.PHONY: test redis publish clean docs
