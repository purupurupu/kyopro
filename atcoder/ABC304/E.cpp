#include <bits/stdc++.h>
using namespace std;

vector<int> graph[200005];
bool visited[200005];

bool dfs(int u, int v)
{
    if (u == v)
        return true;
    visited[u] = true;
    for (int i = 0; i < graph[u].size(); i++)
    {
        int next_node = graph[u][i];
        if (!visited[next_node] && dfs(next_node, v))
            return true;
    }
    return false;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    for (int i = 0; i < M; i++)
    {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int K;
    cin >> K;
    vector<pair<int, int>> constraints(K);
    for (int i = 0; i < K; i++)
    {
        cin >> constraints[i].first >> constraints[i].second;
    }

    int Q;
    cin >> Q;
    vector<pair<int, int>> questions(Q);
    for (int i = 0; i < Q; i++)
    {
        cin >> questions[i].first >> questions[i].second;
    }

    for (auto [p, q] : questions)
    {
        graph[p].push_back(q);
        graph[q].push_back(p);
        bool good = true;
        for (auto [x, y] : constraints)
        {
            memset(visited, 0, sizeof(visited));
            if (dfs(x, y))
            {
                good = false;
                cout << "No\n";
                break;
            }
        }
        if (good)
        {
            cout << "Yes\n";
        }
        graph[p].pop_back();
        graph[q].pop_back();
    }

    return 0;
}
