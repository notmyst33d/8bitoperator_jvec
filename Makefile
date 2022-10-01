all: build

build: build.stamp

venv: venv/touchfile

build.stamp: venv
	mkdir -p fonts
	. venv/bin/activate; fontmake -g sources/8bitoperator_jvec.glyphs
	cp master_ttf/8bitoperatorJVEC-Regular.ttf fonts/8bitoperator_jvec.ttf
	cp master_otf/8bitoperatorJVEC-Regular.otf fonts/8bitoperator_jvec.otf
	. venv/bin/activate; woff2_compress fonts/8bitoperator_jvec.ttf
	rm -rf master_otf master_ttf master_ufo
	touch build.stamp

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

clean:
	rm -rf venv fonts build.stamp

