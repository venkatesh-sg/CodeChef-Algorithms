#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{
	int T,N,K,P
	int i,j
	int *s;
	scanf("%d",&T);
	for(i=0;i<T;i++){
		scanf("%d %d",&N,&K);
		for(j=0;j<N;j++){
			scanf("%d",&P);
			s = malloc(P * sizeof(int));
			for(k=0;k<P;k++){
				scanf("%d",&s[k]);
			}
			
		}
	}
}

