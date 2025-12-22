import sys
import time


def ft_tqdm(lst: range) -> None:
    """
    Custom progress bar generator mimicking tqdm.
    Yields items from the iterable while displaying progress.
    """
    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst, start=1):
        elapsed = time.time() - start_time
        speed = i / elapsed if elapsed > 0 else 0
        eta = (total - i) / speed if speed > 0 else 0

        percent = int(i * 100 / total)
        bar_filled = int(percent / 2) * 2
        bar_empty = 100 - bar_filled

        bar = f"{percent:3d}%|{'█' * bar_filled}{'-' * bar_empty}|"
        stats = (
            f"{i:>{len(str(total))}}/{total} "
            f"[{time.strftime('%H:%M:%S', time.gmtime(elapsed))}<"
            f"{time.strftime('%H:%M:%S', time.gmtime(eta))}, "
            f"{speed:.2f}it/s]"
        )

        sys.stdout.write(f"\033\r[K{bar} {stats}\r")
        sys.stdout.flush()
        yield item
    print()
