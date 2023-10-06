publish_pypi:
	cd hungry_hungry_hippos && rm -rf dist build && \
	python3 setup.py sdist bdist_wheel && \
	python3 -m twine upload dist/*

uninstall:
	pip3 uninstall hungry_hungry_hippos -y

install: uninstall
	cd hungry_hungry_hippos && rm -rf dist build
	cd hungry_hungry_hippos && python3 setup.py install --user
