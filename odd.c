#include <stdio.h>
#include <stdlib.h>

void main()
{
	/* code */
	int i,n,arr[n],ans;
	printf("Enter the number of inputs: \n");
	scanf("%d", &n);
	for (i=0; i<n; i++)
	{
		/* code */
		scanf("%d",&arr[i]);
	}
	for (i=0; i<n; i++)
	{
		if(i%2!=0)
			ans = arr[i];
	}
	printf("%d\n",ans);
}
