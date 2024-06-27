function solution(genres, plays) {
    let genre_lst = {};
    let genre_lst_each = {};
    let answer = [];

    for (let i = 0; i < genres.length; i++) {
        if (!genre_lst[genres[i]]) {
            genre_lst[genres[i]] = 0;
            genre_lst_each[genres[i]] = [];
        }
        genre_lst[genres[i]] += plays[i];
        genre_lst_each[genres[i]].push([plays[i], i]);
    }

    genre_lst = Object.entries(genre_lst).sort((a, b) => b[1] - a[1]);

    for (let [genre, _] of genre_lst) {
        genre_lst_each[genre].sort((a, b) => b[0] - a[0] || a[1] - b[1]);

        for (let i = 0; i < Math.min(2, genre_lst_each[genre].length); i++) {
            answer.push(genre_lst_each[genre][i][1]);
        }
    }

    return answer;
}
