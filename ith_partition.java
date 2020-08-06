import java.util.*;
public class ith_partition
{
	//this function is called quicksort, however it returns ith partition
	public static void quicksort(int a[],int start,int end, int k)
	{
		if(end>=start)
		{
			int n=a.length;

			Random r=new Random();
			int x=start+r.nextInt(end-start+1);

			//swapping rando and last
			aswap(a,x,end);


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

			if(i==k)
			{
				System.out.println(a[i]+ " "+ i);
				return;
			}
			// System.out.println(a[i]+ " "+ i);
			else if(i>k)
				quicksort(a,start,i-1,k);
			else
				quicksort(a,i+1,end,k);
		}
	}
	

			
	public static void aswap(int a[],int i,int j)
	{
		int t=a[i];
		a[i]=a[j];
		a[j]=t;
	}

	public static void main(String[] args) 
	{
		int a[]={0,16, 4, 10, 14, 7, 9, 3, 2, 8, 1};
		// int a[]={-383, 385, -591, -272, 247};
		quicksort(a,0,a.length-1,4);
		System.out.println();
		for (int i: a ) 
		{
			System.out.print(i+" ");	
		}
		

	}
}