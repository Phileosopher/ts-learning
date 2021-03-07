import sys

def main():
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
  print 'Hello', name

# Standard boilerplate to invoke the main() function
if __name__ == '__main__':
  main()

