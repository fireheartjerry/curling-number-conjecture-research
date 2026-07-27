#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>

static bool primitive(const std::vector<int>& w) {
    const int n = (int)w.size();
    for (int p=1;p<n;++p) if (n%p==0) {
        bool ok=true; for(int i=p;i<n;++i) if(w[i]!=w[i%p]) {ok=false;break;}
        if(ok) return false;
    }
    return true;
}

static int pc(const std::vector<int>& w,int cut) {
    const int n=(int)w.size(); int best=1;
    for(int p=1;p<n;++p) {
        int e=1;
        while(e<4) {
            bool ok=true;
            for(int j=0;j<p;++j) if(w[(cut-(e+1)*p+j%n+n*10)%n]!=w[(cut-p+j+n*10)%n]) {ok=false;break;}
            if(!ok) break; ++e;
        }
        best=std::max(best,e); if(best>=4) return best;
    }
    return best;
}

int main(int argc,char**argv) {
    if(argc!=3) return 2; int n=std::atoi(argv[1]), sigma=std::atoi(argv[2]);
    std::uint64_t total=1; for(int i=0;i<n;++i) total*=sigma;
    std::uint64_t admissible=0,weighted=0; bool shown=false;
    for(std::uint64_t code=0;code<total;++code) {
        std::uint64_t x=code; std::vector<int>w(n),f(n);
        for(int i=0;i<n;++i){w[i]=x%sigma;x/=sigma;}
        if(w[0]!=0 || !primitive(w)) continue;
        bool ok=true;for(int i=0;i<n;++i){f[i]=pc(w,i);if(f[i]<2||f[i]>3){ok=false;break;}}
        if(!ok) continue; ++admissible;
        std::map<int,int> weight;
        for(int i=0;i<n;++i){auto [it,ins]=weight.emplace(w[i],f[i]);if(!ins&&it->second!=f[i]){ok=false;break;}}
        if(!ok) continue; ++weighted;
        if(!shown){shown=true;std::cout<<"model=";for(int a:w)std::cout<<a;std::cout<<" profile=";for(int a:f)std::cout<<a;std::cout<<" weights=";for(auto [a,b]:weight)std::cout<<a<<":"<<b<<",";std::cout<<"\n";}
    }
    std::cout<<"n="<<n<<" sigma="<<sigma<<" admissible="<<admissible<<" weighted="<<weighted<<"\n";
}
