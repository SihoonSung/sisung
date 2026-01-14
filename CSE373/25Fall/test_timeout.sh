#!/bin/bash
timeout=60
count=0
total=0

for f in s-*.txt; do
    total=$((total + 1))
    echo -n "$f: "
    start=$(date +%s)
    timeout $timeout ./setcover < "$f" > /dev/null 2>&1
    exit_code=$?
    end=$(date +%s)
    elapsed=$((end - start))
    
    if [ $exit_code -eq 124 ]; then
        echo "시간 초과 (>${timeout}초)"
    elif [ $exit_code -eq 0 ]; then
        echo "${elapsed}초 - 완료"
        count=$((count + 1))
    else
        echo "오류 발생"
    fi
done

echo
echo "========================================"
echo "총 파일: $total개"
echo "1분 안에 완료: $count개"
echo "시간 초과: $((total - count))개"
echo "========================================"
