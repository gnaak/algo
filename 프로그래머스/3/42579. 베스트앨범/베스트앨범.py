def solution(genres, plays):
    genre_lst = {}
    genre_lst_each = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] not in genre_lst:
            genre_lst[genres[i]] = 0
            genre_lst_each[genres[i]] = []
        genre_lst[genres[i]] += plays[i]
        genre_lst_each[genres[i]].append((plays[i],i))
    genre_lst = sorted(genre_lst.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in genre_lst:
        print(genre)
        genre_lst_each[genre].sort(key=lambda x: (-x[0], x[1]))

        for i in range(min(2,len(genre_lst_each[genre]))):
            answer.append(genre_lst_each[genre][i][1])
    return answer