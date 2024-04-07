#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <numeric>
#include <string>
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

        float exp_theta = std::exp(-std::log(this->p / (1 - this->p)));

        for (int t = 0; t < 1e6; ++t) {
            int i = rand() % N;
            int j = rand() % N;

            if (this->e[i][j] == 0) {
                this->e[i][j] = 1;
            } else if ((float)rand() / RAND_MAX < exp_theta) {
                this->e[i][j] = 0;
            }
        }
    }
};

int main(int argc, char** argv) {
    srand(time(NULL));

    if (argc != 4) {
        printf("Usage: er <type> <N> <p>\n");
        return 1;
    }

    char type = argv[1][0];
    int N = atoi(argv[2]);
    float p = atof(argv[3]);

    ER* graph = new ER(type, N, p);
    graph->print_edges();

    return 0;
}
