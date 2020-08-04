public class Quicksort
{
	public static void quicksort(int a[],int start,int end)
	{
		if(end>start)
		{
			int pivot=end;
			int i=start;
			for(int j=start;j<end;j++)
			{
				if(a[j]<a[pivot])
				{
					int t=a[j];
					a[j]=a[i];
					a[i]=t;
					i++;
				}
			}
			
				int t=a[i];
					a[i]=a[pivot];
					a[pivot]=t;

				quicksort(a,start,i-1);
				quicksort(a,i+1,end);
		}


	}

	public static void main(String[] args) 
	{
		int a[]={0,16, 4, 10, 14, 7, 9, 3, 2, 8, 1};
		quicksort(a,0,a.length-1);
		for(int i: a)
		{
			System.out.print(i+" ");
		}
		System.out.println();

	}
}