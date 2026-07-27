#include <bits/stdc++.h>
using namespace std;
using W = vector<unsigned char>;

pair<int,int> cn(const W& s) {
    int n = (int)s.size();
    vector<int> z(n);
    int l=0,r=0;
    auto at=[&](int i){ return s[n-1-i]; };
    for(int i=1;i<n;i++){
        if(i<r) z[i]=min(r-i,z[i-l]);
        while(i+z[i]<n && at(z[i])==at(i+z[i])) z[i]++;
        if(i+z[i]>r){l=i;r=i+z[i];}
    }
    int bk=1,bp=n;
    for(int p=1;p<n;p++){
        int k=1+z[p]/p;
        if(k>bk || (k==bk && p<bp)){bk=k;bp=p;}
    }
    return {bk,bp};
}

string sw(const W& s){ string x; for(auto c:s)x+=char('0'+c); return x; }

int main(int argc,char**argv){
    int N=argc>1?stoi(argv[1]):18;
    int steps=argc>2?stoi(argv[2]):500;
    long long squares=0,tested=0,fullmatch=0,mismatch=0,terminalmis=0,newrecordmis=0;
    map<tuple<int,int,int,int,int>,long long> pats;
    int printed=0;

    for(int n0=1;n0<=N;n0++){
        uint64_t total=1ULL<<n0;
        for(uint64_t m=0;m<total;m++){
            W s;
            s.reserve(n0+steps+2);
            for(int i=0;i<n0;i++) s.push_back(2+((m>>i)&1));
            int rec=0;
            vector<pair<int,int>> ev;
            ev.reserve(steps+2);

            for(int st=0;st<=steps;st++){
                auto [k,p]=cn(s);
                ev.push_back({k,p});
                bool isrec = p>rec;
                if(isrec){
                    rec=p;
                    if(k==2 && (int)s.size()-p>=n0){
                        squares++;
                        int t=(int)s.size();
                        int startFinal=t-p;
                        int idx=startFinal-n0;
                        if(idx>=0 && idx<(int)ev.size()){
                            int q=ev[idx].second;
                            if(q<p){
                                tested++;
                                W Y(s.end()-p,s.end());
                                int b=p-q;
                                int aLen=2*q-p;
                                if(b>0 && aLen>0 && b+(int)q==(int)Y.size()+0){
                                    W R(Y.begin()+b,Y.end());
                                    if((int)R.size()!=q) continue;
                                    W u=s;
                                    int jmis=-1;
                                    pair<int,int> got{-1,-1};
                                    for(int j=0;j<q;j++){
                                        auto z=cn(u);
                                        if(z.first!=R[j]){ jmis=j; got=z; break; }
                                        if(z.first!=2 && z.first!=3){ jmis=j; got=z; break; }
                                        u.push_back((unsigned char)z.first);
                                    }
                                    if(jmis<0){
                                        fullmatch++;
                                    }else{
                                        mismatch++;
                                        if(got.first!=2 && got.first!=3) terminalmis++;
                                        if(got.second>p) newrecordmis++;
                                        pats[{p,q,jmis,got.first,got.second}]++;
                                        if(printed<40){
                                            cerr<<"MIS seed=";
                                            for(int i=0;i<n0;i++) cerr<<char('0'+2+((m>>i)&1));
                                            cerr<<" t="<<t<<" P="<<p<<" q="<<q
                                                <<" Y="<<sw(Y)<<" R="<<sw(R)
                                                <<" j="<<jmis<<" expect="<<(int)R[jmis]
                                                <<" got="<<got.first<<"/"<<got.second<<"\n";
                                            printed++;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                if(k!=2 && k!=3) break;
                s.push_back((unsigned char)k);
            }
        }
        cerr<<"done n="<<n0<<" squares="<<squares<<" tested="<<tested
            <<" match="<<fullmatch<<" mis="<<mismatch<<"\n";
    }

    cout<<"squares="<<squares<<" tested="<<tested<<" fullmatch="<<fullmatch
        <<" mismatch="<<mismatch<<" terminalmis="<<terminalmis
        <<" newrecordmis="<<newrecordmis<<" kinds="<<pats.size()<<"\n";
    for(auto &[t,c]:pats){
        auto [P,q,j,k,p]=t;
        cout<<P<<"/"<<q<<" j"<<j<<" got"<<k<<"/"<<p<<" count="<<c<<"\n";
    }
    return 0;
}
