import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 도감에 등록되어 있는 포켓몬 수, 맞춰야 하는 문제의 개수
pokemon = {}
for i in range(1,n+1): # n개의 줄에 1번부터 n번인 포켓몬
    # 포켓몬의 첫글자만 대문자, 일부 포켓몬은 마지막 문자만 대문자
    pokemon_name = input().strip()
    pokemon[str(i)] = pokemon_name # 1 : 이상해씨
    pokemon[pokemon_name] = str(i) # 이상해씨 : 1
for _ in range(m) : # 내가 맞춰야 하는 문제
    # 번호가 들어왓으면 그 해당 번호 포켓몬,
    # 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호
    q = input().strip()
    print(pokemon[q])


