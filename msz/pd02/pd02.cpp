#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <cstdlib>
#include <vector>

typedef std::vector<float> edges;
struct graph {
    int N;
    int m;
    std::vector<edges> nodes;
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

void random_attach(graph* ba, int t, float E) {
    for (int i = 0; i < ba->m; ++i) {
        int node = rand() % t / RAND_MAX;
        ba->nodes[t].push_back(node);
        ba->nodes[node].push_back(t);
    }
}

int main(int argc, char** argv) {
    srand(time(NULL));

    char* attachment = argv[1];
    int N = atoi(argv[2]);
    int m = atoi(argv[3]);

    graph ba = {
        .N = N,
        .m = m,
        .nodes = std::vector<edges>(N),
    };

    for (int i = 0; i < ba.N; ++i) {
        ba.nodes[i] = edges();
    }

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
                random_attach(&ba, t, E);
                break;
            default:
                break;
        }
    }

    for (edges from : ba.nodes) {
        for (int to : from) {
            fprintf(stderr, "%d ", to);
        }
        fprintf(stderr, "\n");
    }

    for (edges from : ba.nodes) {
        printf("%zu\n", from.size());
    }

    return 0;
}
