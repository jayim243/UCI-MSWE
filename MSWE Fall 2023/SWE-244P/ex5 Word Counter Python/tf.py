import re, sys, collections, os, concurrent.futures #import os and concurrent.futures (os to find directory path, concurrent.futures for thread pool)

# worker function (run method): words open file given the file name from thread pool
def worker_function(file): 
    stopwords = set(open('stop_words').read().split(','))
    # Read the contents of the file
    with open(file, 'r') as file:
        content = file.read().lower()
    words = re.findall('\w{3,}', content)
    
    counts = collections.Counter(w for w in words if w not in stopwords)
    return counts


def main():
    # create fixed thread pool 4 for 4 threads to work on 4 text files
    with concurrent.futures.ThreadPoolExecutor(4) as executor:
        # Get the directory of the currently running script
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Get a list of all files in the current directory
        all_files = os.listdir(current_directory)

        # Filter out only the text files (files ending with '.txt')
        text_files = [file for file in all_files if file.endswith('.txt')]

        # Submit tasks to the thread pool and collect the results
        results = list(executor.map(worker_function, text_files))

    combined_counts = collections.Counter()
    for result in results:
        combined_counts.update(result)

    # Print the top 40 most frequently occurring words
    for (word, count) in combined_counts.most_common(40):
        print(word, '-', count)


if __name__ == "__main__":
    main()