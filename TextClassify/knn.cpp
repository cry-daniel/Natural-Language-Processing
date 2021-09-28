#include <iostream>
#include <cstdlib>
#define MAXX 20005
using namespace std;

double temp;
int cnt=0,err=0,cnt_err=0;
int near[MAXX],cate[MAXX],res[MAXX];

void init(){
    for(int i=1;i<=cnt;i++){
        if(i%3==0){
            near[i]=i;
            res[i]=cate[i];
        }
    }
}

int find(int x){
    err++;
    if(err>20000) return -1;
    if(res[x]) return res[x];
    else return find(near[x]);
}

int main(){
    FILE *fp;
    fp=freopen("./data/near.txt","r",stdin);
    while(cin>>temp){
        near[cnt++]=int(temp);
        //cout<<cnt<<' '<<int(temp)<<endl;
    }
    fclose(fp);
    cin.clear();
    fp=freopen("./data/y.txt","r",stdin);
    cnt=0;
    while(cin>>temp){
        cate[cnt++]=int(temp);
        //cout<<cnt<<' '<<temp<<endl;;
    }
    fclose(fp);
    cin.clear();
    init();
    for(int i=1;i<=cnt;i++){
        if(res[i]) continue;
        else{
            err=0;
            res[i]=find(i);
        }
        if(res[i]==-1) cnt_err++;
        cout<<i<<' '<<res[i]<<endl;
    }
    cout<<"cnt_err"<<' '<<cnt_err<<endl;
}