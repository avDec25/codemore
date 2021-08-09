py:
	python3 $(file) <in

pyo:
	python3 $(file)>out


cpp:
	g++ --std=c++17 -g $(file)
	./a.out <in