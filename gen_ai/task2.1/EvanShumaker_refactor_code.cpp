#include <iostream>
#include <fstream>
#include <vector>
#include "binTree.h"

using namespace std;

// Default constructor using initializer list
binTree::binTree() : root(nullptr) {}

// Constructor for a leaf node (with a letter and its frequency)
binTree::binTree(char letter, int frequency) {
    root = new binTreeNode{letter, frequency, nullptr, nullptr};
}

// Constructor for combining two subtrees into a new tree
binTree::binTree(binTree *t1, binTree *t2) {
    root = new binTreeNode;
    root->left = t1->root;
    root->right = t2->root;
    // Use '\0' as a sentinel value for internal nodes with no letter.
    root->letter = '\0';
    root->frequency = t1->getFrequency() + t2->getFrequency();
}

// Destructor: deallocate all nodes via post-order traversal
binTree::~binTree() {
    destroyTree(root);
}

// Post-order traversal to delete all nodes in the tree
void binTree::destroyTree(binTreeNode *node) {
    if (node == nullptr)
        return;
    destroyTree(node->left);
    destroyTree(node->right);
    delete node;
}

// Returns the frequency stored at the root (or 0 if the tree is empty)
int binTree::getFrequency() const {
    return root ? root->frequency : 0;
}

// Public function to get the prefix code for a letter.
// It calls the overloaded recursive function and then removes the marker.
string binTree::getPrefixCode(char letter) {
    string code = getPrefixCode(root, letter);
    // Remove the trailing marker '2' that signals the found letter.
    if (!code.empty() && code.back() == '2') {
        code.pop_back();
    }
    return code;
}

// Recursive helper: finds the prefix code for the given letter.
// Returns a string ending with '2' as a marker if the letter is found.
string binTree::getPrefixCode(binTreeNode *node, char letter) {
    if (node == nullptr)
        return "";
    
    // Check if we're at a leaf node.
    if (node->left == nullptr && node->right == nullptr) {
        if (node->letter == letter)
            return "2"; // Marker indicating the letter is found.
        return "";
    }
    
    // Search in the left subtree.
    string leftCode = getPrefixCode(node->left, letter);
    if (!leftCode.empty())
        return "0" + leftCode;
    
    // Search in the right subtree.
    string rightCode = getPrefixCode(node->right, letter);
    if (!rightCode.empty())
        return "1" + rightCode;
    
    return "";
}

