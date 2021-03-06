# 참고 주소
# https://www.youtube.com/watch?v=-YQkA9vVqu8&list=RDCMUChflhu32f5EUHlY7_SetNWw&start_radio=1&t=463

# 다익스트라 알고리즘 : 길 찾기에서 사용되는 알고리즘
# 방문하지 않은 노드 중에 가장 짧은 것을 선택
# 음수 값이 없음
# 그리디 모델. - 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택하는 임의의 과정을 반복하는 것
# 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더이상 바뀌지 않음.
#   - 그렇기 때문에 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있음
#   - 다익스트라 알고리즘을 수행한 뒤엔 테이블에 각 노드까지의 최단 거리 정보가 저장됨.
# -------------------------------------------------

# 단계 :

# step 1 : 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드인 1번 노드를 처리
#   - 들어오는 곳이 없기에 혼자만 0원. 다른 것은 inf

# step 2 : 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드인 4번 노드를 처리
#   - 이미 방문한 노드는 처리 표시를 해준다.
#   - 갱신 여부 : True -> False

# step 3 : 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드인 2번 노드를 처리한다.
# step 4 : 가장 짧은 노드인 5번 노드를 처리.
#   - 6번은 아직까지 inf 였지만, 5번을 거쳐간 비용인 4로 갱신된다

# step 5 : 가장 짧은 노드인 3번 노드를 처리.
#   - 3번으로 가는 경우, 2번과 6번. 2번과 같은 경우 갔던 곳이고 6번은 5로 비싸기 때문에 무시한다.

# step 6 : 마지막으로 6번을 확인하는데, 바뀌지 않음. 인접한 노드가 없기 때문 (출발할 수가 없기 때문)
# --------------------------

# 다익스트라 알고리즘 : 간단한 구현 방법 (일반적인 방법은 heap을 이용)
#   1) 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해
#   매 단계마다 1차원 테이블의 모든 원소를 순차 탐색합니다.

import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m) :
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c 라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node() :
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(index)
    for i in range(1, n+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return  index

def dijkstra(start) :
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start] :
        distance[j[0]] = 1
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1) :
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now] :
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]] :
                distance[j[0]] = cost

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1) :
    # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF :
        print("INFINITY")
    # 도달할 수 있는 경우엔 거리를 출력
    else :
        print(distance[i])

# 간단한 구현 방법의 성능 분석 :
# 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야함.
# 그러므로 전체 시간 복잡ㄷ는 O(V^2)가 나옴.
# 노드의 개수가 기하급수적으로 늘어나면 문제가 발생함.
# 그렇다면 어떻게 해야할까? -> 우선순위 큐

# 우선 순위 쿠 (priority Queue)
#   - 우선 순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
#   - 예를 들어, 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건의 데이터부터 꺼내서 확인해야 하는 경우,
#   우선 순위 큐를 이용할 수 있음.
#   Python, C++, Java를 포함한 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원.

#   자료구조         추출되는 데이터
#   스택            가장 나중에 삽입된 데이터
#   큐              가장 먼저 삽입된 데이터
#   우선순위 큐      가장 우선 순위가 높은 데이터

# 힙 (Heap)
#   - 우선 순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
#   - 최소 힙과 최대 힙이 있음
#   - 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용됨

#   우선순위 큐 구현 방식        삽입시간        삭제시간
#   리스트                      O(1)            O(N)
#   힙(Heap)                   O(logN)         O(logN)

# 힙 라이브러리 사용 예제 : 최소 힙
import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable) :
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable :
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
# result : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

