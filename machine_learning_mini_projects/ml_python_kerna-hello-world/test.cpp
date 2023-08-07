#include <iostream>
using namespace std;
template <typename T>
class TNode {
public:
    TNode(T data) : data(data), prev(nullptr), next(nullptr) {}

    void AddNext(TNode<T>* node) {
        if (node == nullptr) {
            return;
        }
        node->prev = this;
        node->next = next;
        if (next != nullptr) {
            next->prev = node;
        }
        next = node;
    }

    void AddPrev(TNode<T>* node) {
        if (node == nullptr) {
            return;
        }
        node->prev = prev;
        node->next = this;
        if (prev != nullptr) {
            prev->next = node;
        }
        prev = node;
    }

    void Print() const {
        cout << data << " ";
    }

    TNode<T>* GetPrev() const {
        return prev;
    }

    TNode<T>* GetNext() const {
        return next;
    }

    T GetData() const {
        return data;
    }

private:
    T data;
    TNode<T>* prev;
    TNode<T>* next;
};

int main() {
    TNode<int>* first = new TNode<int>(1);
    TNode<int>* second = new TNode<int>(2);
    TNode<int>* third = new TNode<int>(3);

    first->AddNext(second);
    second->AddNext(third);

    first->AddPrev(new TNode<int>(999));

    int count = 0;
    TNode<int>* current = first;
    while (current != nullptr) {
        current->Print();
        current = current->GetNext();
        ++count;
    }

    cout << "First element: " << first->GetData() << endl;

    delete first;
    delete second;
    delete third;

    return 0;
}