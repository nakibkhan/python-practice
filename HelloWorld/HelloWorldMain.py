import sys

def main(argv='Hello World'):
  if argv is None:
    argv = sys.argv

  else:
    print argv


if __name__ == "__main__":
    sys.exit(main())