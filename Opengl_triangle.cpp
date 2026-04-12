#define GLFW_INCLUDE_NONE
#include <GLFW/glfw3.h>
#include <GL/gl.h>
#include <iostream>
using namespace std;

class Triangle {
private:
    float vertices[9] = {
        -0.5f, -0.5f, 0.0f,
         0.5f, -0.5f, 0.0f,
         0.0f,  0.5f, 0.0f
    };

public:
    void draw() const {
        glBegin(GL_TRIANGLES);
        glVertex3f(vertices[0], vertices[1], vertices[2]);
        glVertex3f(vertices[3], vertices[4], vertices[5]);
        glVertex3f(vertices[6], vertices[7], vertices[8]);
        glEnd();
    }

    void setup() {
        // No setup needed for immediate-mode rendering.
    }
};

int main() {
    if (!glfwInit()) {
        cerr << "Failed to initialize GLFW" << endl;
        return 1;
    }
    GLFWwindow* window = glfwCreateWindow(800, 600, "hello", nullptr, nullptr);
    if (!window) {
        cerr << "Failed to create GLFW window" << endl;
        glfwTerminate();
        return 1;
    }

    glfwMakeContextCurrent(window);

    Triangle triangle;
    triangle.setup();

    cout << "hello" << endl;

    while (!glfwWindowShouldClose(window)) {
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);
        triangle.draw();
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwDestroyWindow(window);
    glfwTerminate();
    return 0;
}

