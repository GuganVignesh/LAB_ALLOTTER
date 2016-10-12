init:
	virtualenv ~/dev
	. ~/dev/bin/activate && pip install -r requirements.txt
	
run :
	python SAGen.py
