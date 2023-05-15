#include <stack>

class MyQueue {
private:
    std::stack<int> pushStack;
    std::stack<int> popStack;

public:
    MyQueue() {}

    void push(int x) {
        pushStack.push(x);
    }

    int pop() {
        if (popStack.empty()) {
            while (!pushStack.empty()) {
                popStack.push(pushStack.top());
                pushStack.pop();
            }
        }
        int front = popStack.top();
        popStack.pop();
        return front;
    }

    int peek() {
        if (popStack.empty()) {
            while (!pushStack.empty()) {
                popStack.push(pushStack.top());
                pushStack.pop();
            }
        }
        return popStack.top();
    }

    bool empty() {
        return pushStack.empty() && popStack.empty();
    }
};
