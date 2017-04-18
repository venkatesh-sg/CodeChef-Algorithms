#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{
	int T,N,Q,L,R,K;
	int i,j,k,od,oda,q;
	int *s;
	scanf("%d", &T);
	for(i=0;i<T;i++){
		scanf("%d %d",&N,&Q);
		s = malloc(N * sizeof(int));
		for(j=0;j<N;j++){
			scanf("%d",&s[j]);
		}
		for(k=0;k<Q;k++){
			scanf("%d %d %d",&L,&R,&K);
			oda=0;
			od=0;
			for(q=L-1;q<R-1;q++){
				if(s[q]==s[q+1]){
					od=od+1;
				}
				else{
					od=0;
				}
				if(od==K-1){
					oda=oda+1;
				}
			}
			if(K==1){
				oda=oda+1;
			}
			printf("%d\n",oda);
		}
	}
	free(s);
	return 0;
}
