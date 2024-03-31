#include<iostream>
using namespace std;

class TrieNode{
    public:
    char data;
    TrieNode* children[26];
    bool isTerminal;
    TrieNode(char ch){
        data=ch;
        for(int i=0;i<26;i++){
            children[i]=NULL;
        }
        isTerminal=false;
    }

};
class Trie{
    public:
    TrieNode* root;
    Trie(){
       root = new TrieNode('\0');
    }
    void insertUntil(TrieNode* root,string word){
        //base case where length of word length become zero 
        if(word.length()==0){
            root->isTerminal=true;
            return;
        }
        //here we are asuming input is in capital letter
        int index=word[0]-'A';
        TrieNode* child;
        //if the word is present 
        if(root->children[index]!=NULL){
            child=root->children[index];
        }
        //if the word is not present
        else{
            child=new TrieNode(word[0]);
            root->children[index]=child;
        }
        //recurssion
     return insertUntil(child,word.substr(1));
    }
    void insertWord(string word){
        insertUntil(root,word);
    }
    bool searchUntil(TrieNode* root,string word){
        //base case where length of word becomes zero
        if(word.length()==0){
            return root->isTerminal;
        }
        int index=word[0]-'A';
        TrieNode* child;
        //if word is present
        if(root->children[index]!=NULL){
            child=root->children[index];
        }
        //not present
        else{
            return false;
        }
        return searchUntil(root,word.substr(1));
    }
    bool searchWord(string word){
       return searchUntil(root,word);
    }
};
int main(){
   Trie* t=new Trie();
   t->insertWord("ABCD");
   cout<<"present or not"<<t->searchWord("ABCl")<<endl;
   return 0;
}