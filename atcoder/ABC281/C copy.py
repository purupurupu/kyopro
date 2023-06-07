# N曲からなるプレイリストの曲の数を標準入力から取得
n, t = map(int, input().split())

# 曲の合計長さ
total_length = 0

# 曲リスト内の曲の長さを格納する配列
song_lengths = []

# 曲リスト内の曲の長さを標準入力から取得して配列に格納する
for i in range(n):
    song_lengths.append(int(input()))
    total_length += song_lengths[i]

# T秒後に流れている曲が何番目か、その曲が再生されてから何秒経過したかを求める

# total_length と T の差が何回割り切れるかを調べる
num_times_played = t // total_length

# T から num_times_played * total_length を引いた値
remaining_time = t - num_times_played * total_length

# 曲リスト内の曲を 1 から N 番目まで順番に見て、曲が remaining_time 以内に収まる最初の曲を current_song とする
current_song = 1

# remaining_timeが曲リスト内の曲をすべて超えている場合は曲リスト内の曲をすべて見るまでループする
while remaining_time > 0:
    # 曲リスト内の次の曲の長さ
    next_song_length = song_lengths[current_song]
    # remaining_timeが曲リスト内の次の曲を超えるかどうか
    if remaining_time > next_song_length:
        # remaining_timeから曲リスト内の次の曲の長さを引く
        remaining_time -= next_song_length
        # 曲番号を1つ増やす
        current_song += 1
    else:
        # remaining_timeが曲リスト内の次の曲を超えない場合は終了
        break
