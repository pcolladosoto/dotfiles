#include <stdio.h>

int main(int argc, char** argv) {
	if (argc != 2) {
		printf("Usage: flip <path/to/file>\n");
		return -1;
	}
	FILE* f = NULL;
	if (*(*(argv + 1)) == '-')
		f = stdin;
	else
		if (!(f = fopen(argv[1], "rb"))) {
			printf("File not found...\n");
                        return -1;
		}

	while(!feof(f))
		printf("%c", (char) ~fgetc(f));
	if (f != stdin)
		fclose(f);
	return 0;
}
