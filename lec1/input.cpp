#include <iostream>
#include <string>
using namespace std;

int main() {
    string buf;
    getline(cin, buf);
    cout << "[+] Received: " << buf << endl;
    return 0;
}
