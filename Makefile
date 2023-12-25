setup: infra/bin/activate

infra/bin/activate: requirements.txt
	python3 -m virtualenv infra
	infra/bin/pip3 install -r requirements.txt
	touch infra/bin/activate
	@echo ""
	@echo "--------------------------------------------------------------------------"
	@echo "Setup Successful !!!"
	@echo "--------------------------------------------------------------------------"

verify:
	infra/bin/autopep8 -vvvvv --in-place --recursive supmkt/*
	infra/bin/flake8 supmkt/

clean:
	rm -rf infra __pycache__