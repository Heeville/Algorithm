#include <iostream>
#include <queue>
#include <vector>
#include <stack>

#define MAX_VERTEX 1001
#define INF 10000000000001
using namespace std;

int n, m;
vector<pair<int, int>> graph[MAX_VERTEX];
long long distances[MAX_VERTEX];
int path[MAX_VERTEX];

void dijkstra(int start, int end)
{
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, start });

	while (!pq.empty())
	{
		int now = pq.top().second;
		int cost_now = -pq.top().first;
		pq.pop();

		if (distances[now] < cost_now)
			continue;

		for (int i = 0; i < graph[now].size(); i++)
		{
			int dest = graph[now][i].first;
			int cost = graph[now][i].second + cost_now;
			if (distances[dest] > cost)
			{
				distances[dest] = cost;
				pq.push({ -cost, dest });
				path[dest] = now;
			}
		}
	}

}

int main()
{
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int start, end, count = 0;
	stack<int> pathStack;

	cin >> n;
	cin >> m;

	for (int i = 0; i < m; i++)
	{
		int a, b, c;
		cin >> a >> b >> c;
		graph[a].push_back({ b, c });
	}

	cin >> start >> end;
	
	fill(distances + 1, distances + n + 1, INF);
	distances[start] = 0;

	dijkstra(start, end);

	cout << distances[end] << endl;

	pathStack.push(end);
	for(int i = end; i != start;)
	{
		pathStack.push(path[i]);
		i = path[i];
	}

	cout << pathStack.size() << endl;

	while (!pathStack.empty())
	{
		cout << pathStack.top() << " ";
		pathStack.pop();
	}

	return 0;
}