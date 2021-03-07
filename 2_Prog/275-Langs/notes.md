[general format]
  what it is, its history
  what it's really good at
  downsides of each of the languages
Look into computer language profilers
https://en.wikipedia.org/wiki/Programming_language_generations
https://en.wikipedia.org/wiki/List_of_programming_languages_by_type
Quick Reference - Tech Stacks
  Lay out the most common tech stacks (LAMP, e.g.)
JS
  Atwood's law: Any software that can be written in JavaScript will eventually be written in JavaScript.
Lisp
  PaulGraham - Lisp
    Lisp code is made out of Lisp data objects.  And not in the trivial sense that the source files contain characters, and strings are one of the data types supported by the language. Lisp code, after it’s read by the parser, is made of data structures that you can traverse.
    If you understand how compilers work, what’s really going on is not so much that Lisp has a strange syntax as that Lisp has no syntax.  You write programs in the parse trees that get generated within the compiler when other languages are parsed.
    But these parse trees are fully accessible to your programs. You can write programs that manipulate them. In Lisp, these programs are called macros. They are programs that write programs.
    Paul Graham wrote *Ansi Common Lisp*
    So the short explanation of why this 1950s language is not obsolete is that it was not technology but math, and math doesn’t get stale. The right thing to compare Lisp to is not 1950s hardware but the Quicksort algorithm, which was discovered in 1960 and is still the fastest general-purpose sort.
    The 9 Ideas of Lisp:
      1. Conditionals. A conditional is an if-then-else construct. We take these for granted now, but Fortran I didn’t have them. It had only a conditional goto closely based on the underlying machine instruction.
      2. A function type.  In Lisp, functions are a data type just like integers or strings. They have a literal representation, can be stored in variables, can be passed as arguments, and so on.
      3. Recursion. Lisp was the first high-level language to support recursive functions.
      4. Dynamic typing. In Lisp, all variables are effectively pointers. Values are what have types, not variables, and assigning values to variables means copying pointers, not what they point to.
      5. Garbage-collection.
      6. Programs composed of expressions. Lisp programs are trees of expressions, each of which returns a value. This is in contrast to Fortran and most succeeding languages, which distinguish between expressions and statements. This distinction was natural in Fortran I because you could not nest statements. So while you needed expressions for math to work, there was no point in making anything else return a value, because there could not be anything waiting for it. This limitation went away with the arrival of block-structured languages, but by then it was too late. The distinction between expressions and statements was entrenched.  It spread from Fortran into Algol and then to both their descendants.
      7. A symbol type. Symbols are effectively pointers to strings stored in a hash table. So you can test equality by comparing a pointer, instead of comparing each character.
      8. A notation for code using trees of symbols and constants.
      9. The whole language there all the time. There is no real distinction between read-time, compile-time, and runtime. You can compile or run code while reading, read or run code while compiling, and read or compile code at runtime. Running code at read-time lets users reprogram Lisp’s syntax; running code at compile-time is the basis of macros; compiling at runtime is the basis of Lisp’s use as an extension language in programs like Emacs; and reading at runtime enables programs to communicate using s-expressions, an idea recently reinvented as XML.5
      If you define [another] language that has car, cdr, cons, quote, cond, atom, eq, and a notation for functions expressed as lists, then you can build all the rest of Lisp out of it.
Perl
  [CERT] CIW Perl Specialist - $150
PHP
  How to setup a Drupal site??
  WP Content Copy Protection & No Right Click - reproduce in PHP without a plugin
  Zend PHP certification - $195
Python
  It's very powerful
  But...it doesn't scale well
    the code ends up getting heavily typed
    dcolkitt:
    I think in general Python's biggest challenge is that it doesn't scale well. This is an agglomeration of issues around the same theme: bad packaging when there's a lot of cross-cutting dependencies, slow performance, no concurrency, typing as second-class citizens, etc. All of that is barely noticeable when you're just getting started on a small experimental project, but incredibly painful in large production systems.
    I strongly suspect that devs' satisfaction with Python is strongly correlated with the size of the codebase they're working on. Generally people using Python for one-off projects or self-contained tools tend to be pretty happy. People stuck in sprawling enterprise codebases, with O(million) lines of code to wrangle, seem almost universally miserable with the language.
    What I've observed a lot is that many startups or greenfield projects start with Python to get an MVP out the door as fast as possible. Then as the scope of the software expands they feel increasingly bogged down and trapped in the language. 
  Zenva key
    f-21-giveu2-69lxq0w60n
