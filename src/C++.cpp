#include <iostream>
int _ICC_ratio[] = {7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2};
std::string _ICC_ID;
bool _ICC_Check_ID() {
    int sum = 0;
    char last_word;
    for (int i = 0; i < 17; i++) {
        sum += (_ICC_ID[i] - '0') * _ICC_ratio[i];
    }
    if ((12 - (sum % 11)) == 10)
        last_word = 'X';
    else if ((12 - (sum % 11)) == 0)
        last_word = '1';
    else if ((12 - (sum % 11)) == 1)
        last_word = '0';
    else
        last_word = (12 - (sum % 11)) + '0';
    return last_word == _ICC_ID[17];
}
int main() {
    std::cin >> _ICC_ID;
    std::cout << _ICC_Check_ID();
    return 0;
}