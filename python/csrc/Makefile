CC=gcc -v
LIBS=-lncurses
CFLAGS=-c -Wall
LDFLAGS=
SOURCES=ncurses_capp.c curses_attrib.c
OBJECTS=$(SOURCES:.curses_attrib=.o)
EXECUTABLE=curses_exec

all: $(SOURCES) $(EXECUTABLE)


build_curses: ncurses_capp.c curses_attrib.c
	${CC} -o curses_app 

	
$(EXECUTABLE): $(OBJECTS)
	${CC} -o $@ $< ${SOURCES}



