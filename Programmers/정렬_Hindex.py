def solution(citations):
    answer = 0
    sort_citations = sorted(citations)
    for h in range(len(sort_citations)):
        if sort_citations[h] >= len(sort_citations) - h:
            return len(sort_citations) - h
    return answer