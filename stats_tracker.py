"""
Usage:
    tracker init                # to start
    tracker create              # to create a variable to track
    tracker log {variable}      # add a value to log for the variable
    tracker list                # show variables currently being tracked
    tracker graph {variable}    # plot the daily averages of the variable
"""
import os
from utils import slugify

DEBUG = True

if DEBUG:
    TRACKER_DIR_PATH = os.path.join("./", ".tracker")
else:
    TRACKER_DIR_PATH = os.path.join(os.environ['HOME'], ".tracker")

def tracker_init():
    """
    Create a `.tracker/` directory at $HOME
    """
    if not os.path.exists(TRACKER_DIR_PATH):
        print("$HOME/.tracker does not exist. Creating...")
        os.mkdir(TRACKER_DIR_PATH)
    else:
        print("Directory exists, nothing to do")

def tracker_create():
    """
    Create a log file to log the values, under the tracker directory
    """
    tracking_var = input("Enter the name of the variable to track: ")
    tracking_var = slugify(tracking_var)
    tracking_file = os.path.join(TRACKER_DIR_PATH, tracking_var)

    if not os.path.exists(tracking_file):
        open(tracking_file, 'a').close()
    else:
        print("File already exists. Nothing to do.")

def tracker_log():
    """
    Log an entry to the variable
    """

def tracker_list():
    """
    List the current variables being tracked
    Same result as `ls ~/.tracker`
    """
    print("Currently tracking:")
    for entry in os.listdir(TRACKER_DIR_PATH):
        print(entry)

def tracker_graph():
    """
    Graph the values - defaults to last 30 days
    """

def tracker():
    """
    Start the program
    """
