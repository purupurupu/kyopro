#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, pair<int, int>> &a, pair<int, pair<int, int>> &b)
{
    long long a_total = (long long)a.first + a.second.first;
    long long b_total = (long long)b.first + b.second.first;

    if (a_total * b.second.first == b_total * a.second.first)
    {
        return a.second.second < b.second.second;
    }

    return a_total * b.second.first > b_total * a.second.first;
}

int main()
{
    int N;
    cin >> N;

    vector<pair<int, pair<int, int>>> people(N);
    for (int i = 0; i < N; i++)
    {
        int Ai, Bi;
        cin >> Ai >> Bi;
        people[i] = make_pair(Ai, make_pair(Bi, i + 1));
    }

    sort(people.begin(), people.end(), compare);

    for (auto &p : people)
    {
        cout << p.second.second << " ";
    }
    return 0;
}
