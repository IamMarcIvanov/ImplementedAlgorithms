public class Heapsorto
{
	static int parent(int i)
	{
		return((int)Math.floor(i/2.0));
	}
	static int left(int i)
	{
		return(2*i);
	}
	static int right(int i)
	{
		return((2*i)+1);
	}
	static void max_heapify(int a[], int i, int hsize)
	{
		int l=left(i);
		int r=right(i);
		int largest;


		if(l<=hsize&&a[l]>a[i])
		{
			largest=l;
		}
		else
		{
			largest=i;
		}
		if(r<=hsize&&a[r]>a[l])
		{
			largest=r;
		}

		if(largest!=i)
		{
			int t=a[i];
			a[i]=a[largest];
			a[largest]=t;
			max_heapify(a,largest,hsize);
		}
		
	}


	static void build_max_heap(int b[])
	{
		int t=(int)Math.floor((b.length-1)/2);
		for(int i=t;i>0;i--)
		{
			max_heapify(b,i,b.length-1);
		}
	}
	static void print_heap(int a[])
	{
		for (int i=1;i<a.length ;i++ ) {
			System.out.print(a[i]+" ");
		}
		System.out.println();
	}

	static void heapsort(int a[])
	{
		build_max_heap(a);
		// print_heap(a);
		for(int hsize=a.length-1;hsize>1;hsize--)
		{
			int t=a[1];
			a[1]=a[hsize];
			a[hsize]=t;
			print_heap(a);
			System.out.println("before");
			max_heapify(a,1,hsize-1);
			print_heap(a);
		}
	}


	public static void main(String[] args) 
	{
		int a[]={0,16, 4, 10, 14, 7, 9, 3, 2, 8, 1};


		int b[]={0,4,1,3,2,16,9,10,14,8,7};


		
		

		 heapsort(b);
		//  int c[]={0,1,2,3};
		//  max_heapify(c,1,c.length-1);
		// print_heap(c);
		// max_heapify(c,1,c.length-1);
		// print_heap(c);
	}
}