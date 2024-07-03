function solution(cap, n, deliveries, pickups) {
  var answer = -1;
  function lastIdx(arr) {
    let len = arr.length;
    for (let i = len - 1; i >= 0; i--) {
      if (arr[i] != 0) {
        return i;
      } else {
        arr.pop();
      }
    }
    return -1;
  }
  function check(arr, cap) {
    let idx = lastIdx(arr);
    let dist = idx;
    while (idx >= 0 && cap > 0) {
      if (arr[idx] >= cap) {
        arr[idx] -= cap;
        cap = 0;
        break;
      } else {
        cap -= arr[idx];
        arr[idx] = 0;
        idx--;
      }
    }
    return dist;
  }

  while (true) {
    var delLen = check(deliveries, cap) + 1;
    var pickLen = check(pickups, cap) + 1;
    if (delLen === 0 && pickLen === 0) {
      return answer + 1;
    } else if (delLen > pickLen) {
      answer += delLen * 2;
    } else {
      answer += pickLen * 2;
    }
  }
}
