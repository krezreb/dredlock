publish_pypi:
	cd dredlock && rm -rf dist build && \
	python3 setup.py sdist bdist_wheel && \
	python3 -m twine upload dist/*

uninstall:
	pip3 uninstall dredlock -y

install: uninstall
	cd dredlock && rm -rf dist build
	cd dredlock && python3 setup.py install --user
