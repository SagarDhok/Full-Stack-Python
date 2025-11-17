
import sys

def process_command(command):
    match command:
        case "start":
            print("Starting the process...")
        case "stop":
            print("Stopping the process...")
            sys.exit(0)  # The program terminates here, nothing below this will run
        case "restart":
            print("Restarting the process...")
        case _:
            print("Unknown command.")
            sys.exit(1)  # Exit with an error code

    print("This will not be printed if sys.exit() is called!")

# Example usage
process_command("GG")
