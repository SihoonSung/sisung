#!/bin/bash
for f in s-*.txt; do
    echo -n "$f: "
    start=$(date +%s.%N)
    ./setcover < "$f" > /dev/null 2>&1
    end=$(date +%s.%N)
    runtime=$(echo "$end - $start" | bc)
    printf "%.4f초\n" "$runtime"
done
