"""
Utilities for some validation.
Not directly related to tracker but to ensure functionality.
"""
import unicodedata
import re
import shutil

def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    Django's slugify function, stripped to meet the needs
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

def delete_all_trackers():
    """
    Delete all trackers to clean up during debugging.
    """
    import stats_tracker # pylint: disable = import-outside-toplevel
    if stats_tracker.DEBUG:
        print("Deleting directory: ", stats_tracker.TRACKER_DIR_PATH)
        confirm = input("Confirm directory y/[n]: ")
        if confirm.lower() == "y":
            print("confirmed")
            shutil.rmtree(stats_tracker.TRACKER_DIR_PATH)
            print("deleted")
        else:
            print("Nothing to do.")
    else:
        print("To be only used in debugging. Please set DEBUG to True if you are sure")
