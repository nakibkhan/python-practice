import sys

def main(argv=None):
  if argv is None:
    argv = sys.argv
    print argv


if __name__ == "__main__":
    sys.exit(main())