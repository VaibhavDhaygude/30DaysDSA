#include<iostream>
using namespace std;

class node{
    public:
        int val;
        node* right;
        node* left;
        node(int ele){
            val=ele;
            right=left=NULL;
        }
};
int height(node* root){
    if (root==NULL){
        return 0;
    }
    return 1+max(height(root->left),height(root->right));

}

bool balanced(node* root){
    // cout<<"inn"<<endl;

    if (root==NULL){
        return true;
    }

    int lh=height(root->left);
    int rh=height(root->right);
    
    if (abs(lh-rh)<=1 && balanced(root->left) && balanced(root->right)){
        return true;
    }
    return false;
}


int main(){
    node* root=new node(5);
    root->left=new node(2);
    root->right=new node(8);
    root->left->right=new node(3);
    root->left->right->left=new node(4);

    // cout<<"hello"<<endl;

    if (balanced(root)){
        cout<<"tree is balanced";
    }
    else{
        cout<<"tree is not balanced";
    }
   

    return 0;
}