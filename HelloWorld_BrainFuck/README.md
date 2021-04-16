# HelloWorld_BrainFuck

I have come across a new interpreter called brainfuck and developed a hello world program in it. 

# Instructions

Getting the source
Download the source code by running the following code in your command prompt:

$ git clone https://github.com/fabianishere/brainfuck.git

or simply grab a copy of the source code as a Zip file.

Building
Create the build directory.

$ mkdir build

$ cd build

Brainfuck requires CMake and a C compiler (e.g. Clang or GCC) in order to run. It also depends on libedit, which is available in the main repositories of most Linux distributions (e.g. as libedit-dev on Debian/Ubuntu) and comes with the macOS XCode command line tools. Then, simply create the Makefiles:

$ cmake ..

and finally, build it using the building system you chose (e.g. Make):

$ make

After the build has been finished, you may install the binaries to your local system (see CMAKE_INSTALL_PREFIX for information about the install prefix):

$ make install

Alternatively, you may run the interpreter directly without installation, for instance:

$ ./brainfuck ../examples/hello.bf
