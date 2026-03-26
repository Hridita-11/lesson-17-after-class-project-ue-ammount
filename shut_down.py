def shutdown():
    print("Choose an option:")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("shutting down")
    elif choice == "2":
        print("abort shut down")
    else:
        print("sorry")
shutdown()