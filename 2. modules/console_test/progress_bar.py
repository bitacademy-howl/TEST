#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
from time import sleep

# Print iterations progress
def print_progress(iteration, total, prefix='Progress:', suffix='Complete', decimals=1, bar_length=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : 현재 위치 (Int)
        total       - Required  : 전체 위치 (Int)
        prefix      - Optional  : 전위 문자 (Str)
        suffix      - Optional  : 후위 문자 (Str)
        decimals    - Optional  : 소수점 이하 자리 표시 (Int)
        bar_length  - Optional  : 프로그레스바 전체 길이 (Int)
    """
    str_format = "{0:." + str(decimals) + "f}"
    current_progress = iteration / float(total)
    percents = str_format.format(100 * current_progress)
    filled_length = int(round(bar_length * current_progress))
    bar = "#" * filled_length + '-' * (bar_length - filled_length)

    # 캐리지 리턴(\r) 문자를 이용해서 출력후 커서를 라인의 처음으로 옮김
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

    # 현재 위치가 전체 위치에 도달하면 개행문자 추가
    if iteration == total:
        sys.stdout.write('\n')

    # 버퍼의 문자를 출력
    sys.stdout.flush()

if __name__ == "__main__":
    # 출력 리스트 샘플
    items = list(range(0, 54))
    items_length = len(items)

    # 0%를 출력
    print_progress(0, items_length)

    for i, item in enumerate(items):
        # 실제 처리할 작업
        # 0.1초 sleep
        sleep(0.1)
        # 프로그레스바 변환
        print_progress(i + 1, items_length)