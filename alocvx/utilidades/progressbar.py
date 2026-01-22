
import sys


def progress_bar(current, total, width=50):
    percent = current / total
    filled = int(width * percent)
    bar = "█" * filled + "░" * (width - filled)
    sys.stdout.write(f"\r[{bar}] {percent:.1%} ({current}/{total})")
    sys.stdout.flush()