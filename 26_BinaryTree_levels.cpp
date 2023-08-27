#include<iostream>
using namespace std;

class node{
    public:
        int val;
        node* left;
        node* right;
        node(int data){
            val=data;
            left=right=NULL;
        }
};

int finder(node* root){
    return max(root->left->val,root->right->val);
}

int levels(node* temp){
    if (temp->left==NULL && temp->right==NULL){
        
    }
}

int main(){
    node* root=new node(5);
    root->left=new node(2);
    root->right=new node(8);
    root->left->right=new node(3);
    root->left->right->left=new node(4);

    // cout<<"hello"<<endl;

    

    return 0;
}
