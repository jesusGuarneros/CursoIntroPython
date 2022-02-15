def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError:
        print('error path.')
        
if __name__ == '__main__':
    main()