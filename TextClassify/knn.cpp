#include <iostream>
#include <cstdlib>
#include <cstdio>

#define MAXX 21005
#define len 14675
#define num 19997

using namespace std;

double temp;
int cnt=0,cnt0=1,err=0,cnt_err=0;
int dis[MAXX][MAXX],cate[MAXX],fin[MAXX];

struct element{
    int cate;
    double value;
} ele[MAXX][MAXX];

void init(){
    for (int i=1;i<=num;i++){
        if(!(rand()%3)){
            fin[i]=1;
        } 
    }
    return;
}

int main(){

    FILE *fp;

    fp=freopen("./data/x.txt","r",stdin);
    cout<<"check 1"<<endl;
    while(scanf("%lf",&temp)){
        cnt++;
        //cout<<cnt<<endl;
        if(cnt>len){
            cnt=1;
            cnt0++;
            if(cnt0%100==0) printf("%d ",cnt0);
        }
        ele[cnt0][cnt].value=temp;
        //cout<<cnt<<' '<<int(temp)<<endl;
    }
    fclose(fp);
    cout<<"i"<<cnt0<<" j"<<cnt<<endl;
    return 0;

    fp=freopen("./data/y.txt","r",stdin);
    cnt=0;
    while("%lf",&temp){
        cate[cnt++]=int(temp);
        //cout<<cnt<<' '<<temp<<endl;;
    }
    fclose(fp);

    init(); //初始化,撒种子,33%
    
    for(int i=1;i<=num;i++){
        for(int j=1;j<=num;j++){
            if(i==j){
                dis[i][i]=-1;
                continue;    
            }

        }
    }
}
