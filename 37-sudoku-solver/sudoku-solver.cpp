class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        int rows[9] = {0}, cols[9] = {0}, boxes[9] = {0};
        vector<pair<int,int>> empty;

        auto box_id = [](int r, int c) {
            return (r / 3) * 3 + (c / 3);
        };

        auto bit = [](int d) {
            return 1 << (d - 1);
        };


        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    empty.push_back({r, c});
                } else {
                    int d = board[r][c] - '0';
                    rows[r] |= bit(d);
                    cols[c] |= bit(d);
                    boxes[box_id(r, c)] |= bit(d);
                }
            }
        }

        function<bool()> dfs = [&]() {
            if (empty.empty()) return true;

            int best_i = -1, best_mask = 0, best_cnt = 10;
            for (int i = 0; i < (int)empty.size(); i++) {
                int r = empty[i].first, c = empty[i].second;
                int used = rows[r] | cols[c] | boxes[box_id(r, c)];
                int avail = (~used) & 0x1FF;
                if (avail == 0) return false;
                int cnt = __builtin_popcount((unsigned)avail);
                if (cnt < best_cnt) {
                    best_cnt = cnt;
                    best_mask = avail;
                    best_i = i;
                    if (cnt == 1) break;
                }
            }

            int r = empty[best_i].first, c = empty[best_i].second;
            int b = box_id(r, c);
            int avail = best_mask;

            swap(empty[best_i], empty.back());
            empty.pop_back();

            while (avail) {
                int pick = avail & -avail; 
                int d = __builtin_ctz((unsigned)pick) + 1; 

                board[r][c] = char('0' + d);
                rows[r] |= pick;
                cols[c] |= pick;
                boxes[b] |= pick;

                if (dfs()) return true;

                board[r][c] = '.';
                rows[r] &= ~pick;
                cols[c] &= ~pick;
                boxes[b] &= ~pick;

                avail &= avail - 1; 
            }

            empty.push_back({r, c});
            return false;
        };

        dfs();
    }
};
