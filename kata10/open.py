def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError:
        print('File not found in the indicate path!')

if __name__ == '__main__':
    main()