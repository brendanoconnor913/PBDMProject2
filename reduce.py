#!/usr/bin/python

import sys
import hdfs

current_word = None
current_count = 0
word = None
unique_count = 0
duplicate_count = 0

client = hdfs.InsecureClient("http://localhost:50070", user="hduser")
# Use uniqs.txt and dups.txt to output corresponding tweets
with client.write('uniqs.txt', encoding='utf-8') as uniques, \
        client.write('dups.txt', encoding='utf-8') as duplicates:
    for line in sys.stdin:
        line = line.strip()
        # Get the word and the count
        word, count = line.split('\t', 1)

        try:
            count = int(count)
        except ValueError:
            continue

        # If the current word is this word increment counter with its value
        if current_word == word:
            current_count += count
        else:
            # if unique write to uniq file if dup write to dup file
            if current_word:
                if current_count > 1:
                    duplicates.write(current_word+"\n")
                    duplicate_count += 1
                else:
                    uniques.write(current_word+"\n")
                    unique_count += 1

            current_count = count
            current_word = word

# Output ratio of unique to duplicate
ratio = float(unique_count) / float(duplicate_count)
print 'number uniq:%.2f\tnumber dups:%.2f\tuniq to dups ratio:%.3f' % (unique_count,\
                                                           duplicate_count, ratio)
