from api_utils import clean_data, extract_next_to_jump
import sys

def main():
    # read std in
    filename = sys.argv[1]

    df = clean_data(filename)

    print(extract_next_to_jump(df))
    return extract_next_to_jump(df)

if __name__ == "__main__":
    main()