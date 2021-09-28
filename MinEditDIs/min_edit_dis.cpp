#include <iostream>
#include <cstring>
#define maxx 105
#define INF 1e7
using namespace std;

string a,b;
int dis[maxx+5][maxx+5],cnt;
struct routine{
    int i,j;
} rou[10*maxx+5];

int cal_min_edit_dis(){
    for(int i=0;i<=maxx;i++){
        for(int j=0;j<=maxx;j++){
            dis[i][j]=INF;
        }
    }
    for(int i=0;i<=maxx;i++){
        dis[i][0]=i;
    }
    for(int j=0;j<=maxx;j++){
        dis[0][j]=j;
    }
    for(int i=1;i<=a.length();i++){
        for(int j=1;j<=b.length();j++){
            dis[i][j]=min(dis[i][j],dis[i-1][j]+1);
            dis[i][j]=min(dis[i][j],dis[i][j-1]+1);
            if(a[i-1]!=b[j-1]){
                dis[i][j]=min(dis[i][j],dis[i-1][j-1]+2);
            }
            else{
                dis[i][j]=min(dis[i-1][j-1],dis[i][j]);
            }
        }
    }
    return dis[a.length()][b.length()];
}

void assign(int i,int j){
    rou[cnt].i=i;
    rou[cnt].j=j;
}

void back_trace(int i,int j){//当前位置
    if(i==0||j==0) return;
    cnt++;
    assign(i,j);
    if(a[i-1]!=b[j-1]){
        if(dis[i][j]==dis[i-1][j-1]+2){
            back_trace(i-1,j-1);
            return;
        }
    }
    else{
        if(dis[i][j]==dis[i-1][j-1]){
            back_trace(i-1,j-1);
            return;
        }
    }
    if(dis[i][j]==dis[i-1][j]+1){
        back_trace(i-1,j);
        return;
    }
    if(dis[i][j]==dis[i][j-1]+1){
        back_trace(i,j-1);
        return;
    }
}

int main(){
    cin>>a>>b;
    cout<<cal_min_edit_dis()<<endl;
    back_trace(a.length(),b.length());
    for(int i=a.length();i>=1;i--){
        cout<<a[i-1]<<' ';
        for(int j=1;j<=b.length();j++){
            cout<<dis[i][j]<<' ';
        }
        cout<<endl;
    }
    cout<<"  ";
    for(int j=1;j<=b.length();j++) cout<<b[j-1]<<' ';
    cout<<endl<<"min_edit_dis_path is :"<<endl;
    for(int i=cnt;i>=1;i--){
        cout<<'('<<rou[i].i<<','<<rou[i].j<<')'<<endl;
    }
}