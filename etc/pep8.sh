find ../snussum/ -name '*.py' -exec autopep8 --in-place --verbose --aggressive --aggressive --ignore-local-config --max-line-length 120 '{}' \;
pep8
