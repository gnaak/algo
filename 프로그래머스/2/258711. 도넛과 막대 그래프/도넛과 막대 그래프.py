def solution(edges):
    send_node = {}
    recieve_node = {}
    for send, recieve in edges :
        if send not in send_node:
            send_node[send] = []
        if recieve not in recieve_node:
            recieve_node[recieve] = []
        send_node[send].append(recieve)
        recieve_node[recieve].append(send)
        
    line_graph = 0 # 막대그래프는 맨 끝에 보내지 않는 애가 있음 
    eight_graph = 0 # 그래프 시작 정점은 2개 보내고 2개 받음 
    
    # 정점 찾기
    static_node = 0 
    for node in send_node:
        if len(send_node[node]) > 1 and node not in recieve_node:
            static_node = node
        # 8자 그래프 찾기 
        if node in send_node and node in recieve_node and len(send_node[node]) == 2 and len(recieve_node[node]) >= 2:
            eight_graph += 1
    for node in recieve_node:
        # 막대 그래프 찾기 
        if node not in send_node:
            line_graph += 1
            
    # 정점에서 나간만큼 그래프의 개수 
    total_graph = len(send_node[static_node])
    donut_graph = total_graph - line_graph - eight_graph
    answer = [static_node, donut_graph, line_graph, eight_graph]
    return answer