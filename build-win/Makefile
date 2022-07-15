.PHONY: all


all:
	cmake -DBUILD_SHARED_LIBS:BOOL=ON ..
	make msym.dll

objects = basis_function.o character_table.o context.o debug.o elements.o equivalence_set.o geometry.o linalg.o msym.o msym_error.o permutation.o point_group.o rsh.o subspace.o symmetrize.o symmetry.o symop.o

$(objects): %.o: ../src/%.c
	gcc -Dmsym_EXPORTS -std=c99 -fPIC -fvisibility=hidden   -I . -I ../src/ -c  $< -o $@

msym.dll: $(objects)
	gcc -fPIC -Wl,-soname -shared -o msym.dll basis_function.o character_table.o context.o debug.o elements.o equivalence_set.o geometry.o linalg.o msym.o msym_error.o permutation.o point_group.o rsh.o subspace.o symmetrize.o symmetry.o symop.o   basis_function.o -lm