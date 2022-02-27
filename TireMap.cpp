/*
 * @Author: Zhanglei
 * @Date: 2022-02-12 16:12:08
 * @LastEditors: Zhanglei
 * @LastEditTime: 2022-02-22 22:32:37
 * @Description: file content
 */



#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

struct TrieNode
{
    /* data */
    vector<TrieNode*> children = vector<TrieNode*>(26);
    string word;
    TrieNode(){}
};

template < class V>
class TireMap
{
public:

    int size(){
        return size;
    }
    /*增/改*/
    void put(string key, V val);

    /*删除*/
    void remove(string key);

    /*查询 存在返回V类型，不存在返回Null*/
    V get(string key);



private:
    /* data */
    static final int R = 256; // ASCII 码个数
    int size = 0; // 当前map内key的数量
    
    static struct TireNode
    {
        /* data */
        V* val = nullptr;
        vector<TrieNode*> children = vector<TrieNode*>(R);
    };

    TrieNode* root = nullptr;


        
public:
    TireMap(/* args */);
    ~TireMap();
};



