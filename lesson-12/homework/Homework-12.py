import threading

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result_list):
    """Check primes in range [start, end) and append to result_list."""
    local_primes = []
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    result_list.extend(local_primes)

def main():
    range_start = 1
    range_end = 1000
    num_threads = 4

    chunk_size = (range_end - range_start) // num_threads
    threads = []
    primes_found = []


    for i in range(num_threads):
        start = range_start + i * chunk_size      
        end = start + chunk_size if i != num_threads - 1 else range_end
        t = threading.Thread(target=check_primes, args=(start, end, primes_found))
        threads.append(t)
        t.start()

   
    for t in threads:
        t.join()

    primes_found.sort()
    print("Prime numbers found:", primes_found)

if __name__ == "__main__":
    main()




import threading
from collections import Counter

def process_lines(lines, result_list):
    """Count words in the given list of lines."""
    word_count = Counter()
    for line in lines:
        words = line.strip().split()
        word_count.update(words)
    result_list.append(word_count)

def main():
    file_path = "large_text.txt"
    num_threads = 4

  
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

   
    chunk_size = len(lines) // num_threads
    threads = []
    partial_counts = []

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i != num_threads - 1 else len(lines)
        t = threading.Thread(target=process_lines, args=(lines[start:end], partial_counts))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


    total_count = Counter()
    for pc in partial_counts:
        total_count.update(pc)

    print("Word occurrences:")
    for word, count in total_count.most_common():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
