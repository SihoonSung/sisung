#!/bin/bash
timeout=60
count=0
total=0
timeout_count=0

for f in s-*.txt; do
    total=$((total + 1))
    echo -n "$f: "
    start=$(date +%s.%N)
    (./setcover < "$f" > /dev/null 2>&1) &
    pid=$!
    sleep $timeout
    if kill -0 $pid 2>/dev/null; then
        kill $pid 2>/dev/null
        echo "시간 초과 (>${timeout}초)"
        timeout_count=$((timeout_count + 1))
    else
        wait $pid
        end=$(date +%s.%N)
        elapsed=$(echo "$end - $start" | bc)
        if (( $(echo "$elapsed < $timeout" | bc -l) )); then
            printf "%.2f초 - 완료\n" "$elapsed"
            count=$((count + 1))
        else
            echo "시간 초과 (>${timeout}초)"
            timeout_count=$((timeout_count + 1))
        fi
    fi
done

echo
echo "========================================"
echo "총 파일: $total개"
echo "1분 안에 완료: $count개"
echo "시간 초과: $timeout_count개"
echo "========================================"
