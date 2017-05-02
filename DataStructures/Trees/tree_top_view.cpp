// https://www.hackerrank.com/challenges/tree-top-view/
/*
struct node
{
    int data;
    node* left;
    node* right;
};

*/
struct item
{
    node* n;
    int hd;
    item(node* n, int hd) {
        this->n = n;
        this->hd = hd;
    }
};
struct less_than_key
{
    inline bool operator() (const item& struct1, const item& struct2)
    {
        return (struct1.hd < struct2.hd);
    }
};
void top_view(node * root)
{
    std::queue<item*> q;
    std::set<int> s;
    std::vector<item> tops;
    q.push(new item(root, 1));
    while(!q.empty()) {
        item* top = q.front();
        q.pop();
        if(s.find(top->hd) == s.end()) {
            s.insert(top->hd);
            tops.push_back(*top);
        }
        if(top->n->left)
            q.push(new item(top->n->left, top->hd - 1));
        if(top->n->right)
            q.push(new item(top->n->right, top->hd + 1));
    }
    std::sort(tops.begin(), tops.end(), less_than_key());
    for(std::vector<item>::iterator it = tops.begin(); it != tops.end(); ++it) {
        std::cout << (*it).n->data << " ";
    }
    std::cout << std::endl;
}
