def main():
  # 入力
  N, M = map(int, input().split())
  X = list(map(int, input().split()))

  # 全ての島から他の全ての島への最短距離を計算
  distance = floyd_warshall(N, X)

  # 最短ツアーの長さの最小値
  min_length = float('inf')
  for i in range(N):
    # i番目の橋を封鎖した場合の長さ
    length = 0
    for j in range(N):
      if i != j:
        length = max(length, distance[i][j])

    # 最小値更新
    min_length = min(min_length, length)

  # 出力
  print(min_length)


def floyd_warshall(N, X):
  # 距離の初期化
  distance = [[float('inf')] * N for _ in range(N)]
  for i in range(N):
    distance[i][i] = 0

  # 各橋の情報に基づいて距離を更新
  for i in range(N - 1):
    distance[i][i + 1] = 1
    distance[i + 1][i] = 1

  # ワーシャルフロイド法による最短距離計算
  for k in range(N):
    for i in range(N):
      for j in range(N):
        distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

  return distance


if __name__ == '__main__':
  main()
