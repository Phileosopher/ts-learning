https://news.ycombinator.com/item?id=26036790

[NandGame - Build a computer from scratch.](https://nandgame.com/)
[Code: The Hidden Language of Computer Hardware and Software, by Charles Petzold](https://www.charlespetzold.com/code/)
[Build a Modern Computer from First Principles: From Nand to Tetris (Project-Centered Course) | Coursera](https://www.coursera.org/learn/build-a-computer)
[Home | nand2tetris](https://www.nand2tetris.org/)
Nand2Tetris Part 1 Notes
  elements that you need the computer to do
    how are we going to specify our inxtructions?
      what instructions is it going to be following?
    how do we know what instruction to do at any point in time?
      it'll be sequential, but how do we move around in the sequence when we want to jump forward or redo things?
    what should the hardware operate on?
      where will it stick the result?
  Addressing Modes
    ALL COMPUTERS HAVE DIRECT, IMMEDIATE, AND INDIRECT ADDRESSING
    Register
      add r1, r2
      directly on 2 registers
      OPTIONAL: unlike the other 3, it's not always the same
    Direct
      Add R1, M[150]
      directly address register, but also a memory address
    Indirect
      Add R1, @A
      references something else already loaded inside the CPU
    Immediate
      Add 73, R1
      add a constant directly to the register
  Hack platform
    REGISTERS - 3 of them
      D (data) register
      A register (address) - data OR address
      M register (memory) - selected memory register
    INSTRUCTIONS
      @value:
        either non-negative constant
        OR
        a symbol referring to a constant
        basically, it refers to somewhere in memory, but can be its own value
      A instruction (address)
        [REGET IMAGE FROM VIDEO]
        3 major purposes:
          1 the only way to enter a constant into the computer with a program
          2 prepares for a C instruction about the memory at that location by moving there (otherwise the C instruction would have to be more complicated)
          3 prepares for a C instruction after that by preloading that jump to an A register
      C-instruction (computation)
        calculates and jumps
      Syntax inside the instructions
        [REGET IMAGE FROM VIDEO]
        1-3 op code
          A instruction - represented by 0, ADDRESS instruction (i.e. WHERE to go)
            writes to memory
            can be symbolized with @
          C instruction - represented by 1, COMPUTE instruction (i.e., WHAT to do)
            jump instruction
          2-3 not used
        4-10 comp - WHAT to compute (optional)
          will be sent to ALU as computing control bits
          [REGET IMAGE FROM VIDEO]
          [REGET IMAGE FROM VIDEO]
        11-13 dest - WHERE to store the computation (optional)
          [REGET IMAGE FROM VIDEO]
          M refers to RAM[A]
        14-16 jump - WHERE NEXT to go
          [REGET IMAGE FROM VIDEO]
          if comp jump 0, jump to execute the instruction in ROM[A]
        [REGET IMAGE FROM VIDEO]
  In other machine languages, A and C instructions can actually go on the same line!
  Machine language programming is lots of the same stuff as higher-level languages
    Working with registers and memory
    Branching
    Variables
    Iteration
    Pointers
    Input/Output
  I/O
    many types
      keyboard, mouse, camera, sensors, printers, screen, sound
    CPU needs a set of rules: a "protocol" to talk to them
      that's what software "drivers" are
    generally, they often use "memory mapping"
      e.g., memory location 15231 holds the last movement of the mouse
      e.g., memory location 62421 tells the printer which paper to use
      there's a screen memory map that the screen keeps pulling from EVERY frame
        
        essentially, each register put together is 16/32/64 bits that would be one looooooong string of values that goes from left to right
        e.g. first 16 bits (in 16-bit color)
        the screen memory map is a LOT of bits
          1920 wide x 1080 tall x 32-bit graphics ("true color") = 66,355,200 bits
          in a 64-bit register, that's 10, 368,000 ram registers!
      there's a keyboard memory map that captures ALL the keys we press
        a-z, A-Z, 0-9, all the special characters in normal language were codified as ASCII
        https://en.wikipedia.org/wiki/ASCII
        ASCII only needs 7 bits, so they block off 1 register just for that, since that can hold 65536 values with 
        Unicode, on the other hand, uses at least 18 bits to hold their 143859 characters
        https://en.wikipedia.org/wiki/Unicode
        It happens to be in 24576 in Hack
  
  How does Boolean logic work?
  principles
    unit testing
    obstruction
    modularity
Video: LectureUnit 4.6: Hack Programming, Part 1
Video: LectureUnit 4.7: Hack Programming, Part 2
Video: LectureUnit 4.8: Hack Programming, Part 3
Video: LectureUnit 4.9: Project 4 Overview
Video: LectureUnit 4.10: Perspectives
Programming Assignment: Project 4
MHRD - Decoder
MHRD - CPU
Reading: ReadingModule 5: Computer Architecture Roadmap
Video: LectureUnit 5.1: Von Neumann Architechture
Video: LectureUnit 5.2: The Fetch-Execute Cycle
Video: LectureUnit 5.3: Central Processing Unit
Video: LectureUnit 5.4: The Hack Computer
Video: LectureUnit 5.5: Project 5 Overview
Video: LectureUnit 5.6: Perspectives
Programming Assignment: Project 5
Reading: ReadingModule 6: Assembler Roadmap
Video: LectureUnit 6.1: Assembly Languages and Assemblers
Video: LectureUnit 6.2: The Hack Assembly Language
Video: LectureUnit 6.3: The Assembly Process - Handling Instructions
Video: LectureUnit 6.4: The Assembly Process - Handling Symbols
Video: LectureUnit 6.5: Developing a Hack Assembler
Video: LectureUnit 6.6: Project 6 Overview: Programming Option
Video: LectureUnit 6.6B: Project 6 Overview: Without Programming
Video: LectureUnit 6.7: Perspectives
Programming Assignment: Project 6








[course] [TeachYourselfCS1] nand2tetris Part 2
  https://www.coursera.org/learn/nand2tetris2
