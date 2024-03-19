#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <vector>

struct graph {
    int N;
    int m;
    std::vector<std::vector<float>> nodes;
};

void pref_attach(graph* ba, int t, float E) {
    std::vector<float> cdf(t);

    float acc = 0;
    for (int i = 0; i < t; ++i) {
        acc += ba->nodes[i].size() / E;
        cdf[i] = acc;
    }

    for (int i = 0; i < ba->m; ++i) {
        float p = (float)rand() / RAND_MAX;

        int node = 0;
        while (node < cdf.size() && p >= cdf[node]) ++node;

        ba->nodes[t].push_back(node);
        ba->nodes[node].push_back(t);
    }
}

void rand_attach(graph* ba, int t, float E) {
    for (int i = 0; i < ba->m; ++i) {
        int node = rand() % t;
        ba->nodes[t].push_back(node);
        ba->nodes[node].push_back(t);
    }
}

int main(int argc, char** argv) {
    if (argc != 4) {
        printf("Usage: %s [p|r] N m\n", argv[0]);
        return 1;
    }

    srand(time(nullptr));

    char* attachment = argv[1];
    int N = atoi(argv[2]);
    int m = atoi(argv[3]);

    graph ba = {
        .N = N,
        .m = m,
        .nodes = std::vector<std::vector<float>>(N),
    };

    for (int i = 0; i < ba.m; ++i) {
        for (int j = 0; j < i; ++j) {
            ba.nodes[i].push_back(j);
            ba.nodes[j].push_back(i);
        }
    }

    for (int t = ba.m + 1; t < ba.N; ++t) {
        float E = 0;
        for (int i = 0; i < t; ++i) E += ba.nodes[i].size();

        switch (attachment[0]) {
            case 'p':
                pref_attach(&ba, t, E);
                break;
            case 'r':
                rand_attach(&ba, t, E);
                break;
            default:
                printf("Invalid attachment type\n");
                return 1;
        }
    }

    for (const auto& from : ba.nodes) {
        for (int to : from) {
            fprintf(stderr, "%d ", to);
        }
        fprintf(stderr, "\n");
    }

    for (const auto& from : ba.nodes) {
        printf("%zu\n", from.size());
    }

    return 0;
}
