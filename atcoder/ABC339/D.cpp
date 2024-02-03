#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <set>

using namespace std;

// 方向を示す配列
const int dx[4] = {0, 0, 1, -1};
const int dy[4] = {1, -1, 0, 0};

// BFSで最小操作回数を求める関数
int bfs(pair<int, int> start1, pair<int, int> start2, int N, vector<string> &grid)
{
    set<pair<pair<int, int>, pair<int, int>>> visited;
    queue<tuple<pair<int, int>, pair<int, int>, int>> q;
    q.push({start1, start2, 0});
    visited.insert({start1, start2});

    while (!q.empty())
    {
        auto [p1, p2, moves] = q.front();
        q.pop();
        int x1 = p1.first, y1 = p1.second;
        int x2 = p2.first, y2 = p2.second;

        // プレイヤーが同じマスにいるかチェック
        if (x1 == x2 && y1 == y2)
            return moves;

        for (int i = 0; i < 4; ++i)
        {
            int nx1 = x1 + dx[i], ny1 = y1 + dy[i];
            int nx2 = x2 + dx[i], ny2 = y2 + dy[i];

            // 移動先がグリッド内かつ障害物でないことを確認
            if (!(0 <= nx1 && nx1 < N && 0 <= ny1 && ny1 < N) || grid[nx1][ny1] == '#')
            {
                nx1 = x1;
                ny1 = y1;
            }
            if (!(0 <= nx2 && nx2 < N && 0 <= ny2 && ny2 < N) || grid[nx2][ny2] == '#')
            {
                nx2 = x2;
                ny2 = y2;
            }

            if (!visited.count({{nx1, ny1}, {nx2, ny2}}))
            {
                visited.insert({{nx1, ny1}, {nx2, ny2}});
                q.push({{nx1, ny1}, {nx2, ny2}, moves + 1});
            }
        }
    }

    return -1; // プレイヤーが集まることが不可能な場合
}

int main()
{
    int N;
    cin >> N;
    vector<string> grid(N);
    pair<int, int> positions[2];
    int count = 0;

    for (int i = 0; i < N; ++i)
    {
        cin >> grid[i];
        for (int j = 0; j < N; ++j)
        {
            if (grid[i][j] == 'P')
            {
                positions[count++] = {i, j};
            }
        }
    }

    // BFSを実行して最小操作回数を求める
    cout << bfs(positions[0], positions[1], N, grid) << endl;

    return 0;
}
