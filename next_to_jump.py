from api_utils import extract_next_to_jump
import sys

def main():
    # read std in
    filename = sys.argv[1]
    
    output = extract_next_to_jump(filename)
    print(output)

if __name__ == "__main__":
    main()