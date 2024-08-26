import sys
import time


def format_time(seconds: float) -> str:
    """Formats time in H:M:S."""
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


def format_progress_bar(percentage: int,
                        progress_blocks: int, remaining_blocks: int) -> str:
    """Formats the progress bar string."""
    return f"{percentage:3d}%|{'█' * progress_blocks}{'-' * remaining_blocks}|"


def ft_tqdm(lst: range) -> None:
    """
    A custom progress bar generator function.
    Parameters:
    - lst: An iterable to track progress for.
    Yields:
    - Items from the input iterable.
    """
    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst, start=1):
        elapsed_time = time.time() - start_time
        elapsed_str = format_time(elapsed_time)
        avg_speed = i / elapsed_time if elapsed_time > 0 else 0
        estimated_total_time = total / avg_speed if avg_speed > 0 else 0
        remaining_time = estimated_total_time - elapsed_time
        remaining_str = format_time(max(remaining_time, 0))
        progress_percentage = int(i * 100 / total)
        progress_blocks = int(progress_percentage / 2) * 2
        remaining_blocks = 100 - progress_blocks

        progress_bar = format_progress_bar(
            progress_percentage, progress_blocks, remaining_blocks)
        stats = (
            f"{i:>{len(str(total))}}/{total} "
            f"[{elapsed_str}<{remaining_str}, "
            f"{avg_speed:.2f}it/s]")

        # Clear the line and write the new progress
        sys.stdout.write(f"\033\r[K{progress_bar} {stats}\r")
        sys.stdout.flush()
        yield item
    print()


def main():
    time.sleep(0.001)
    for _ in ft_tqdm(range(50000)):
        pass


if __name__ == "__main__":
    main()
