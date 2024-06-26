#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <numeric>
#include <vector>

typedef std::vector<int> nodes;

class ER {
   public:
    int N;
    float p;

    nodes v;
    std::vector<nodes> e;

    ER(char type, int N, float p) {
        this->N = N;
        this->p = p;

        nodes v(N);
        std::iota(v.begin(), v.end(), 0);
        this->v = v;

        std::vector<nodes> e(N);
        this->e = e;
        switch (type) {
            case 't':
                this->traditional();
                break;
            case 'm':
                this->metropolis();
                break;
            default:
                break;
        }
    }

    void print_edges() {
        for (int i = 0; i < this->N; ++i) {
            for (int j = 0; j < this->e[i].size(); ++j) {
                printf("%d ", this->e[i][j]);
            }
            printf("\n");
        }
    }

   private:
    void traditional() {
        for (int i = 0; i < this->N; ++i) {
            for (int j = 0; j < i; ++j) {
                float rand_num = (float)rand() / RAND_MAX;
                if (rand_num < this->p) {
                    this->e[i].push_back(j);
                    this->e[j].push_back(i);
                }
            }
        }
    }

    void metropolis() {
        for (int i = 0; i < this->N; ++i) {
            nodes edges(N);
            std::fill(edges.begin(), edges.end(), 0);
            this->e[i] = edges;
        }

        int p = this->p > 0.5;
        float theta = p ? std::log(this->p / (1 - this->p))
                        : std::log((1 - this->p) / this->p);

        float exp_theta = std::exp(-theta);
        int steps = 1e7;

        for (int t = 0; t < steps; ++t) {
            int i, j;
            do {
                i = rand() % this->N;
                j = rand() % this->N;
            } while (i == j);

            if (this->e[i][j] == !p) {
                this->e[i][j] = p;
            } else if ((float)rand() / RAND_MAX < exp_theta) {
                this->e[i][j] = !p;
            }

            if (t % (steps / 100) == 0) {
                int E = 0;
                for (int i = 0; i < this->N; ++i) {
                    for (int j = 0; j < i; ++j) {
                        E += this->e[i][j];
                    }
                }
                fprintf(stderr, "%d %d\n", t, E);
            }
        }
    }
};

int main(int argc, char** argv) {
    srand(time(NULL));

    if (argc != 4) {
        printf("Usage: ./a.out <type> <N> <p>\n");
        return 1;
    }

    char type = argv[1][0];
    int N = atoi(argv[2]);
    float p = atof(argv[3]);

    ER* graph = new ER(type, N, p);
    graph->print_edges();

    return 0;
}
