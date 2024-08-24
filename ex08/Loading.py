import sys
import time
from tqdm import tqdm

def ft_tqdm(lst):
    total = len(lst)
    start_time = time.time()
    
    for i, item in enumerate(lst, start=1):
        elapsed_time = time.time() - start_time
        elapsed_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        
        avg_speed = i / elapsed_time if elapsed_time > 0 else 0
        
        estimated_total_time = total / avg_speed if avg_speed > 0 else 0
        remaining_time = estimated_total_time - elapsed_time
        remaining_str = time.strftime("%H:%M:%S", time.gmtime(max(remaining_time, 0)))
        
        progress_percentage = int(i * 100 / total)
        progress_blocks = int(progress_percentage / 2) * 2
        remaining_blocks = 50 - progress_blocks
        
        if i < total:
            sys.stdout.write(f"\r{progress_percentage:3d}%|{'█' * progress_blocks}{'-' * remaining_blocks}| {i:}/{total} [{elapsed_str}<{remaining_str}, {avg_speed:.2f}it/s]")
        else:
            sys.stdout.write(f"\r{progress_percentage:3d}%|{'█' * progress_blocks}{'-' * remaining_blocks}| {i:}/{total} [{elapsed_str}<{remaining_str}, {avg_speed:.2f}it/s]\n")
        
        sys.stdout.flush()
        yield item

    print()
def main():
    time.sleep(0.001)
    for _ in ft_tqdm(range(500)):
        time.sleep(0.001)
    for _ in tqdm(range(500)):
        time.sleep(0.001)

if __name__ == "__main__":
    main()
