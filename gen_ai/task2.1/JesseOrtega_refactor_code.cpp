#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib>

// Function to add a dramatic typewriter effect
void typewriterEffect(const std::string& text, int delay = 50) {
    for (char c : text) {
        std::cout << c << std::flush;
        std::this_thread::sleep_for(std::chrono::milliseconds(delay));
    }
}

// Function to get a random ANSI color code
std::string getRandomColor() {
    const std::string colors[] = {
        "\033[31m", // Red
        "\033[32m", // Green
        "\033[33m", // Yellow
        "\033[34m", // Blue
        "\033[35m", // Magenta
        "\033[36m", // Cyan
        "\033[91m", // Bright Red
        "\033[92m", // Bright Green
        "\033[93m", // Bright Yellow
        "\033[94m", // Bright Blue
        "\033[95m", // Bright Magenta
        "\033[96m"  // Bright Cyan
    };
    return colors[rand() % (sizeof(colors) / sizeof(colors[0]))];
}

// Function to print ASCII-stylized text
void asciiHelloWorld() {
    std::string art = R"(
 _    _      _ _       
| |  | |    | | |      
| |__| | ___| | | ___  
|  __  |/ _ \ | |/ _ \ 
| |  | |  __/ | | (_) |
|_|  |_|\___|_|_|\___/ 
    )";

    std::cout << getRandomColor(); // Set random color
    typewriterEffect(art, 10);
    std::cout << "\033[0m\n"; // Reset color
}

int main() {
    srand(time(0)); // Seed for random colors

    // Epic ASCII intro
    asciiHelloWorld();
    
    // Extra spice - typewriter effect for "Hello, world!"
    typewriterEffect("\n🔥 Welcome to the most STANKED Hello, World! 🔥\n", 40);
    
    return 0;
}
