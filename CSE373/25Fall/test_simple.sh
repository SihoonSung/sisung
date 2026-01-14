#!/bin/bash
count=0
total=0
timeout_count=0

for f in s-*.txt; do
    total=$((total + 1))
    echo -n "테스트 중: $f ... "
    start=$(date +%s)
    ./setcover < "$f" > /dev/null 2>&1 &
    pid=$!
    
    for i in {1..60}; do
        if ! kill -0 $pid 2>/dev/null; then
            wait $pid
            end=$(date +%s)
            elapsed=$((end - start))
            if [ $elapsed -lt 60 ]; then
                echo "완료 (${elapsed}초)"
                count=$((count + 1))
            else
                echo "시간 초과"
                timeout_count=$((timeout_count + 1))
            fi
            break
        fi
        sleep 1
        if [ $i -eq 60 ]; then
            kill $pid 2>/dev/null
            echo "시간 초과 (>60초)"
            timeout_count=$((timeout_count + 1))
        fi
    done
done

echo
echo "========================================"
echo "총 파일: $total개"
echo "1분 안에 완료: $count개"
echo "시간 초과: $timeout_count개"
echo "========================================"
