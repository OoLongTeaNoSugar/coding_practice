/*
 * @Author: Zhanglei
 * @Date: 2022-02-01 16:39:06
 * @LastEditors: Zhanglei
 * @LastEditTime: 2022-02-11 14:36:23
 * @Description: file content
 */

#include<stdio.h>
#include<unordered_map>
//定义一个双向节点结构
struct DLinkedNode {
    //存值k，v，操作时需要用
    int key, value;
    //前后两个指针
    DLinkedNode* prev;
    DLinkedNode* next;
    //初始化
    DLinkedNode(): key(0), value(0), prev(nullptr), next(nullptr) {}
    DLinkedNode(int _key, int _value): key(_key), value(_value), prev(nullptr), next(nullptr) {}
};

class LRUCache {
private:
    /*hash表+双向链表组成
    哈希表做映射，双项链表做增删改查*/
    std::unordered_map<int, DLinkedNode*> cache;
    //DLNode(k1,v1)<-->DLNode(k2,v2)......
    DLinkedNode* head;
    DLinkedNode* tail;
    int size;
    //最大容量
    int capacity;

public:
    //初始化
    LRUCache(int _capacity): capacity(_capacity), size(0) {
        // 使用伪头部和伪尾部节点
        head = new DLinkedNode();
        tail = new DLinkedNode();
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (!cache.count(key)) {
            return -1;
        }
        // 如果 key 存在，先通过哈希表定位，再移到头部
        DLinkedNode* node = cache[key];
        moveToHead(node);
        return node->value;
    }
    
    void put(int key, int value) {
        if (!cache.count(key)) {
            // 如果 key 不存在，创建一个新的节点
            DLinkedNode* node = new DLinkedNode(key, value);
            // 添加进哈希表
            cache[key] = node;
            // 添加至双向链表的头部
            addToHead(node);
            ++size;
            if (size > capacity) {
                // 如果超出容量，删除双向链表的尾部节点
                DLinkedNode* removed = removeTail();
                // 删除哈希表中对应的项
                cache.erase(removed->key);
                // 防止内存泄漏
                delete removed;
                --size;
            }
        }
        else {
            // 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            DLinkedNode* node = cache[key];
            node->value = value;
            moveToHead(node);
        }
    }

    //增加某个节点
    void addToHead(DLinkedNode* node) {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }
    //移除某个节点
    void removeNode(DLinkedNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    /*将最近使用的移动至头部，O（1）
    先删除，再添加
    */
    void moveToHead(DLinkedNode* node) {
        removeNode(node);
        addToHead(node);
    }

    //移除尾部节点
    DLinkedNode* removeTail() {
        DLinkedNode* node = tail->prev;
        removeNode(node);
        return node;
    }
}; 

